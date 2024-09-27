#!/usr/bin/env python3
import os

iva_general = 1.21
iva_reducido = 1.1
iva_superreducido = 1.04
iva_externo = 1

def calculador(importe, iva):
    total = round((importe * iva), 2)
    print(f"El precio final del articulo es: {total}")

try:
    importe = float(input("Introduce el importe sin IVA de tu artículo: "))

    print("Selecciona el tipo de IVA:")
    print("[1] IVA General")
    print("[2] IVA Reducido")
    print("[3] IVA Superreducido")
    print("[4] Actividades extensas de IVA\n")

    option = int(input("Introduce la opcion: "))

    if option == 1:
        calculador(importe, iva_general)
    elif option == 2:
        calculador(importe, iva_reducido)
    elif option == 3:
        calculador(importe, iva_superreducido)
    elif option == 4:
        calculador(importe, iva_externo)
    else:
        print("Opcion no correcta.")
        os._exit(0)

except ValueError:
    print("No has introducido un número!")
    