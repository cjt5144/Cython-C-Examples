#!/usr/bin/python
# (c) 2015 Christopher Thompson
# license: https://github.com/cjt5144/Cython-Cpp-Examples/blob/master/LICENSE

import numpy as np
from pandas import DataFrame
import pandas as pd


class Pans:
	""" Pans
	
	Pans class provides a interface between the pandas DataFrame object and the 
	knapsac.pyknap SackSet object. The typeTupTup member variable would be the 
	input into the SackSet items variable.
	
	Member Variables:
		df DataFrame input data frame
		typeTupTup dict of tuples in the form (id, wt, val)
		subsetData DataFrame subset of df containing proper column names
	"""
	
	
	def __init__(self, df):
		
		if not isinstance(df, DataFrame):
			
			raise TypeError("\n[-] TypeError: 'df' must be a" \
				" pandas.DataFrame\n")
				
		columnNames = df.columns.tolist()
		mustIncludeColumns = ['id', 'wt', 'val', 'type']
		
		if not set(mustIncludeColumns) <= set(columnNames):
			
			raise ValueError("\n[-] ValueError: 'df' must include columns"\
				"'id', 'wt', 'val', 'type'\n")
		
		self.data = df
		self._typeTupTup = {}
		
	def typeGroupsToTupTupDict(self):
		""" Type Group to Dict of Tuples
		
		Group the type variable into a dict of tuples of the form (id, wt, val).
		
		Args:
			None
		Returns:
			None
		"""
		
		subsetNoType = self.data[['id', 'wt', 'val']]
		typeGroups = subsetNoType.groupby(self.data["type"])
		dictFrame = dict(list(typeGroups))
		
		for name, group in dictFrame.iteritems():
			
			self._typeTupTup[name] = frameToTupTup(group)
			
	
def frameToTupTup(df):
	""" DataFrame to Tuple of Tuples
	
	Turns data frame df into tuple of tuples.
	
	Args:
		df DataFrame input data
	Returns:
		tuple of tuples
	"""
	
	if not isinstance(df, DataFrame):
		
		raise TypeError("\n[-] TypeError: 'df' must be a DataFrame\n")
	
	tupTup = tuple([tuple(x) for x in df.values])
	return tupTup
