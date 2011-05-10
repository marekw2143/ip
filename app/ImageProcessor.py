from numpy import *
from pdb import set_trace

dtype = int16

class Filter (object):
    def __init__(self, x, y):
        self.shape = (x, y)


class FilterAdapter(object):

    def _calculate_boundaries(self, filter, arr_in):
        ''' returns coordinates of array for which filter can be applied '''
        min_row = (filter.shape[0] - 1) / 2 #index of the min row to apply filter for
        max_row = arr_in.shape[0] - min_row - 1 #index of the max row to apply filter for
        
        min_col = (filter.shape[1] - 1) / 2
        max_col = arr_in.shape[1] - min_col - 1
        
        return min_row, max_row, min_col, max_col


    def _perform_on_each(self, shape_pattern, arr_in, fnct, **kwargs):
        ''' for each pixel in arr_in, that can be applied filter with size of shape_pattern, call
        fnct with arguments: position (row, col), boundaries (dictionary of min/max_row/col), arr_in, arr_out, **kwargs
        fnct should update arr_out '''
        min_row, max_row, min_col, max_col = self._calculate_boundaries(shape_pattern, arr_in)
        boundaries = {'min_row': min_row, 'max_row': max_row, 'min_col': min_col, 'max_col': max_col}
        arr_out = zeros((arr_in.shape[0], arr_in.shape[1]), dtype = dtype)
        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                position = row, col
                fnct(position, boundaries, arr_in, arr_out, **kwargs)
        return arr_out
    perform_on_each = _perform_on_each


    def __apply_filter(self, position, boundaries, arr_in, arr_out, **kwargs):
        """
        Multiplies all points in range defined by {boundaries} from pixel defined by {position} by their corresponding
        positions in {kwargs['filter']}
        then resulting value is divided by {kwargs['multiply']} and set to {arr_out({position})}
        """
        row, col = position
        min_row, min_col = boundaries.get('min_row'), boundaries.get('min_col')
        filter, multiply = kwargs.get('filter'), kwargs.get('multiply')

        val = 0
        for y in range(-min_row, min_row + 1):
            for x in range(-min_col, min_col + 1):
                val += arr_in[row + y, col + x] * filter[min_row + y, min_col + x]

        val = val / multiply
        arr_out[row, col] = val	

    def median_filter(self, position, boundaries, arr_in, arr_out, **kwargs):
        row, col = position
        min_row, min_col = boundaries.get('min_row'), boundaries.get('min_col')
        vals = []
        for y in range(-min_row, min_row + 1):
            for x in range(-min_col, min_col + 1):
                vals.append (arr_in[row+y, col+x] )
        vals = sort(vals)
        arr_out[row, col] = vals[ len(vals) / 2 - 1 + 1 ]
        

    def apply_filter3(self, arr_in, filter, multiply = 1):
        return self._perform_on_each(filter, arr_in, self.__apply_filter, **{'filter': filter, 'multiply': multiply})

    def apply_median(self, arr_in):
        shape = Filter(3, 3)
        return self._perform_on_each(shape, arr_in, self.median_filter)

    def apply_filter2(self, arr_in, filter, multiply = 1):
        u'''applies given filter for whole image
        arr_in - input array representing image, in grayscale
        filter - filter to apply, must be in size (2n+1, 2n+1)
        multiply - value that will be multipled by product of filter

        returns array of the size of input array'''
        min_row, max_row, min_col, max_col = self._calculate_boundaries(filter, arr_in)
        arr_out = zeros((arr_in.shape[0], arr_in.shape[1]), dtype = dtype)
        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                val = 0
                for y in range(-min_row, min_row + 1):
                    for x in range(-min_col, min_col + 1):
                        val += arr_in[row + y, col + x] * filter[min_row + y, min_col + x]
                val = val / multiply
                if val>255: val = 255
                arr_out[row, col] = val	
        return arr_out

    def density_fitler(self, arr_in, size = Filter(4, 4)):
        ''' calcluates destiny of given points '''

                

class SimpleConversion (object):
    # set threslod to max value of all 
    def threslod(self, arr_in, threslod, passed = 255, not_passed = 0):
        ''' makes thresloding  - all pixels with value > threslod will have new_value set to passed, other will have not passed '''
        arr_out = zeros((arr_in.shape[0], arr_in.shape[1]), dtype = dtype)
        for row in range(arr_in.shape[0]):
            for col in range(arr_in.shape[1]):
                val = arr_in [row, col]
                new_val = None
                if val > threslod:
                    new_val = passed
                else:
                    new_val = not_passed
                arr_out[row, col]  = new_val
        return arr_out
    def cut_vals (self, arr, min, max):
        ''' all pixel values > max will have value set to max, all with value<min will have val = min'''
        rows, cols = arr.shape
        ret =  zeros((rows, cols), dtype = dtype)
        for r in range(rows):
            for c in range(cols):
                val = arr[r, c]
                if val > max: val = max
                elif val < min: val = min
                ret[r,c ] = val
        return ret

    def convert(self, arr, dtype):
        ''' converts given array to given dtype '''
        height, width = arr.shape
        ret_arr = zeros((height, width), dtype =dtype)
        for row in range(height):
            for col in range(width):
                ret_arr[row, col] = arr[row, col]
        return ret_arr

    def get_uint8(self, arr):
        ''' returns array converted to uint8 '''
        return self.convert(arr, uint8)

    def get_int16(self, arr):
        return self.convert(arr, int16)


