''' Image related stuff '''
from numpy import *
import Image
from pdb import set_trace
dtype = int16

class ImageManipulator(object):
	def getGrayArray(self, im):
		u'returns array of pixels of image converted to grayscale'
		im = im.convert('L')
		pix = im.load ()
		width, height = im.size[1], im.size[0]
		arr = zeros((width, height), dtype=uint8)
		for r in range(width):
			for c in range(height):
				arr[r, c] = pix[c, r]
		ret = zeros((width, height), dtype = dtype)
		for r in range(width):
			for c in range(height):
				ret[r, c] = arr[r, c]
		from ImageProcessor import SimpleConversion
		return SimpleConversion ().cut_vals(ret, 0, 255)


	def create_array(self, im):
		u'''returns numpy array of pixels in an image'''
		rows = im.size[1]
		columns = im.size[0]
		arr = zeros((rows, columns, 3), dtype=uint8)
		pix = im.load()
		for row in range(rows):
			for col in range(columns):
				for i in range(3):
					color = pix[col, row][i]
					arr[row, col, i] = color
		return arr

	def create_image(self, arr):
		u'returns image object from the numpy array of the pixels'
		return Image.fromarray(arr)
	
