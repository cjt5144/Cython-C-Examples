import numpy as np
import pansack as ps
from pandas import Series, DataFrame
import pandas as pd
import unittest


centerTuples = (
				('DeAndre Jordan', 8900, 32.356756000000004),
				('Marc Gasol', 7900, 33.273391000000004),
				('Dwight Howard', 7900, 0.0),
				('Hassan Whiteside', 7800, 43.643265)
 				)

try:

	data = pd.read_csv("data/022315_projectedplayers.csv")[:25]
	
except IOError:
	
	print "\n[-] IOError: Failure opening 'data/022315_projectedplayers.csv'\n"


class PansInitTest(unittest.TestCase):


	def test_TypeError_with_non_DataFrame_input(self):
			
		self.assertRaises(TypeError, ps.Pans, 2)
		self.assertRaises(TypeError, ps.Pans, 'hasjfdhajkf')
		self.assertRaises(TypeError, ps.Pans, [1,2,3,4])
		self.assertRaises(TypeError, ps.Pans, Series([1,2,3,4]))
		

class PansGetColumnsWithNameTest(unittest.TestCase):

	
	def setUp(self):
		
		self.pans = ps.Pans(data)
		self.harden = np.array(['James Harden', 10600, 
		47.175783, "SG"], dtype=object)
	
	def test_TypeError_getColumnsWithName_non_str_inputs(self):
	
		self.assertRaises(TypeError, self.pans.getColumnsWithName,
			1, 2, 3, 4)
		self.assertRaises(TypeError, self.pans.getColumnsWithName,
			1, '2', '3', '4')
	
	def test_harden_equals_first_row(self):
		
		self.pans.getColumnsWithName("name","sal","ppg","pos")
		test = self.harden == self.pans.subsetData.ix[0].values
		self.assertTrue(np.all(test))
	
	
class FrameToTupTupTest(unittest.TestCase):

	
	def setUp(self):
	
		self.pans = ps.Pans(data)
		self.pans.getColumnsWithName("name","sal","ppg","pos")
		subsetNoType = self.pans.subsetData[['id', 'wt', 'val']]
		groups = subsetNoType.groupby(self.pans.subsetData["type"])
		self.dictFrame = dict(list(groups))
		self.output = tuple([tuple(x) for x in self.dictFrame['C'].values])
		
	def test_centerTuple_equal_output(self):

		test = centerTuples == self.output
		self.assertTrue(test)
		
	
class PansTypeGroupsToTupTupDictTest(unittest.TestCase):

	
	def setUp(self):
	
		self.pans = ps.Pans(data)
		self.pans.getColumnsWithName("name","sal","ppg","pos")
		self.pans.typeGroupsToTupTupDict()
		self.output = self.pans.typeTupTup['C']
			
	def test_centerTuple_equal_output(self):
		
		test = centerTuples == self.output
		self.assertTrue(test)
	
	
if __name__ == '__main__':
	
	unittest.main()
