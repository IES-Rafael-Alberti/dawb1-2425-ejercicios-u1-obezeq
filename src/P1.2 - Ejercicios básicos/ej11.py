#!/usr/bin/env python3

try:
    n = int(input("Introduce un número entero positivo: "))

    if n > 0:
        suma = (n*(n+1))/2
        print(f"La suma ({n}*({n}+1))/2 = {suma}")
    else:
        print("El número es negativo.")
except ValueError:
    print(f"\nNo has introducido un número!")