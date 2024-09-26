#!/usr/bin/env python3

try:
    peso = float(input("Cual es tu peso en (en kg)? "))
    estatura = float(input("Cual es tu estatura (en metros)? "))

    IMC = (peso / (estatura**2))
    print(f"Tu índice de masa corporal es: {round(IMC, 2)} kg/m^2")

except ValueError:
    print(f"\nNo has introducido un número!")