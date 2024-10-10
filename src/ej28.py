#!/usr/bin/env python3

try:
    n1 = input("Introduce el primer número entero: ")
    n2 = input("Introduce el segundo número entero: ")

    if str(float(n1)) == f"{n1}.0" and str(float(n2)) == f"{n2}.0":
        n1 = int(n1)
        n2 = int(n2)

        if n1 == n2:
            print("ERROR: Los números no pueden ser iguales")

        elif n1 < n2:
            print(f"El número menor es el {n1} y entre ellos existen {n2-n1} números enteros")
        else:
            print(f"El número menor es el {n2} y entre ellos existen {n1-n2} números enteros")
    else:
        print("ERROR: Tienes que introducir un número entero!")

except ValueError:
    print("ERROR: No has introducido un número!")