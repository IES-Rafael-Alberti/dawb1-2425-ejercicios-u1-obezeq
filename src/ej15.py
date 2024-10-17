#!/usr/bin/env python3


# Interes al año
interes = 1.04
anos = 3

try:
    dinero = float(input("Introduce la cantidad de dinero depositada en tu cuenta de ahorros: "))

    capital = dinero
    for n in range(anos):
        capital = interes*capital
        
    capital = round(capital, 2)
    print(capital)

except ValueError:
    print(f"\nNo has introducido un número!")