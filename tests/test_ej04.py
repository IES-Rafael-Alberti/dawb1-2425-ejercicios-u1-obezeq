#!/usr/bin/env python3

from src.ej04_def2 import grados_celsius

def test_conversion_positiva():
    assert grados_celsius(33.8) == 1.0
    
def test_conversion_negativa():
    assert grados_celsius(-33.8) == -1.0