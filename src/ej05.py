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
        imp_iva_general = round((importe*iva_general), 2)
        print(f"El precio final del articulo es: {imp_iva_general}")
    elif option == 2:
        imp_iva_reducido = round((importe*iva_reducido), 2)
        print(f"El precio final del articulo es: {imp_iva_reducido}")    
    elif option == 3:
        imp_iva_superreducido = round((importe*iva_superreducido), 2)
        print(f"El precio final del articulo es: {imp_iva_superreducido}")    
    elif option == 4:
        imp_iva_externo = round((importe*iva_externo), 2)
        print(f"El precio final del articulo es: {imp_iva_externo}")    
    else:
        print("Opcion no correcta.")
        os._exit(0)

except ValueError:
    print("No has introducido un número!")