import unittest
from numpy import *
from image_manipulator import ImageManipulator
from common import _cmp_arr
from descr import Searcher, DIRECTION_UP, DIRECTION_DOWN,DIRECTION_LEFT, DIRECTION_RIGHT, NextFinder, SearchNearest
from pdb import set_trace

dtype = int16

class DescrTestCase (unittest.TestCase):
    def setUp(self):
        self.searcher = Searcher ()


    def test_searcher_get_next_from_pattern(self):
        fnct = self.searcher.get_next
        self._test_get_next_3_3(fnct)
        self._test_get_next_3_5(fnct)

    def test_get_next (self):
        arr = array([	[100,4,100],
                        [5,1,6],
                        [2,0,3]], dtype = dtype)
        nf = SearchNearest (arr)
        nf.make_priors ()
        fnct = nf.get_next
        self._test_get_next_3_3(fnct)
        arr = array([	[100,100,4,100,100],
                        [100,5,1,6,100],
                        [7,2,0,3,8]], dtype = dtype)
        nf = SearchNearest (arr)
        nf.make_priors ()
        fnct = nf.get_next
        self._test_get_next_3_5(fnct)

    def _test_get_next_3_3(self, fnct):
        arr = array([ 	[0, 0, 0],
                        [1, 0, 0],
                        [0, 0, 0]], dtype = dtype)
        ret = fnct(arr, 1)
        self.assertEquals(ret, (-1, 1))
    
    
        arr = array([	[0, 1, 0],
                        [0, 0, 0],
                        [0, 0, 0]], dtype = dtype)
        ret = fnct(arr, 1)
        self.assertEquals(ret, (0, 2))


    def _test_get_next_3_5(self, fnct):
        arr = array([	[0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0]], dtype = dtype)
        ret = fnct(arr, 1)
        self.assertEquals(ret, (-1, 0))
                    

        arr = array([	[0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0]], dtype = dtype)
        ret = fnct(arr, 1)
        self.assertEquals(ret, (-1, 1))
        

        arr = array([	[0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0],
                        [1, 0, 0, 0, 0]], dtype = dtype)
        ret = fnct(arr, 1)
        self.assertEquals(ret, (0, 2))
        

        arr = array([	[0, 0, 1, 0, 0],
                        [0, 1, 1, 0, 0],
                        [1, 0, 0, 0, 0]], dtype = dtype)
        ret = fnct(arr, 1)
        self.assertEquals(ret, (0, 1))

            
        arr = array([	[0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0],
                        [1, 0, 0, 1, 0]], dtype = dtype)
        ret = fnct(arr, 1)
        self.assertEquals(ret, (1, 0))


        arr = array([	[0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0],
                        [1, 0, 1, 1, 0]], dtype = dtype)
        ret = fnct(arr, 1)
        self.assertEquals(ret, (1, 0))
        self.assertTrue(_cmp_arr(arr, array([	[0, 0, 1, 0, 0],
                                                [0, 1, 0, 0, 0],
                                                [1, 0, 1, 1, 0]], dtype = dtype)))

    def test_get_subarr(self):
        arr = array([	[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12]], dtype = dtype)
        ret = self.searcher.get_subarr( arr, (1, 2), (2, 2))# [[7,8], [11,12]]
        self.assertTrue(_cmp_arr(ret, array([[7,8], [11,12]], dtype =dtype)))
        self.assertTrue (_cmp_arr(arr, array([	[1, 2, 3, 4], #array doesn't changes
                                                [5, 6, 7, 8],
                                                [9, 10, 11, 12]], dtype = dtype)))

    def test_get_subarray_direction (self):
        arr = array([	[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12]], dtype = dtype)
        ret = self.searcher.get_subarr_direction(arr, (2, 1), DIRECTION_UP, (2, 3))
        self.assertTrue (_cmp_arr(ret, array([[1, 2, 3], [5, 6, 7]], dtype = dtype )))
        self.assertTrue (_cmp_arr(arr, array([	[1, 2, 3, 4], #array doesn't changes
                                                [5, 6, 7, 8],
                                                [9, 10, 11, 12]], dtype = dtype)))

        
        ret = self.searcher.get_subarr_direction(arr, (0, 1), DIRECTION_DOWN, (2, 3))
        self.assertTrue (_cmp_arr(ret, array([[5, 6, 7],[1, 2, 3]], dtype = dtype )))
        self.assertTrue (_cmp_arr(arr, array([	[1, 2, 3, 4], #array doesn't changes
                                                [5, 6, 7, 8],
                                                [9, 10, 11, 12]], dtype = dtype)))


        
        ret = self.searcher.get_subarr_direction(arr, (1,1), DIRECTION_LEFT, (2, 3))
        self.assertTrue (_cmp_arr(ret, array([[9, 5, 1],[10, 6, 2]], dtype = dtype )))
        self.assertTrue (_cmp_arr(arr, array([	[1, 2, 3, 4], #array doesn't changes
                                                [5, 6, 7, 8],
                                                [9, 10, 11, 12]], dtype = dtype)))


        return 
        ret = self.searcher.get_subarr_direction(arr, (0, 1), DIRECTION_RIGHT, (2, 3))
        self.assertTrue (_cmp_arr(ret, array([[5, 6, 7],[1, 2, 3]], dtype = dtype )))
        self.assertTrue (_cmp_arr(arr, array([	[1, 2, 3, 4], #array doesn't changes
                                                [5, 6, 7, 8],
                                                [9, 10, 11, 12]], dtype = dtype)))

        
