# CPE 101-01
# LAB 5: Map Function Tests
# Name: Joanna Chou
# Section: 07

import unittest
from filter import *

class TestPoly(unittest.TestCase):
   #do not delete this part, use this to comapre two lists
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)
   
   def test_are_even(self):
      even_list1 = [1,2,3] 
      self.assertListAlmostEqual(are_even(even_list1), [2])

      even_list2 = [8, 69, 6.9] 
      self.assertListAlmostEqual(are_even(even_list2), [8])

      even_list3 = [13, 0, -4] 
      self.assertListAlmostEqual(are_even(even_list3), [0, -4])

   def test_remove_duplicates(self):
      duplicates_list1 = [1, 2, 3, 2]
      self.assertListAlmostEqual(remove_duplicates(duplicates_list1), [1, 2, 3])

      duplicates_list2 = [1738, 1249, 1249, 631]
      self.assertListAlmostEqual(remove_duplicates(duplicates_list2), [1738, 1249, 631])

      duplicates_list3 = [9, -4, 0, 0, 0, -1, -2]
      self.assertListAlmostEqual(remove_duplicates(duplicates_list3), [9, -4, 0, -1, -2])

   def test_are_divisible_by_n(self):
      div_list1 = [24, 13, 32]
      self.assertListAlmostEqual(are_divisible_by_n(div_list1, 6), [24])

      div_list2 = [39, 42, 3.1]
      self.assertListAlmostEqual(are_divisible_by_n(div_list2, 3), [39, 42])

      div_list3 = [2173649, 94285, 536893]
      self.assertListAlmostEqual(are_divisible_by_n(div_list3, 2), [])


if __name__ == '__main__':
   unittest.main()
