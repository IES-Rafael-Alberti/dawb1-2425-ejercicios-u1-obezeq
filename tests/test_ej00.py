#!/usr/bin/env python3

from src.ej00 import ejecucion_programa
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        ejecucion_programa()
    def test_2(self):
        ejecucion_programa()

if __name__ == '__main__':
    unittest.main()