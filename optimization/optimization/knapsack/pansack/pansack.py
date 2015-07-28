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
				
		self.data = df
		self.typeTupTup = {}
		self.subsetData = DataFrame()
	
	def getColumnsWithName(self, id, wt, val, type):
		""" Get Columns With Name in df
		
		Subset df with the columns corresponding to the input strings.
		Renames the columns to input variable strings.
		
		Args:
			id, wt, val, type str column names to subset
		Return:
			None
		"""
		
		strArgs = (id, wt, val, type)
		isStrArg = [isinstance(arg, str) for arg in strArgs]
		
		if not all(isStrArg):
		
			isStrArg = np.array(isStrArg)
			notStrList = isStrArg[isStrArg == False]
			raise TypeError("\n[-] TypeError: '" + str(notStrList) + 
								"' must be a str\n")
		
		subsetData = self.data[[id, wt, val, type]]
		subsetData.columns = ["id", "wt", "val", "type"]
		
		self.subsetData = subsetData
		
	def typeGroupsToTupTupDict(self):
		""" Type Group to Dict of Tuples
		
		Group the type variable into a dict of tuples of the form (id, wt, val).
		
		Args:
			None
		Returns:
			None
		"""
		
		if self.subsetData.values.tolist() == []:
			
			raise ValueError("\n[-] ValueError: subsetData is empty.\n" \
			"Use getColumnsWithName to fill subsetData\n")
		
		subsetNoType = self.subsetData[['id', 'wt', 'val']]
		typeGroups = subsetNoType.groupby(self.subsetData["type"])
		dictFrame = dict(list(typeGroups))
		
		for name, group in dictFrame.iteritems():
			
			self.typeTupTup[name] = frameToTupTup(group)
		
	
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
	
	try:
	
		tupTup = tuple([tuple(x) for x in df.values])
		return tupTup
		
	except Exception, e:
	
		print "\n[-] Error in frameToTupTup = " + str(e) + "\n"