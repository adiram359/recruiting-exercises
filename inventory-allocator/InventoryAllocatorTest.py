import unittest
from collections import OrderedDict
from InventoryAllocator import InventoryAllocator


class InventoryAllocatorTest(unittest.TestCase):
    def test_exact(self):
        """
        This test checks that the output is correct if the order matches the
        warehouse inventory exactly.
        """
        order = {"orange": 3}
        inventory = [{"name": "warehouse1", "inventory": {"orange": 3}}]
        correct_output = [{"warehouse1": {"orange": 3}}]

        inventory_allocator = InventoryAllocator(inventory)
        self.assertEqual(inventory_allocator.create_shipment_detail(order), correct_output)

    def test_not_enough_inventory(self):
        """
        This test checks if there is not enough inventory
        """
        order = {'strawberry': 1}
        inventory = [{'name': 'warehouse1', 'inventory': {'strawberry': 0}}]
        correct_output = []
        inventory_allocator = InventoryAllocator(inventory)
        self.assertEqual(inventory_allocator.create_shipment_detail(order), correct_output)

    def test_no_order_no_inventory(self):
        """
        This test checks if no order is placed or if no inventory details are given
        """
        order = {}
        inventory = []
        correct_output = []
        inventory_allocator = InventoryAllocator(inventory)
        self.assertEqual(inventory_allocator.create_shipment_detail(order), correct_output)

    def test_multiple_source(self):
        """
        This test checks that the output is correct when the item needs to be
        collected from > 1 warehouses.
        """
        order = {"melon": 12}
        inventory = [
            {"name": "warehouse1", "inventory": {"melon": 0}},
            {"name": "warehouse2", "inventory": {"melon": 5}},
            {"name": "warehouse3", "inventory": {"melon": 9}},
        ]
        correct_output = [{'warehouse2': {'melon': 5}}, {'warehouse3': {'melon': 7}}]

        inventory_allocator = InventoryAllocator(inventory)
        self.assertEqual(inventory_allocator.create_shipment_detail(order), correct_output)

    def test_zero_inventory_some(self):
        """
        This test checks that the output is correct when
        some of the warehouses do not contain inventory of the item
        """
        order = {"apple": 4}
        inventory = [
            {"name": "warehouse1", "inventory": {"apple": 0}},
            {"name": "warehouse2", "inventory": {"orange": 15}},
            {"name": "warehouse3", "inventory": {"apple": 4}},
            {"name": "warehouse4", "inventory": {"apple": 11}},
        ]
        correct_output = [{"warehouse3": {"apple": 4}}]

        inventory_allocator = InventoryAllocator(inventory)
        self.assertEqual(inventory_allocator.create_shipment_detail(order), correct_output)

    def test_split_across_warehouses(self):
            """
            This test checks that the output is correct when
            > 1 items need to come from > 1 sources.
            """
            order = {'apple': 15, 'banana': 5, 'orange': 5}
            inventory = [{'name': 'warehouse1', 'inventory': {'apple': 5, 'orange': 10}},
                         {'name': 'warehouse2', 'inventory': {'apple': 10, 'banana': 5, 'orange': 10}}]
            correct_output = [{'warehouse1': {'apple': 5, 'orange': 5}}, {'warehouse2': {'apple': 10, 'banana': 5}}]
            inventory_allocator = InventoryAllocator( inventory)
            self.assertEqual(inventory_allocator.create_shipment_detail(order),correct_output)

    def test_pick_cheapest(self):
        """
        This test checks that the output is correct when an item is at multiple
        warehouses
        """
        order = {"lemon": 4}
        inventory = [
            {"name": "warehouse1", "inventory": {"lemon": 22}},
            {"name": "warehouse2", "inventory": {"lemon": 6}},
            {"name": "warehouse3", "inventory": {"lemon": 5}},
            {"name": "warehouse4", "inventory": {"lemon": 6}},
        ]
        correct_output = [{"warehouse1": {"lemon": 4}}]

        inventory_allocator = InventoryAllocator(inventory)
        self.assertEqual(inventory_allocator.create_shipment_detail(order), correct_output)

    def test_exact_matches(self):
        """
        This test checks that the output is correct when there are exact matches with
        the necessary items.
        """
        order = {"blueberry": 8, "rasberry": 8}
        inventory = [{"name": "warehouse1", "inventory": {"blueberry": 10}},
                    {"name": "warehouse2", "inventory": {"rasberry": 10}}

        ]
        correct_output = [{'warehouse1': {'blueberry': 8}}, {'warehouse2': {'rasberry': 8}}]

        inventory_allocator = InventoryAllocator(inventory)
        self.assertEqual(inventory_allocator.create_shipment_detail(order), correct_output)

    def test_all_but_one(self):
        """
        This test checks that the output is correct when
        all but one item can be fullfilled
        """
        order = {"lime": 3, "cherry": 2}
        inventory = [
            {"name": "warehouse1", "inventory": {"lime": 1}},
            {"name": "warehouse2", "inventory": {"cherry": 0, "lime":2 }},
        ]
        correct_output = []

        inventory_allocator = InventoryAllocator(inventory)
        self.assertEqual(inventory_allocator.create_shipment_detail(order), correct_output)


if __name__ == "__main__":
    unittest.main()
