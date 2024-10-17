#!/usr/bin/env python3

username = input("Introduce tu nombre de usuario: ")

try:
    n = int(input("Introduce un número entero: "))

    for i in range(n):
        print(username)

except ValueError:
    print("No has introducido un número entero!")