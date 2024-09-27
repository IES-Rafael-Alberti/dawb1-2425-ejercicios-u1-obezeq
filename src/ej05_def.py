#!/usr/bin/env python3

def calculador(importe, iva):
    if importe >= 0:
        total = round((importe * iva), 2)
        print(f"El precio final del articulo es: {total}")
    else:
        print(f"El importe debe ser mayor o igual a 0")