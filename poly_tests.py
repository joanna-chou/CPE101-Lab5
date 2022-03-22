# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Joanna Chou
# Section: 07

import unittest
from poly import *

class TestPoly(unittest.TestCase):
   #do not delete this part, use this to comapre two lists
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)
   
   def test_polyadd2(self):	# Tests for add function
      poly_list1 = [2.3, 4.7, 1.0] 
      poly_list2 = [1.2, 2.1, -3.2] 
      poly_new_list1 = poly_add2(poly_list1, poly_list2)
      self.assertListAlmostEqual(poly_new_list1, [3.5, 6.8, -2.2])

      poly_list3 = [3, 5, 0] 
      poly_list4 = [-2, 4, 6.6] 
      poly_new_list2 = poly_add2(poly_list3, poly_list4)
      self.assertListAlmostEqual(poly_new_list2, [1, 9, 6.6])

      poly_list5 = [2.2, 4, 13] 
      poly_list6 = [0, 33, 5] 
      poly_new_list3 = poly_add2(poly_list5, poly_list6)
      self.assertListAlmostEqual(poly_new_list3, [2.2, 37, 18])

   def test_polymult2(self):
      poly_list1 = [2, 2, 1]
      poly_list2 = [1, 2, 2]
      poly_new_list = poly_mult2(poly_list1, poly_list2)
      self.assertListAlmostEqual(poly_new_list, [2, 6, 9, 6, 2])

      poly_list1 = [0, 5, 1]
      poly_list2 = [2, 0, 2]
      poly_new_list = poly_mult2(poly_list1, poly_list2)
      self.assertListAlmostEqual(poly_new_list, [2, 10, 2, 10, 0])

      poly_list1 = [5, 0, -2]
      poly_list2 = [5, 0, 2]
      poly_new_list = poly_mult2(poly_list1, poly_list2)
      self.assertListAlmostEqual(poly_new_list, [-4, 0, 0, 0, 25])

if __name__ == '__main__':
   unittest.main()
