# CPE 101-01
# LAB 5: Map Function Tests
# Name: Joanna Chou
# Section: 07

#Purpose Statement: This function cubes each value in a given list.
#Signature: list -> list
def cube_all(cube_list):
    new_list = []
    for item in cube_list:
        new_list.append((item**3))
    return new_list

#Purpose Statement: This function adds a value to each value in a given list.
#Signature: list float -> list
def add_n_to_all(n_list, num):
    new_list = []
    i = 0
    while i < len(n_list):
        new_list.append(n_list[i]+ num)
        i += 1
    return (new_list)

#Purpose Statement: This function takes a given list and returns a list containing True or False depending on if the corresponding value in the input list is divisible by five.
#Signature: list -> list
def div_by_5_all(div_list):
    new_list = [(item % 5 == 0) for item in div_list]
    return new_list



