#!/usr/bin/python
# (c) 2015 Christopher Thompson
# license: https://github.com/cjt5144/Cython-Cpp-Examples/blob/master/LICENSE

import knapsack as knp
import numpy as np


_arraytypes = (np.ndarray, list, tuple)


def _knapSetInitInputCheck(items, limits, sizes):
	""" 
	Input Check For KnapSet Init
	"""
	
	if not isinstance(items, dict):
		raise TypeError("[-] 'items' must be of type dict")
		
	if not isinstance(limits, _arraytypes):
		raise TypeError("\n[-] 'limit' must be list, ",
		"np.ndarray, or tuple\n")
			
	if not all([
				isinstance(limits[i], _arraytypes) for i in xrange(len(limits))
				]):
		
		raise TypeError("\n[-] inner 'limit' objects must be arraytype\n")
		
	if not isinstance(sizes, dict):
		raise TypeError("\n[-] 'size' must be dict\n")
		
	if not set(items.keys()) >= set(sizes.keys()):
			raise ValueError("\n[-] 'items' keys must contain 'sizes' keys\n")
	
	if not all([len(limits[i]) == len(sizes.keys()) 
		for i in xrange(len(limits))]):
			raise ValueError("\n[-] 'items' and 'sizes' must be same length\n")	
			
	
class KnapSet:
	"""
	KnapSet(items, limits, sizes)
	
	Class creates an optimized set of knapsacks 
	for different input groups with different input
	limits but the same input size.
	
	Parameters:
	-----------
	items : dict of tuples of tuples in the form:
		(string : id, int : wt, float: val)
	limits : 2d list of _arraytype
		column index corresponds to sorted sizes dict keys
	sizes : dict of ints
		sizes for each group
		
	Attributes:
	-----------
	knapsack01 : list of tuples in the form:
		(tuple items, total weight, total value, isSetfull)
		Creates optimized sets using knapsack01
	"""
	
	
	def __init__(self, items, limits, sizes):
		
		_knapSetInitInputCheck(items, limits, sizes)
		
		self.items = items
		self.limits = limits
		self.sizes = sizes
		
	def knapsack01(self, keepUnfilled=False):
		"""
		KnapSet knapsack01
		
		Run knapsack01 on different types to get a
		collection of optimized item list.
		
		Given a 2d list of limits, where each
		row corresponds to a set of limits,
		run knapsack01 on each limit item.
		Collect sets (rows) of optimized items
		with the set total value and weight.
		The sets' isSingleSetFull property
		is set to True only if all set items
		are filled to their capacity as determined
		by knapsack01.
		The user has the option of keeping only 
		full set.
		
		Args:
		-----
		keepUnfilled : bool
			if a group returns a unfilled knapsack, 
			should it be kept?
			
		Returns:
		--------
		knapset : list of tuples in the form:
			(items, totwt, totval, isSetFull)
			
			items : tuple
				string tuple ids
			totwt : int
				total weight
			totval : float
				total value
			isSetFull : bool
				is set full
		"""
		
		# Unpack variables
		itm = self.items
		lmt = self.limits
		sz = self.sizes
		knapset = []
		
		# All lineup limits
		for i in xrange(len(lmt)):
			ids = []
			totwt = 0
			totval = 0
			isSingleSetFull = True
			
			# All types in size keys
			for j in xrange(len(sz.keys())):
				type = sorted(sz.keys())[j]
				typeKnap = knp.knapsack01(itm[type], lmt[i][j], sz[type])
				
				# Unpack isFilled
				filled = typeKnap[3]
				if filled==False and keepUnfilled==False:
					isSingleKnapFull = False
					break
					
				# Unpack typeKnap
				items = typeKnap[0]
				val = typeKnap[1]
				wt = typeKnap[2]
				
				# Add up knapsack items and attributes
				ids.extend(items)
				totwt = totwt + wt
				totval = totval + val
					
			if keepUnfilled == False and isSingleSetFull == False:
				pass
			else:
				oneset = (ids, totwt, totval, isSingleSetFull)
				knapset.append(oneset)
		
		if not knapset:
			print "\n[-] Warning : Returning empty KnapSet Object\n"
		else:
			print "\n[+] KnapSet finished creating optimized set...\n"
			
		return knapset
