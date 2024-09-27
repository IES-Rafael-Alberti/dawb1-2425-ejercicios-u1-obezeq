#!/usr/bin/env python3

import pytest
from src.ej05_def import calculador

def test_iva_general(capfd):
    calculador(1, 1.21)
    output = capfd.readouterr()
    assert output.out.strip() == "El precio final del articulo es: 1.21"
    
def test_iva_reducido(capfd):
    calculador(1, 1.1)
    output = capfd.readouterr()
    assert output.out.strip() == "El precio final del articulo es: 1.1"
    
def test_iva_superreducido(capfd):
    calculador(1, 1.04)
    output = capfd.readouterr()
    assert output.out.strip() == "El precio final del articulo es: 1.04"
    
def test_iva_superreducido(capfd):
    calculador(1, 1)
    output = capfd.readouterr()
    assert output.out.strip() == "El precio final del articulo es: 1"
def test_importe_negativo(capfd):
    calculador(-1, 1)
    output = capfd.readouterr()
    assert output.out.strip() == "El importe debe ser mayor o igual a 0"