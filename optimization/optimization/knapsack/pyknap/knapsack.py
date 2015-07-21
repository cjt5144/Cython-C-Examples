#!/usr/bin/python
# (c) 2015 Christopher Thompson
# license: https://github.com/cjt5144/Cython-Cpp-Examples/blob/master/LICENSE

def xrangeImport():
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

def findItems(table, items, currentitem, currentwt, size=None):
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
			was_added = table[i][w] != table[i-1][w]
			
		if was_added:
			item, wt, val = items[i-1]
			result.append(items[i-1])
			w -= wt
			if size != None:
				size -= 1
			
	return result

def totalValue(comb):
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
	
def itemNames(comb):
	""" Item names from result of knapsack01
	
	Args:
		comb tuple of tuples result of knapsack01
	Returns:
		tuple sorted item ids
	"""
	
	return tuple(sorted(item for item,_,_ in comb))
	
# def knapsack01(items, limit):
# 	""" Knapsack 01 Algorithm modified from 
# 	http://rosettacode.org/wiki/Knapsack_problem/0-1#Python
# 	source code
# 	
# 	Args:
# 		items tuple of tuples of the form (id, wt, val)
# 		limit int limit of knapsack weight
# 	Returns:
# 		tuple of form (item ids, total value, total weight)
# 	"""
# 
# 	xrange = xrangeImport()
# 	
# 	table = [[0 for w in xrange(limit + 1)] for j in xrange(len(items) + 1)]
# 
# 	for j in xrange(1, len(items) + 1):
# 		item, wt, val = items[j-1]
# 		for w in xrange(1, limit + 1):
# 			if wt > w:
# 				table[j][w] = table[j-1][w]
# 			else:
# 				table[j][w] = max(table[j-1][w],
# 									table[j-1][w-wt] + val)
# 	
# 	result = findItems(table, items, j, w)
# 	knapItems = itemNames(result)
# 	totval, totwt = totalValue(result)
# 	return (knapItems, totval, totwt)
	
def knapsack01(items, limit, size_in=None):
	""" Knapsack 01 Algorithm with Maximum Item Number
	Code modified from: http://rosettacode.org/wiki/Knapsack_problem/0-1#Python
	
	Args:
		items tuple of tuples of the form (id, wt, val)
		limit int limit of knapsack weight
	Returns:
		tuple of form (item ids, total value, total weight, is filled to maximum size)
	"""
	
# 	if size_in != None:
# 		size = size_in
		
	xrange = xrangeImport()
	
# 	table = [[[0 for w in xrange(limit + 1)] for j in xrange(len(items) + 1)] 
# 																for k in xrange(size + 1)]
	
	if size_in == None:
		table = [[0 for w in xrange(limit + 1)] for j in xrange(len(items) + 1)]

		for j in xrange(1, len(items) + 1):
			item, wt, val = items[j-1]
			for w in xrange(1, limit + 1):
				if wt > w:
					table[j][w] = table[j-1][w]
				else:
					table[j][w] = max(table[j-1][w],
										table[j-1][w-wt] + val)
									
		result = findItems(table, items, j, w)
			
	else:
		
		size = size_in
		
		table = [[[0 for w in xrange(limit + 1)] for j in xrange(len(items) + 1)] 
																for k in xrange(size + 1)]
		
		for k in xrange(1, size + 1):
			for j in xrange(1, len(items) + 1):
				item, wt, val = items[j-1]
				if j > k:
					for w in xrange(1, limit + 1):
						if wt > w:
							table[k][j][w] = table[k][j-1][w]
						else:
							table[k][j][w] = max(table[k][j-1][w],
													table[k-1][j-1][w-wt] + val)
				else:
					for w in xrange(1, limit + 1):
						if wt > w:
							table[k][j][w] = table[k][j-1][w]
						else:
							table[k][j][w] = max(table[k][j-1][w],
													table[k][j-1][w-wt] + val)
												
		result = findItems(table, items, j, w, size)
		isFilled = True if len(result) == size else False
		
		
# 	if size_in == None:
# 		result = findItems(table, items, j, w)
# 	else:
# 		result = findItems(table, items, j, w, size)
# 		isFilled = True if len(result) == size else False
	
	knapItems = itemNames(result)
	totval, totwt = totalValue(result)
	
	if size_in == None:
		return (knapItems, totval, totwt)
	else:
		return (knapItems, totval, totwt, isFilled)