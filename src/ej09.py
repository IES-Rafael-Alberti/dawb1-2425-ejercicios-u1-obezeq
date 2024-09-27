#!/usr/bin/env python3

try:
    print(float(input("Introduce el primer numero: ")) + float(input("Introduce el segundo numero: ")) + float(input("Introduce el tercer numero_ ")))
    
except ValueError:
    print(f"\nNo has introducido un número!")