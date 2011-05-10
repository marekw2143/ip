import unittest
from numpy import *
from image_manipulator import ImageManipulator, open_file
from common import _cmp_arr

dtype = int16

class ImageManipulatorTestCase (unittest.TestCase):
	def setUp(self):
		self.manipulator = ImageManipulator ()
		self.black = open_file ('imgs/black.png')
		self.white = open_file ('imgs/white.png')

		self.black_width = self.black.size[0]
		self.black_height = self.black.size[1]

		self.white_width = self.white.size[0]
		self.white_height = self.white.size[1]
	
		# shape - rows, columns

	def test_dtype(self):
		arr = self.manipulator.getGrayArray (self.white)
		self.assertEquals (int16, arr.dtype)

	def test_get_gray_array(self):
		arr = self.manipulator.getGrayArray (self.black)
		self.assertEquals(arr.shape[1], self.black_width)
		self.assertEquals(arr.shape[0], self.black_height)
		self.assertTrue(_cmp_arr(zeros((self.black_height, self.black_width), dtype = dtype), arr))

		arr = self.manipulator.getGrayArray (self.white)
		ret = zeros((self.white_height, self.white_width), dtype = dtype)
		for row in range(arr.shape[0]):
			for col in range(arr.shape[1]):
				ret[row, col] = 255

		self.assertEquals(arr.shape[1], self.white_width)
		self.assertEquals(arr.shape[0], self.white_height)
		self.assertTrue(_cmp_arr(ret, arr))

	def test_save (self):
		''' checks whether opening image and then saving it, produces same image'''
		arr = self.manipulator.getGrayArray (self.white)
		im = self.manipulator.create_image (arr)
	
		arr2 = self.manipulator.getGrayArray (im)
		good_ret = zeros((self.white_height, self.white_width), dtype = uint8)
		for row in range(arr.shape[0]):
			for col in range(arr.shape[1]):
				good_ret[row, col] = 255
		self.assertTrue(_cmp_arr(good_ret, arr2))


