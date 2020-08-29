# recruiting-exercises

# Solution


## Aditya Ramaakrusnan
## adityaramaakrushnan@gmail.com

### Language: Python3

### Solution Approach:
Being by looping through the order items and cross checking against all warehouses. If a warehouse has sufficient stock, I record this and continue onto the next item. If a warehouse cannot full-fill the amount of a certain item, I grab all the stock of the item and move onto the next warehouse. If I am not able to full-fill an item after looping through the list, the order cannot be full-filled. After trying to grab a sufficient amount of a given item, I move onto the next item. This guarantees the right answer as long as the list contains the warehouses in order of increasing cost

#### Unit Tests
1. Ensure the output is correct if the order matches the warehouse inventory exactly.
2. Ensure the output is correct if there is not enough inventory
3.  Ensure the output is correct if no order is placed or if no inventory details are given
4. Ensure the output is correct if the item needs to be collected from > 1 warehouses.
5. Ensure the output is correct if some of the warehouses do not contain inventory of the item
6. Ensure the output is correct when > 1 items need to come from > 1 sources
7. Ensure the output is correct when an item is at multiple warehouses
8. Ensure the output is correct when there are exact matches with the necessary items
9. Ensure the output is correct when all but one item can be fullfilled
