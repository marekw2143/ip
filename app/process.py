import pdb 
import Image 
import os 
import sys
from numpy import *
from ImageProcessor import *
from image_manipulator import ImageManipulator, open_file, SimpleConversion

dtype = int16

show = lambda arr: ImageManipulator().create_image(arr).show()

def main():
    processor, manipulator, cvt = FilterAdapter(), ImageManipulator(), SimpleConversion ()
    im = open_file("imgs/google_Captcha.jpeg")
    arr = manipulator.getGrayArray(im)
    arr = cvt.threslod(arr, 130)
    #@	filter = array([	[ 0, -2, 0],
    #						[-2, 0, 2], 
    #						[ 0, 2, 0]], dtype = dtype)
    filter = array([    [0, 0, 0],
                        [-1, 1, 0],
                        [0, 0, 0]], dtype = dtype)
#    arr = processor.apply_filter3( arr, filter)
#    arr = processor.apply_median( arr)
#    arr = absolute(arr)
    show(arr)


if __name__ == '__main__':
    main()
