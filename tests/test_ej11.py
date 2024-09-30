#!/usr/bin/env python3

from src.ej11_def import checker

def test_numero_positivo():
    assert checker(3) == f"(3*(3+1))/2 = 6.0"

def test_numero_negativo():
    assert checker(-1) == "ERROR: El número es negativo."