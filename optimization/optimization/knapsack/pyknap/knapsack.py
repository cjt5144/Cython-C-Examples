#!/usr/bin/python
# (c) 2015 Christopher Thompson
# license: https://github.com/cjt5144/Cython-Cpp-Examples/blob/master/LICENSE

from numpy import ndarray
import types

def _xrangeImport():
	""" Import Xrange as xrange or range depending on availability
	
	Args:
		None
	Returns:
		xrange function xrange or range 
	"""
	
	try:
	
		return xrange
		
	except:
	
		xrange = range
		return xrange

def _totalValue(comb):
	""" Total a particular combination of items
	
	Args:
		comb tuple of items in the form (item, weight, value)
	Returns:
		tuple (total value, total weight)
	"""
	
	totwt = totval = 0
	
	for item, wt, val in comb:
	
		totwt  += wt
		totval += val
		
	return (totval, totwt)
	
def _itemNames(comb):
	""" Item names from result of knapsack01
	
	Args:
		comb tuple of tuples result of knapsack01
	Returns:
		tuple sorted item ids
	"""
	
	return tuple(sorted(item for item,_,_ in comb))

def _findItems(table, items, currentitem, currentwt, size=None):
	""" Find Items in Optimized Set
	
	Args:
		table 2/3 - dimensional array of knapsack numbers
		items tuple of tuples containing items of the form (id, wt, val)
		currentItem int last item number added to knapsack01
		currentwt int the current weight of knapsack01 algorithm
		size default(None) int size limit of knapsack
	Returns:
		tuple of tuples of form (id, wt, val)
	"""
	
	result = []
	w = currentwt
	
	for i in xrange(len(items), 0, -1):
	
		if size != None:
		
			was_added = table[size][i][w] != table[size][i-1][w]
		else:
		
			was_added = table[0][i][w] != table[0][i-1][w]
			
		if was_added:
		
			item, wt, val = items[i-1]
			result.append(items[i-1])
			w -= wt
			
			if size != None:
			
				size -= 1
			
	return result

def _wtCheck(table, wt, val, k, j, w):
	""" Weight Check
	
	Private knapsack01 member function
	Check the weight versus the index for _jkTableRun
	Returns nothing
	"""
	
	if wt > w:
	
		table[k][j][w] = table[k][j-1][w]
		
	else:
	
		table[k][j][w] = max(table[k][j-1][w],
							table[k-1][j-1][w-wt] + val)

def _jkTableRun(table, items, limit, k):
	""" j-k Table Run
	
	Private knapsack01 member function
	Run the core body of knapsack algorithm
	Returns nothing
	"""
	
	for j in xrange(1, len(items) + 1):
	
		item, wt, val = items[j-1]
		
		if j > k:
		
			for w in xrange(1, limit + 1):

				_wtCheck(table, wt, val, k, j, w)
				
		else:
		
			for w in xrange(1, limit + 1):

				_wtCheck(table, wt, val, k, j, w)
											
	return table

def _knapsackInputCheck(items, limit, size_in):
	""" Knapsack Input Check
	
	Private knapsack member function
	Error checks the input variables for the knapsack01 function
	Returns nothing
	"""

	if not isinstance(items, tuple):
		
		raise TypeError('[-] TypeError items must be tuple of tuples\n')

	if not all([isinstance(item, tuple) for item in items]):
	
		raise TypeError('[-] TypeError inner item objects must be tuples\n')
		
	if not all([len(item) == 3 for item in items]):
	
		raise ValueError('[-] ValueError inner items must be of length 3\n')

	if not isinstance(limit, int):
	
		raise TypeError('[-] TypeError limit must be int\n')
		
	sizeCheck = (isinstance(size_in, int), isinstance(size_in, types.NoneType))
	
	if not any(sizeCheck):
		
		raise TypeError('[-] TypeError size must be int or None\n')

def knapsack01(items, limit, size_in=None):
	""" Knapsack 01 Algorithm with Maximum Item Number
	Code modified from: http://rosettacode.org/wiki/Knapsack_problem/0-1#Python
	
	Args:
		items tuple of tuples of the form (id, wt, val)
		limit int limit of knapsack weight
		size_in int or None maximum size of the knapsack
	Returns:
		tuple of form (item ids, total value, total weight, 
			is filled to maximum size)
	"""
	
	_knapsackInputCheck(items, limit, size_in)	
			
	if size_in != None:
	
		size = size_in
		
	else:
	
		size = 0
		
	xrange = _xrangeImport()
	table = [[[0 for w in xrange(limit + 1)] 
					for j in xrange(len(items) + 1)] 
					for k in xrange(size + 1)]
	
	if size_in != None:
	
		for k in xrange(1, size + 1):
		
			_jkTableRun(table, items, limit, k)
	
	else:
		
		k = 0
		_jkTableRun(table, items, limit, k)
		
	if size_in != None:
	
		result = _findItems(table, items, j, w, size)
		isFilled = True if len(result) == size else False
	
	else:
	
		result = _findItems(table, items, j, w)
	
	knapItems = _itemNames(result)
	totval, totwt = _totalValue(result)
	
	if size_in != None:
	
		return (knapItems, totval, totwt, isFilled)
		
	else:
	
		return (knapItems, totval, totwt)
