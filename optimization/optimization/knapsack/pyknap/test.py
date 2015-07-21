#!/usr/bin/python
# (c) 2015 Christopher Thompson
# license: https://github.com/cjt5144/Cython-Cpp-Examples/blob/master/LICENSE

import unittest
import knapsack
import bag
import bagset

items = (
		("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
		("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
		("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
		("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
		("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
		("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
		("socks", 4, 50), ("book", 30, 10),
		)
		

class Knapsack01TestWithLimit400(unittest.TestCase):


	def setUp(self):
	
		self.result = knapsack.knapsack01(items, 400)
		
	def test_total_value_of_items_equals_1030_with_limit_400(self):
	
		_, totalval, _ = self.result
		self.assertEqual(1030, totalval)
		
	def test_total_weight_of_items_equals_396_with_limit_400(self):
	
		_, _, totalwt = self.result
		self.assertEqual(396, totalwt)
		

class Knapsack01TestWithLimit100Size2(unittest.TestCase):


	def setUp(self):
	
		self.result = knapsack.knapsack01(items, 100, 2)
		
	def test_total_value_of_items_equals_310_with_limit_100_size_2(self):
	
		_, totalval, _, _ = self.result
		self.assertEqual(310, totalval)
		
	def test_total_weight_of_items_equal_59_with_limit_100_size_2(self):
	
		_,_,totalwt,_ = self.result
		self.assertEqual(59,totalwt)
		
	def test_isFilled_true_with_limit_100_size_2(self):
	
		self.assertTrue(self.result[3])
		

class BagInitializationTest(unittest.TestCase):


	def setUp(self):
	
		self.Bag = bag.Bag
	
	def test_bag_init_returns_error_with_string_inputs(self):
	
		self.assertRaises(ValueError, self.Bag, ['y', 'x'],3, 'df')
		self.assertRaises(ValueError, self.Bag, ['y', 'x'],'3', 5)
		self.assertRaises(ValueError, self.Bag, ['y', 'x'],'3', 'df')
		
	def test_bag_init_returns_error_with_no_tuple_input(self):
	
		self.assertRaises(ValueError, self.Bag, ['y', 'x'],3, 5)
	
	def test_bag_init_returns_error_with_no_item_tuples(self):
	
		self.assertRaises(ValueError, self.Bag, (('y'), 'x'),3, 5)
		self.assertRaises(ValueError, self.Bag, ('y', ('x')),3, 5)
		self.assertRaises(ValueError, self.Bag, ('y', 'x'),3, 5)
		self.assertRaises(ValueError, self.Bag, (['y'], ['x']),3, 5)
		self.assertRaises(ValueError, self.Bag, (['y',3], ['x',2]),3, 5)
		
	def test_bag_init_returns_error_with_tuple_length_not_3(self):
	
		self.assertRaises(ValueError, self.Bag, (('y',3), ('x',2)),3, 5)
		self.assertRaises(ValueError, self.Bag, (('y',3,'3'), ('x',2)),3, 5)
		self.assertRaises(ValueError, self.Bag, (('y',3), ('x',2,'a')),3, 5)
		self.assertRaises(ValueError, self.Bag, (('y'), ('x')),3, 5)
		

class BagKnapsackTestLimit400SizeNone(unittest.TestCase):
	
	
	def setUp(self):
		
		self.bag = bag.Bag(items, 400)
		
	def test_total_value_equals_1030_with_weight_400(self):
		
		_,totalval,_ = self.bag.knapsack01()
		self.assertEqual(1030, totalval)
	
	def test_total_weight_equal_396_with_weight_400(self):
		
		_,_,totalwt = self.bag.knapsack01()
		self.assertEqual(396, totalwt)
		
	
class BagKnapsackTestLimit100Size2(unittest.TestCase):
	
	
	pass
	
	
class BagSetInitializationTest(unittest.TestCase):
	
	
	def setUp(self):
		
		self.bagset	= bagset.BagSet
		
	def test_bagset_init_returns_type_error_with_items_not_dict(self):
	
		self.assertRaises(TypeError, self.bagset, 3, 4, 5)
	
	def test_bagset_init_returns_type_error_with_limits_not_list(self):
		
		self.assertRaises(TypeError, self.bagset, {'a':0}, 4, 5)
		
	def test_bagset_init_returns_type_error_with_size_not_dict(self):
		
		self.assertRaises(TypeError, self.bagset, {'a':0}, [0,1,2], 2)
		
	def test_bagset_init_returns_value_error_with_unmatched_dict_keys(self):
		
		self.assertRaises(ValueError, self.bagset, {'a':0, 'c':2}, [[0,1,2]], {'b':1, 'a':0})
		
	def test_bagset_init_returns_value_error_with_unequal_limits_size_key_length(self):
	
		self.assertRaises(ValueError, self.bagset, {'a':0, 'c':2}, [[0,1,2]], {'c':1, 'a':0})
		
	def test_bagset_init_returns_type_error_with_nonarraytype_inner_limits(self):
		
		self.assertRaises(TypeError, self.bagset, {'a':0, 'c':2}, [0,1,2], {'b':1, 'a':0})
		
		
if __name__ == '__main__':
	unittest.main()