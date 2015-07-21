#!/usr/bin/python
# (c) 2015 Christopher Thompson
# license: https://github.com/cjt5144/Cython-Cpp-Examples/blob/master/LICENSE

import knapsack
import numpy as np

arraytypes = (np.ndarray, list, tuple)

class BagSet:


	def __init__(self, items, limits, sizes):
		
		if isinstance(items, dict):
			self.items = items
		else:
			raise TypeError("[-] TypeError: 'items' must be of type dict")
			
		if isinstance(limits, arraytypes):
			self.limits = limits
		else:
			raise TypeError("[-] TypeError: 'limit' must be list, np.ndarray, or tuple")
			
		if not all([isinstance(limits[i], arraytypes) for i in xrange(len(limits))]):
			raise TypeError("[-] TypeError: inner 'limit' objects must be arraytype")
			
		if isinstance(sizes, dict):
			self.sizes = sizes
		else:
			raise TypeError("[-] TypeError: 'size' must be dict")
		
		if sorted(items.keys()) != sorted(sizes.keys()):
			raise ValueError("[-] ValueError: 'items' and 'sizes' must have the same keys")
		
		if not all([len(limits[i]) == len(sizes.keys()) for i in xrange(len(limits))]):
			raise ValueError("[-] ValueError: 'items' and 'sizes' must be same length")	
	
	def knapsack01(self, keepUnfilled=False):
		
		bagsets = []
		
		for i in xrange(len(self.limits)):
			
			ids = []
			wt = 0
			val = 0
			isSingleBagFull = True
			
			for j in xrange(len(self.sizes.keys())):
			
				itemTypeKey = sorted(self.sizes.keys())[j]
				
				typeBag = knapsack.knapsack(self.items[itemTypeKey],
													self.limits[i][j],
													self.sizes[itemTypeKey]
											)
				
				ids.extend(typeBag[0])
				wt = wt + typeBag[2]
				val = val + typeBag[1]
				isSingleBagFull = False if typeBag[3] == False else True
				
				if keepUnfilled == False and isSingleBagFull == False:
					
					break
					
			if keepUnfilled == False and isSingleBagFull == False:
				
				pass
				
			else:
				
				bagset = (ids, wt, val, isSingleBagFull)
				bagsets.append(bagset)

		return bagsets
