class Histogram (object):
	def __init__(self):
		self._dct = {}

	def add(self, val):
		if val in self._dct:
			self._dct[val] += 1
		else:
			self._dct[val] = 1

	def get(self, val):
		try:
			return self._dct[val]
		except:
			return -1

def generate(arr_in):
	''' generates histogram of values in arr_in '''
	from ImageProcessor import FilterAdapter, Filter

	def fnct(pos, bound, arr_in, _, **kwargs):
		hist = kwargs.get('hist')
		row, col = pos
		hist.add(arr_in[row, col])

	ret = Histogram ()
	for row in range(arr_in.shape[0]):
		for col in range(arr_in.shape[1]):
			ret.add(arr_in[row, col])
	return ret

