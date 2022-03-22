# CPE 101-01
# LAB 5: Map Function Tests
# Name: Joanna Chou
# Section: 07

import unittest
from map import *

class TestPoly(unittest.TestCase):
   #do not delete this part, use this to comapre two lists
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)
   
   def test_cube_all(self):
      cube_list1 = [1,2,3] 
      self.assertListAlmostEqual(cube_all(cube_list1), [1,8,27])

      cube_list2 = [3.3,-2] 
      self.assertListAlmostEqual(cube_all(cube_list2), [35.937,-8])

      cube_list3 = [1.1,0,4] 
      self.assertListAlmostEqual(cube_all(cube_list3), [1.331,0, 64])

   def test_add_n_to_all(self):
      n_list1 = [2, 3,65]
      self.assertListAlmostEqual(add_n_to_all(n_list1, 5), [7, 8, 70])

      n_list2 = [45.3, -2, 0, 0.1]
      self.assertListAlmostEqual(add_n_to_all(n_list2, -2), [43.3, -4, -2, -1.9])

      n_list3 = [9, -4]
      self.assertListAlmostEqual(add_n_to_all(n_list3, 1.1), [10.1, -2.9])

   def test_div_by_5_all(self):
      div_list1 = [1, 5, 10]
      self.assertListAlmostEqual(div_by_5_all(div_list1), [False, True, True])

      div_list2 = [-5, 55, 2, 0, 1.4]
      self.assertListAlmostEqual(div_by_5_all(div_list2), [True, True, False, True, False])

      div_list2 = [1000000, 10000001, -10]
      self.assertListAlmostEqual(div_by_5_all(div_list2), [True, False, True])

if __name__ == '__main__':
   unittest.main()
