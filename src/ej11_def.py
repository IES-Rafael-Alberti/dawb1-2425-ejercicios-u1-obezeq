#!/usr/bin/env python3

def checker(n):
    if n >= 0:
        suma = (n*(n+1))/2
        return f"La suma ({n}*({n}+1))/2 = {suma}"
    else:
        return "ERROR: El número es negativo."

try:
    n = int(input("Introduce un número entero positivo: "))
    print(checker(n))
except ValueError:
    print(f"\nERROR: No has introducido un número!")
    