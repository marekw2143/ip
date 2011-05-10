import numpy 
import unittest
from pdb import set_trace
dtype = numpy.int16
import math

my_ind = lambda : None


def make_repr(arr_in):
        """ 
    1. from starting pixel - move in one direction to find start
    2. from start - move in one direction at some interval (e.g. 5 loops) to get direction of part
    3. if part is simple line - save it's start-stop points, and angle
        """

def get_next_decorator(fnct):
    """
    Decorator
    Sets starting point to 0, so that __no__ match would be performed 
    at that point
    Doesn't change arr (resets starting points value before exit)
    """
    def get_next(self, arr, val = 1):
        height, width = arr.shape
        def pos(x, y):
            ''' transforms x, y relative to arr position '''
            row = height - y - 1
            col = width/2 + x
            return row, col
        # remember value of starting point 
        old_start_y, old_start_x = pos(0, 0)
        old_val = arr[old_start_y, old_start_x]
        arr[old_start_y, old_start_x] = 0
      
        # call function actually
        ret = fnct(self, arr, val)

        # restore old start value
        arr[ old_start_y, old_start_x] = old_val
        return ret
        
    return get_next

DIRECTION_UP = 0
DIRECTION_DOWN = 1
DIRECTION_LEFT = 2 
DIRECTION_RIGHT = 3 

class Description (object):
    def __init__(self, name):
        self.type = name

#class Vector (Description):
    #def __init__(self):
        #Description.__init__(self, 'Vector')

class Arch (Description):
    def __init__(self):
        Description.__init__(self, 'Arch')

class NextFinder(object):
    """
    Allows finding nex pixel in given array
    before use @make_priors must be called
    uses stored array pattern to calculate values of next pixels to check
    """
    def __do_make_priors(self):
        """
        Returns list of coordinates (row, col) 
        of next values in self.parr to check against existance of
        given value
        """
        rows, cols = self.parr.shape
        capacity = rows * cols
        priors = []
        act = found = 0

        while act < capacity:
            for row in range(self.parr.shape[0]):
                if found: break
                for col in range(self.parr.shape[1]):
                    if self.parr[row, col] == act:
                        found = True
                        priors.append( (row, col) )
                        break
            found = 0
            act += 1

        return priors
                

    def __init__(self, priority_arr):
        """
        @param priority_arr: contains array of integers, where each cell contains number when the given pixel should be taken 
        into account
        """
        self.parr = priority_arr

    def make_priors(self):
        """
        initializes object
        """
        self.priors = self.__do_make_priors()

    def get_next(self, arr, val = 1):
        for row, col in self.priors:
            if arr[row, col] == val: 	
                return col -arr.shape[1]/2, (arr.shape[0] - 1) - row  # in () is max row
     
class SearchNearest (NextFinder):
    """
    Searches next element, uses NextFinder's get_next object
    doesn't perform search at current pixel
    doesn't change current pixel value
    
    """
    @get_next_decorator
    def get_next(self, arr, val = 1):
        return NextFinder.get_next(self, arr, val)

class RecursiveSearchNext(object):
    """
    Searches next pixel using dynamically generated order
    Less flexible than SearchNearest
    """
    @get_next_decorator
    def get_next (self, arr, val = 10):#always searches 'UP'
        '''
            arr - part of pattern to get next from
            val - value of pixels matched as passed
            
            returns row, col of next pixel, or None if no next pixel
        '''
        height, width = arr.shape
        def pos(x, y):
            ''' transforms x, y relative to arr position '''
            row = height - y - 1
            col = width/2 + x
            return row, col

        def found(x,y):
            row, col = pos(x,y)
            return arr[row, col] == val

        def found_at_y(y, max_y):
            x_range = max_y - y
            for sign in (-1, 1):
                if found(sign * x_range, y): return sign * x_range, y
    
        for y in range(height):
            act_y = y
            while act_y > -1:
                ret = found_at_y(act_y, y)
                if ret: 
                    return ret
                act_y -= 1


class MemorySearcher (object):# TODO: do it !
    """
    Uses SearchNearest method
    Caches patterns arrays - for generating them uses RecursiveSearchNext
    """
    def __init__(self):
        self.__patterns = {}

    def get_next (self, arr, val = 10):
        pass


class Searcher (object):
    def __init__(self, factory = RecursiveSearchNext()):
        self.get_next = factory.get_next 

                
    def get_subarr(self, arr, start, size):
        """
        Returns array of defined size starting at given coordinates from given array
        (returns part of array)

        @param arr: input array
        @param start: starting pixel (row, col) from which to start (including that one) --> it's top left pixel 
        @param size: size of returned array 
        """
        height, width = size
        ret = numpy.zeros((height, width), dtype = dtype)

        start_row, start_col = start
        for row in range(size[0]):
            for col in range(size[1]):
                ret[row, col] = arr[row + start_row, col + start_col]
        return ret
        
            
    def get_subarr_direction(self, arr, coords, direction, size):
        """
        @param arr: array from which we would like to get subarray
        @param coords: starting point (row, col)
        @param direction: direction of subarray
        @param size: size of expected subarray

        @returns: subarray on the basis of given direction
        size - size of expected arrray (row, col)
        returned array is properly oriented
        """

        row, col = coords
        subarr = None
        if direction == DIRECTION_UP:
            start = (coords[0] - size[0], coords[1] - size[1]/2) # row, col
            subarr = self.get_subarr(arr, start, size)
        elif direction == DIRECTION_DOWN: 
            start = (coords[0], coords[1] - size[1]/2) # row, col
            subarr = self.get_subarr(arr, start, size)
            subarr = numpy.flipud(subarr)
        elif direction == DIRECTION_LEFT:
            start = coords[0] - size[0]/2, coords[1] - size[1]/2
            subarr = self.get_subarr(arr, start, (size[1], size[0]))
            subarr = subarr.transpose()
            subarr = numpy.fliplr (subarr)
            print subarr
        elif directino == DIRECTION_RIGHT:
            pass
        else:
            raise Exception ("Direction: %s is not a valid argument" % direction)
        return subarr
            

    def get_next_pixel (self, arr, coords, direction, value = 1):
        """
        Returns coordinates of next pixel from given arr with value 1
        next pixel is choosen with proper algorithm 
        (see self.get_next in self.__init__)
        """
        subarray = self.get_subarr_direction (arr, coords, direction)
        return self.get_next(subarray, value)
        
                

    def get_descr (self, arr, start, direction, length= 5):
        """
        Returns describing object of array at given direction from starting (row, col) point
        algorithm:
            - get next pixel in given direction
            - collect list of 2 point vectors
            - approximate odd vectors
            - get final vector
        """
        points = []
        start_point = start
        for i in range(length):
            point = self.get_next_pixel(arr, start_point, direction)
            points.append(point)
            start_point = point
        # POINTS COLLECTED
    #    points = self.filter_odd_points(points) #filter points

        # now check shape of that points



