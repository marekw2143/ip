import unittest
from numpy import *
from ImageProcessor import FilterAdapter
from common import _cmp_arr

dtype = int16

class ImagePorcessorTestCase (unittest.TestCase):
	_cmp_arr = _cmp_arr
			
	def setUp(self):
		self.fa = FilterAdapter ()
		self._cmp_arr = _cmp_arr
		self.arr = array( [	[  1,  3,  7,  2],
							[  5, 23,  8, 19],
							[  4, 32, 91,  8],
							[ 51, 35,  2,  4] ], dtype = dtype)


	def _test_avg(self, fnct):
		filter = ones((3,3))

		arr = arange(16).reshape(4,4)
		ret = fnct(arr, filter, 9)
		good_ret = array( [	[0, 0, 0, 0],
							[0, 5, 6, 0], 
							[0, 9, 10, 0], 
							[0, 0, 0, 0] ], dtype=dtype)
		self.assertTrue(self._cmp_arr(ret, good_ret))


		arr = self.arr

		good_ret = array([
			[  0,  0,  0,  0],
			[  0, 19, 21,  0],
			[  0, 27, 24,  0],
			[  0,  0,  0,  0]
		], dtype = dtype)
		ret = fnct(arr, filter, 9)
		self.assertTrue(self._cmp_arr(ret, good_ret))


		arr = array( [	[0, 10, 10, 10],
						[0, 10, 10, 10],
						[0, 10, 10, 10]], dtype = dtype)	

		good_ret = array([	[0, 0, 0, 0],
							[0, 30/9, 0, 0],
							[0, 0,	0,	0],], dtype = dtype)

		filter = array([[-1, 0, 1],
						[-1, 0, 1],
						[-1, 0, 1]],dtype = dtype)

		ret = fnct(arr, filter, 9)
		self.assertTrue(self._cmp_arr(ret, good_ret))


	def _test_median(self, fnct):
		ret = fnct(self.arr)
		good_ret = array([ 	[  0,  0,  0,  0],
							[  0,  7,  8,  0],
							[  0, 23, 19,  0],
							[  0,  0,  0,  0]], dtype = dtype)
		self.assertTrue(self._cmp_arr(ret, good_ret))
		
	def test_median(self):
		self._test_median(self.fa.apply_median)


	def test_avg_filter2 (self):
		self._test_avg(self.fa.apply_filter2)

	def test_avg_filter3 (self):
		self._test_avg(self.fa.apply_filter3)


	def test_cmp(self):
		arr1 = ones((3,4))
		arr2 = ones((3,3))
		self.assertFalse(self._cmp_arr(arr1, arr2))
		arr2 = zeros((3,4))
		self.assertFalse(self._cmp_arr(arr1, arr2))

