from numpy import *
from histogram import Histogram, generate
import unittest

dtype = int16
class HistogramTestCase (unittest.TestCase):
	def setUp (self):
		self.arr = array( [	[  1,  1,  2,  1],  # 1 - 3, 2 - 1
							[  3,  2,  1,  3],  # 1 - 1, 2 - 1, 3 - 2
							[  1,  2,  2,  2]], dtype = dtype) # 1 - 1, 2 - 3
		
		self.amounts = {1: 5, 2: 5, 3: 2}

	def test_generate (self):
		hist = generate (self.arr)
		for k,v in self.amounts.items ():
			self.assertEquals (hist.get(k), v)

