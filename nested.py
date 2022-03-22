# CPE 101-01
# LAB 5: Map Function Tests
# Name: Joanna Chou
# Section: 07

#Purpose Statement: This function takes a nested intergest list and returns a list such that each integer is the product of the inner list.
#Signature: list -> list
def product(nested_list):
    new_list = []
    for items in nested_list:
        new_item = 1
        for item in items:
            new_item = item * new_item
        new_list.append((new_item))
    return new_list