#!/usr/bin/env python3

import pytest
from src.prueba1 import mayor

def test_mayor_a():
    assert mayor(6, 3) == 6
def test_mayor_b():
    assert mayor(3, 9) == 9
def test_iguales():
    assert mayor(3, 3) == 0
def test_mayor_negativo_negativo():
    assert mayor(-13, -11) == -11
def test_mayor_negativo_positivo():
    assert mayor(-3, 3) == 3