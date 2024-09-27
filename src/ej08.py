#!/usr/bin/env python3

try:
    num = float(input("Introduce el primer número: "))
    num += float(input("Introduce el segundo número: "))
    num += float(input("Introduce el tercer número: "))

    print(f"\nLa suma es: {round(num, 2)}")
    
except ValueError:
    print(f"\nNo has introducido un número!")