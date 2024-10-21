#!/usr/bin/env python3

try:
    precio = float(input("Introduce el precio del producto en euros con dos decimales: "))
    precio = round(precio, 2)

    precio_filtrado = str(precio).split(".")
    euros = precio_filtrado[0]
    centimos = precio_filtrado[1]
    
    print(f"El precio es: {euros} euros con {centimos} centimos.")

except ValueError:
    print("No has introducido un número!")
