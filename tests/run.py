import os, sys
sys.path.append(os.path.join(os.path.split(os.getcwd())[0], 'app'))

from testImageProcessor import ImagePorcessorTestCase
from testSimpleConversion import SimpleConversionTestCace
from testHistogram import HistogramTestCase
from testDescr import DescrTestCase
from testImageManipulator import ImageManipulatorTestCase
import unittest

def run():
	unittest.main ()
if __name__ == '__main__':
    run()
