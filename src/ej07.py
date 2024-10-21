#!/usr/bin/env python3

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    num3 = float(input("Introduce el tercer número: "))

    suma = num1 + num2 + num3

    print(f"\nLa suma de {num1}+{num2}+{num3} = {round(suma, 2)}")
    
except ValueError:
    print(f"\nNo has introducido un número!")