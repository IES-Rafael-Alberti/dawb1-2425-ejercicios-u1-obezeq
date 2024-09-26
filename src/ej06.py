#!/usr/bin/env python3

iva = 0.1

try:
    importe = float(input(f"Importe final de tu artículo con {iva*100}% IVA: "))
    print(f"Has pagado {importe*iva}€ de IVA.")
    print(f"El importe sin IVA es {importe*(1-iva)}€")
except ValueError:
    print("No has introducido un número!")