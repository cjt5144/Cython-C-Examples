#!/usr/bin/python
# (c) 2015 Christopher Thompson
# license: https://github.com/cjt5144/Cython-Cpp-Examples/blob/master/LICENSE

import numpy as np
import pandas as pd

		
def pank(df):
	""" 
	Convert type groups to dict of tuples.
	
	Args:
	-----
	df : DataFrame
		Must contain columns ['id', 'wt', 'val', 'type']
	
	Returns:
	--------
	itemsByType : dict of tuples
		Each dict key is a group name created by
		using groupby on df.
		The tuple is in the form output by
		frameToTupTup(DataFrame : df).
	"""
	
	itemsByType = {}
	
	if not isinstance(df, pd.DataFrame):
		raise TypeError("\n[-] 'df' must be a pandas.DataFrame\n")
			
	columnNames = df.columns.tolist()
	mustIncludeColumns = ['id', 'wt', 'val', 'type']
	if not set(columnNames) >= set(mustIncludeColumns):
		raise ValueError("\n[-] 'df' columns must include ",
		"'id', 'wt', 'val', 'type'\n")
		
	subsetNoType = df[['id', 'wt', 'val']]
	typeGroups = subsetNoType.groupby(df["type"])
	dictFrame = dict(list(typeGroups))
	
	for name, group in dictFrame.iteritems():
		itemsByType[name] = frameToTupTup(group)
		
	if not itemsByType:
		print "\n[-] Warning : pank 'itemsByType' is empty\n"
	else:
		print "\n[+] pank finished generating itemsByType...\n"
		
	return itemsByType
			
	
def frameToTupTup(df):
	""" 
	Convert pandas DataFrame rows to a tuple
	of tuples with the index of the inner tuple
	corresponding to the row it came from.
	
	Args:
	-----
	df : DataFrame
		input data
		
	Returns:
	--------
	tupTup : tuple of tuples in the form:
		(([0][1],[0][2],...,[0][n]),([1][1],[1][2],...,[1][n]),...)
		where the indices are [row][col]
	"""
	
	if not isinstance(df, pd.DataFrame):
		
		raise TypeError("\n[-] 'df' must be a DataFrame\n")
	
	tupTup = tuple([tuple(x) for x in df.values])
	return tupTup
