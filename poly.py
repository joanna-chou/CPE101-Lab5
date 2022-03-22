# CPE 101-01
# LAB 5: Polynomial Functions
# Name: Joanna Chou
# Section: 07

#Purpose Statement: This function takes two lists (polynomial coefficients with degrees corresponding to their indices) and returns the sum of the polynomial lists in a new list.
#Signature: list list -> list
def poly_add2(poly_list1, poly_list2):
    poly_new_list = []
    poly_new_list.append(poly_list1[0]+poly_list2[0])
    poly_new_list.append(poly_list1[1]+poly_list2[1])
    poly_new_list.append(poly_list1[2]+poly_list2[2])
    return(poly_new_list)

#Purpose Statement: This function takes two lists (polynomial coefficients with degrees corresponding to their indices), and through the FOIL method, returns the product of the polynomial lists in a new list. 
#Signature: list list -> list
def poly_mult2(poly_list1, poly_list2):
    poly_new_list = []
    poly_new_list.append(poly_list1[2]* poly_list2[2])
    poly_new_list.append((poly_list1[2]* poly_list2[1]) + (poly_list1[1]* poly_list2[2]))
    poly_new_list.append((poly_list1[2]* poly_list2[0]) + (poly_list1[1]*poly_list2[1]) + (poly_list1[0]*poly_list2[2]))
    poly_new_list.append((poly_list1[1]* poly_list2[0]) + (poly_list1[0]*poly_list2[1]))
    poly_new_list.append(poly_list1[0]* poly_list2[0])
    return(poly_new_list)