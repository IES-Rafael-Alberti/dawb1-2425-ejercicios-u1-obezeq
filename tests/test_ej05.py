#!/usr/bin/env python3

from src.ej05_def2 import calcula_precio
 
def test_iva_general():
    assert calcula_precio(100, 21) == "El precio final del artículo con IVA (21.00) es 121.00€."
    
def test_iva_mayor_cien():
    assert calcula_precio(100, 200) == "El precio final del artículo con IVA (200.00) es 300.00€."
    
def test_importe_negativo():
    assert calcula_precio(-1, 10) == "El importe debe ser mayor o igual a 0"