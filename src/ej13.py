#!/usr/bin/env python3

try:
    num1 = int(input ("Introduce el primer número entero: "))
    num2 = int(input ("Introduce el segundo número entero: "))

    cociente = num1 // num2
    resto = num1 % num2

    print(f"La división entre {num1} y {num2} da un cociente {cociente} y un resto {resto}")

except ValueError:
    print(f"\nNo has introducido un número entero!")