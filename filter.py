# CPE 101-01
# LAB 5: Map Function Tests
# Name: Joanna Chou
# Section: 07

#Purpose Statement: This function takes a list and returns a list of all even values in the given list.
#Signature: list -> list
def are_even(even_list):
    new_list = []
    for item in even_list:
        if item % 2 == 0:
            new_list.append((item))
    return new_list

#Purpose Statement: This function takes a list and returns a new list with duplicates removed.
#Signature: list -> list
def remove_duplicates(duplicates_list):
    new_list = []
    i = 0
    while i < len(duplicates_list):
        if duplicates_list[i] not in new_list:
            new_list.append(duplicates_list[i])
        i += 1
    return new_list

#Purpose Statement: This function takes a list and a number and returns a list containing the values in the list that are divisible by the number.
#Signature: list float -> list
def are_divisible_by_n(divisible_list, num):
    new_list = [item for item in divisible_list if (item % num == 0)]
    return new_list