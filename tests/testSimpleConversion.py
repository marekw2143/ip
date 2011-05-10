import unittest
from numpy import *
from ImageProcessor import SimpleConversion
from common import _cmp_arr

dtype = int16

class SimpleConversionTestCace (unittest.TestCase):
	def setUp(self):
		self.cnv = SimpleConversion ()
		self.arr = array( [	[  1,  3,  7,  2],
							[  5, 23,  8, 19],
							[  4, 32, 91,  8],
							[ 51, 35,  2,  4] ], dtype = dtype)


	def test_threslod(self):
		ret = self.cnv.threslod ( self.arr, 50)
		good_ret = array( [	[  0,  0,  0,  0],
							[  0,  0,  0,  0],
							[  0,  0,255,  0],
							[255,  0,  0,  0]], dtype = dtype)
		self.assertTrue(_cmp_arr(ret, good_ret))

	def test_cut_vals (self):
		arr = array( [	[10, 15, -1, 0],
						[10, 15, -1, 0],
						[10, 15, -1, 0]], dtype = dtype)

		good_ret = array([	[10, 10, 0, 0], 
							[10, 10, 0, 0], 
							[10, 10, 0, 0]], dtype = dtype)
		ret = self.cnv.cut_vals(arr, 0, 10)
		self.assertTrue(_cmp_arr(good_ret, ret))
