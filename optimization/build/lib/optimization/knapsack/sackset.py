#!/usr/bin/python
# (c) 2015 Christopher Thompson
# license: https://github.com/cjt5144/Cython-Cpp-Examples/blob/master/LICENSE

import knapsack
import numpy as np

_arraytypes = (np.ndarray, list, tuple)

def _sackSetInitInputCheck(items, limits, sizes):
	""" Private Input Check For SackSet Init
	"""

	if not isinstance(items, dict):
		raise TypeError("[-] TypeError: 'items' must be of type dict")
		
	if not isinstance(limits, _arraytypes):
		raise TypeError("[-] TypeError: 'limit' must be list," \
			" np.ndarray, or tuple")
			
	if not all([
				isinstance(limits[i], _arraytypes) for i in xrange(len(limits))
				]):
		
		raise TypeError("[-] TypeError: inner 'limit' objects" \
		" must be arraytype")
		
	if not isinstance(sizes, dict):
		raise TypeError("[-] TypeError: 'size' must be dict")
		
	if sorted(items.keys()) != sorted(sizes.keys()):
			raise ValueError("[-] ValueError: 'items' and 'sizes'" \
			" must have the same keys")
	
	if not all([len(limits[i]) == len(sizes.keys()) 
			for i in xrange(len(limits))]):
		
			raise ValueError("[-] ValueError: 'items' and 'sizes'" \
			" must be same length")	
			
	
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
		
		_sackSetInitInputCheck(items, limits, sizes)
		
		self.items = items
		self.limits = limits
		self.sizes = sizes
		
	def knapsack01(self, keepUnfilled=False):
		""" knapsack01
		
		Run knapsack01 on different types to get a collection of optimized
		item list.
		For all sack limits, setup the single bag optimized for all types.
		For each type in sizes, retrieve key
			Run knapsack01 for key add stats from knapsack to single bag
		If inner j keepUnfilled and isSingleBagFull False
			break out of inner j and move to next limit set after add items
			to sackset.
		
		Args:
			keepUnfilled bool if a group returns a unfilled knapsack, should it
			be kept?
		Returns:
			sackset list of group tuple items, total weight, total value, 
			whether all the knapsack are full
			list of tuples with items (tuple), totwt (int), totval (number), 
			isFull (bool)
		"""
		
		sackset = []
		
		for i in xrange(len(self.limits)):
			ids = []
			wt = 0
			val = 0
			isSingleBagFull = True
			
			for j in xrange(len(self.sizes.keys())):
			
				itemTypeKey = sorted(self.sizes.keys())[j]
				typeBag = knapsack.knapsack01(self.items[itemTypeKey],
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
