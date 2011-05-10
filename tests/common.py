import unittest
from numpy import *

def _cmp_arr(a1, a2):
    if a1.shape != a2.shape: return False

    for row in range(a1.shape[0]):
        for col in range(a1.shape[1]):
            if a1[row, col] != a2[row, col]: return False
            
    return True
