from typing import OrderedDict
from collections import defaultdict


class InventoryAllocator:

    def __init__(self, inventory):
        """
        function that initializes the warehouse.
        params:
            inventory: dictionary mapping warehouse to it's inventory
        """
        self.warehouse_stock = OrderedDict()
        self.set_warehouse(inventory)

    def set_warehouse(self, inventory):
        """
        function that sets and updates inventories .
        params:
            inventory : dict
                dictionary containing information about single/multiple warehouses and their inventory
        """

        for warehouse in inventory:
            if warehouse["name"] not in self.warehouse_stock:
                self.warehouse_stock[warehouse["name"]] = warehouse["inventory"]
            else:
                for item, quantity in warehouse["inventory"].items():
                    if item not in self.warehouse_stock[warehouse["name"]]:
                        self.warehouse_stock[warehouse["name"]][item] = warehouse["inventory"][item]
                    else:
                        self.warehouse_stock[warehouse["name"]][item] = (quantity + self.warehouse_stock[warehouse["name"]][item])



    def update_stock(self, warehouse_name, item_name, item_stock):
        """
        function that updates stock in a specific warehouse.
        params:
            warehouse_name : str
                Name of warehouse to update.

            item_name : str
                Name of item to update.
            item_stock : int
                Amount of item to update.
        """
        self.warehouse_stock[warehouse_name][item_name] = item_stock

    def create_shipment_detail(self, order):
        """
        function used to find cheapest way to fullfill order
        params:
            order: A dictionary that maps item needed to amount of item needed
        """

        warehouse_item_distribution_amounts = defaultdict(lambda: {})
        for item_name, amount_required in order.items():
            item_distribution_amounts = {}

            for warehouse_name, warehouse_inventory in self.warehouse_stock.items():

                if item_name not in warehouse_inventory or warehouse_inventory[item_name] <= 0:
                    continue

                item_stock = warehouse_inventory[item_name]

                if amount_required <= item_stock:
                    item_distribution_amounts[warehouse_name] = amount_required
                    item_stock -= amount_required
                    amount_required = 0
                    self.update_stock(warehouse_name, item_name, item_stock)
                    break

                elif amount_required > item_stock:
                    item_distribution_amounts[warehouse_name] = item_stock
                    amount_required -= item_stock
                    item_stock = 0
                    self.update_stock(
                        warehouse_name, item_name, item_stock
                    )

            if amount_required > 0:
                return []

            for warehouse_name, amount in item_distribution_amounts.items():
                warehouse_item_distribution_amounts[warehouse_name][item_name] = amount

        final_allocation = []

        for name, items in warehouse_item_distribution_amounts.items():
            final_allocation.append({name: items})

        return final_allocation
