#!/usr/bin/env python3

import os

iva_general = 1.21
iva_reducido = 1.1
iva_superreducido = 1.04
iva_externo = 1

try:
    importe = float(input("Introduce el importe sin IVA de tu artículo: "))

    print("Selecciona el tipo de IVA:")
    print("[1] IVA General")
    print("[2] IVA Reducido")
    print("[3] IVA Superreducido")
    print("[4] Actividades extensas de IVA\n")

    option = int(input("Introduce la opcion: "))

    if option == 1:
        print(f"El precio final del articulo es: {importe*iva_general}")
    elif option == 2:
        print(f"El precio final del articulo es: {importe*iva_reducido}")    
    elif option == 3:
        print(f"El precio final del articulo es: {importe*iva_superreducido}")    
    elif option == 4:
        print(f"El precio final del articulo es: {importe*iva_externo}")    
    else:
        print("Opcion no correcta.")
        os._exit(0)

except ValueError:
    print("No has introducido un número!")