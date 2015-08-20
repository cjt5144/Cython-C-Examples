#!/usr/bin/python
# (c) 2015 Christopher Thompson
# license: https://github.com/cjt5144/Cython-Cpp-Examples/blob/master/LICENSE


import unittest
import pandas
import knapsack
import knapset
import pank


items = (
		("map", 9, 150), ("compass", 13, 35), 
		("water", 153, 200), ("sandwich", 50, 160),
		("glucose", 15, 60), ("tin", 68, 45), 
		("banana", 27, 60), ("apple", 39, 40),
		("cheese", 23, 30), ("beer", 52, 10), 
		("suntan cream", 11, 70), ("camera", 32, 30),
		("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
		("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
		("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
		("socks", 4, 50), ("book", 30, 10),
		)


outputItemsUnlimited = ('banana', 'compass', 'glucose', 'map', 'note-case', 
						'sandwich', 'socks', 'sunglasses', 'suntan cream', 
						'water', 'waterproof overclothes', 
						'waterproof trousers')


centerTuples = (
				('DeAndre Jordan', 8900, 32.356756000000004),
				('Marc Gasol', 7900, 33.273391000000004),
				('Dwight Howard', 7900, 0.0),
				('Hassan Whiteside', 7800, 43.643265)
 				)
 				

################################################################################
#							KNAPSACK01 TEST
################################################################################


class Knapsack01InputTest(unittest.TestCase):

	
	def test_TypeError_with_non_tuple_items(self):
	
		self.assertRaises(TypeError, knapsack.knapsack01, [1 ,2, 3], 2, 6)
	
	def test_TypeError_with_non_tuple_inner_items(self):
	
		self.assertRaises(TypeError, knapsack.knapsack01, 
									(1,2,3), 2, 6)
									
	def test_ValueError_with_inner_tuple_not_length_3(self):
	
		self.assertRaises(ValueError, knapsack.knapsack01, 
									((1,2), (1,2,3)), 2, 6)
	
	def test_TypeError_with_limit_not_int(self):
	
		self.assertRaises(TypeError, knapsack.knapsack01,
									((1,2,3),(3,4,5)), 'a', 6)
									
	def test_TypeError_with_size_not_int_or_None(self):
		
		self.assertRaises(TypeError, knapsack.knapsack01,
									((1,2,3),(3,4,5)),  4, '6')


class Knapsack01TestWithLimit400(unittest.TestCase):


	def setUp(self):
	
		self.result = knapsack.knapsack01(items, 400)
		
	def test_total_value_of_items_equals_1030_with_limit_400(self):
	
		_, totalval, _, _ = self.result
		self.assertEqual(1030, totalval)
		
	def test_total_weight_of_items_equals_396_with_limit_400(self):
	
		_, _, totalwt, _ = self.result
		self.assertEqual(396, totalwt)
		
	def test_items_equal_outputItemsUnlimited(self):
		
		items,_,_, _ = self.result
		self.assertTrue(items==outputItemsUnlimited)
		

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
	

################################################################################
#						END KNAPSACK01 TEST
################################################################################

################################################################################
#							KNAPSET TEST
################################################################################


class KnapSetInitializationTest(unittest.TestCase):
	
	
	def setUp(self):
		
		self.sack	= knapset.KnapSet
		
	def test_TypeError_with_items_not_dict(self):
	
		self.assertRaises(TypeError, self.sack, 3, 4, 5)
	
	def test_TypeError_with_limits_not_list(self):
		
		self.assertRaises(TypeError, self.sack, {'a':0}, 4, 5)
		
	def test_TypeError_with_size_not_dict(self):
		
		self.assertRaises(TypeError, self.sack, {'a':0}, [0,1,2], 2)
		
	def test_ValueError_with_unmatched_dict_keys(self):
		
		self.assertRaises(ValueError, self.sack, {'a':0, 'c':2},
		[[0,1,2]], {'b':1, 'a':0})
		
	def test_ValueError_with_unequal_limits_size_key_length(self):
	
		self.assertRaises(ValueError, self.sack, {'a':0, 'c':2},
		[[0,1,2]], {'c':1, 'a':0})
		
	def test_TypeError_with_nonarraytype_inner_limits(self):
		
		self.assertRaises(TypeError, self.sack, {'a':0, 'c':2},
		[0,1,2], {'b':1, 'a':0})


class KnapSetWithMultipleItems(unittest.TestCase):
	
		
	def testMultiKnapsackOutputCorrectWithUnfilledTrue(self):
		
		itemDict = {}
		itemDict['A'] = items
		itemDict['B'] = items
		limits = [[400, 100]]
		sizes = {'A':None, 'B':2}
		
		ss = knapset.KnapSet(itemDict, limits, sizes)
		result = ss.knapsack01(keepUnfilled=True)
		self.assertEqual(result[0][1], 455)
		self.assertEqual(result[0][2], 1340)
		
	def testMultiKnapWithMoreTypesInItemDict(self):
		
		itemDict = {}
		itemDict['A'] = items
		itemDict['B'] = items
		itemDict['C'] = items
		limits = [[400, 100]]
		sizes = {'A':None, 'B':2}
		
		ss = knapset.KnapSet(itemDict, limits, sizes)
		result = ss.knapsack01(keepUnfilled=True)
		self.assertEqual(result[0][1], 455)
		self.assertEqual(result[0][2], 1340)
		
	def testMultiKnapsackLimitsWithUnfilledTrue(self):
		
		itemDict = {}
		itemDict['A'] = items
		itemDict['B'] = items
		limits = [[400, 100],[400, 100]]
		sizes = {'A':None, 'B':2}
		
		ss = knapset.KnapSet(itemDict, limits, sizes)
		result = ss.knapsack01(keepUnfilled=True)
		self.assertEqual(result[0][1], 455)
		self.assertEqual(result[1][2], 1340)

	def testMultiKnapsackOutputCorrect(self):
		
		itemDict = {}
		itemDict['A'] = items
		itemDict['B'] = items
		limits = [[400, 100]]
		sizes = {'A':None, 'B':2}
		
		ss = knapset.KnapSet(itemDict, limits, sizes)
		result = ss.knapsack01()
		self.assertEqual(result[0][1], 455)
		self.assertEqual(result[0][2], 1340)
		
	def testMultiKnapsackLimitsWithDifferentLimits(self):
		
		itemDict = {}
		itemDict['A'] = items
		itemDict['B'] = items
		limits = [[400, 100],[400, 50]]
		sizes = {'A':None, 'B':2}
		
		ss = knapset.KnapSet(itemDict, limits, sizes)
		result = ss.knapsack01()
		self.assertEqual(result[0][1], 455)
		self.assertEqual(result[1][2], 1260)
		
		
################################################################################
#						END KNAPSET TEST
################################################################################

################################################################################
#							PANK TEST
################################################################################


class PankInitTest(unittest.TestCase):

		
	def testTypeErrorWithNonDataFrameInput(self):
		
		fpank = pank.pank
		self.assertRaises(TypeError, fpank, 2)
				
	def testValueErrorWithProperColumnsNotIncluded(self):
	
		baddata = pandas.read_csv("data/baddata.csv")
		fpank = pank.pank
		self.assertRaises(ValueError, fpank, baddata)
		

class PankOutputTest(unittest.TestCase):

	
	def setUp(self):
	
		gooddata = pandas.read_csv("data/gooddata.csv")
		self.out = pank.pank(gooddata)
		
	def testOutputIsDict(self):
		
		test = isinstance(self.out, dict)
		self.assertTrue(test)
	
	def testOutputIsDictOfTuples(self):
	
		tests = [isinstance(self.out[key], tuple) for key in self.out]
		self.assertTrue(all(tests))
	

################################################################################
#						END PANK TEST
################################################################################


if __name__ == '__main__':
	
	unittest.main()
