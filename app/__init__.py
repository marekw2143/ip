import os, sys, pdb
pdb.set_trace()
cwd = os.getcwd()
added = os.path.split(cwd)[0]
added = os.path.join(added, 'tests')
sys.path.append(added)

#os.path.append(os.get_cwd)
from run import run
print 'hey'
run()

if 0:
    from testImageProcessor import ImagePorcessorTestCase
    from testSimpleConversion import SimpleConversionTestCace
    from testHistogram import HistogramTestCase
    from testDescr import DescrTestCase
    from testImageManipulator import ImageManipulatorTestCase
    import unittest

    if __name__ == '__main__':
        unittest.main ()
