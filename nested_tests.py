# CPE 101-01
# LAB 5: Map Function Tests
# Name: Joanna Chou
# Section: 07

import unittest
from nested import *

class TestPoly(unittest.TestCase):
   #do not delete this part, use this to comapre two lists
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)
   
   def test_product(self):
      nested_list1 = [[1,2], [2,3,4], [-2,5]] 
      self.assertListAlmostEqual(product(nested_list1), [2, 24, -10])

      nested_list2 = [[2, 5], [3, 6]] 
      self.assertListAlmostEqual(product(nested_list2), [10, 18])

      nested_list3 = [[-4, 8, 2], [3, 7, 8]] 
      self.assertListAlmostEqual(product(nested_list3), [-64, 168])


if __name__ == '__main__':
   unittest.main()
