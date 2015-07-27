#!/usr/bin/python
# (c) 2015 Christopher Thompson
# license: https://github.com/cjt5144/Cython-Cpp-Examples/blob/master/LICENSE

import knapsack
import numpy as np

_arraytypes = (np.ndarray, list, tuple)

class SackSet:
	""" SackSet
	
	Class creates an optimized set of knapsacks for different input groups with
	different input limits but the same input size
	
	Member Variables:
		items dict of tuples containing items in the form (id, wt, val)
		limits arraytype int index corresponds to sorted items dict keys
		sizes dict sizes for each group
	"""

	def __init__(self, items, limits, sizes):
		
		if isinstance(items, dict):
		
			self.items = items
		else:
		
			raise TypeError("[-] TypeError: 'items' must be of type dict")
			
		if isinstance(limits, _arraytypes):
		
			self.limits = limits
		else:
		
			raise TypeError("[-] TypeError: 'limit' must be list," \
			" np.ndarray, or tuple")
			
		if not all([isinstance(limits[i], _arraytypes) 
			for i in xrange(len(limits))]):
		
			raise TypeError("[-] TypeError: inner 'limit' objects" \
			" must be arraytype")
			
		if isinstance(sizes, dict):
		
			self.sizes = sizes
		else:
		
			raise TypeError("[-] TypeError: 'size' must be dict")
		
		if sorted(items.keys()) != sorted(sizes.keys()):
		
			raise ValueError("[-] ValueError: 'items' and 'sizes'" \
			" must have the same keys")
		
		if not all([len(limits[i]) == len(sizes.keys()) 
			for i in xrange(len(limits))]):
			
			raise ValueError("[-] ValueError: 'items' and 'sizes'" \
			" must be same length")	
	
	def knapsack01(self, keepUnfilled=False):
		""" knapsack01
		
		Run knapsack01 on different types to get a collection of optimized
		item list
		
		Args:
			keepUnfilled bool if a group returns a unfilled knapsack, should it
			be kept?
		Returns:
			sackset tuple of group items, total weight, total value, whether
				all the knapsack are full
		"""
		
		sackset = []
		
		for i in xrange(len(self.limits)):
			
			ids = []
			wt = 0
			val = 0
			isSingleBagFull = True
			
			for j in xrange(len(self.sizes.keys())):
			
				itemTypeKey = sorted(self.sizes.keys())[j]
				
				typeBag = knapsack.knapsack(self.items[itemTypeKey],
							self.limits[i][j],
							self.sizes[itemTypeKey])
				
				ids.extend(typeBag[0])
				wt = wt + typeBag[2]
				val = val + typeBag[1]
				isSingleBagFull = False if typeBag[3] == False else True
				
				if keepUnfilled == False and isSingleBagFull == False:
					
					break
					
			if keepUnfilled == False and isSingleBagFull == False:
				
				pass
				
			else:
				
				sack = (ids, wt, val, isSingleBagFull)
				sackset.append(sack)

		return sackset
