#!/usr/bin/python
# (c) 2015 Christopher Thompson
# license: https://github.com/cjt5144/Cython-Cpp-Examples/blob/master/LICENSE

import types
import knapsack


class Bag:
	""" Bag class used to wrap knapsack01 functions
	
	Attributes:
		items tuple of tuples of item in the form (id, weight, value)
		limit int limit of bag
		size=None int describes how many items to fit. If None, bag is filled
						until limit is reached.
	
	Methods:
		knapsack01 see knapsack.knapsack01 for docstring
		sknapsack01 see knapsack.sknapsack01 for docstring
	"""
	
	
	def __init__(self, items, limit, size=None):
	
		if isinstance(items, tuple):
			if all([isinstance(item, tuple) for item in items]):
				if all([len(item) == 3 for item in items]):
					self.items = items
				else:
					raise ValueError('[-] ValueError inner items must be of length 3\n')
			else:
				raise ValueError('[-] ValueError inner item objects must be tuples\n')
		else:
			raise ValueError('[-] ValueError items must be tuple of tuples\n')
		
		if isinstance(limit, int):
			self.limit = limit
		else:
			raise ValueError('[-] ValueError limit must be int\n')
			
		if isinstance(size, int) or isinstance(size, types.NoneType):
			self.size = size
		else:
			raise ValueError('[-] ValueError size must be int or None\n')
			
	def knapsack01(self):
	
		return knapsack.knapsack01(self.items, self.limit, self.size)
		
# 	def sknapsack01(self):
# 	
# 		return knapsack.sknapsack01(self.items, self.limit, self.size)