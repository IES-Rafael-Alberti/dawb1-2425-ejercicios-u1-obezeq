#!/usr/bin/env python3
# Dependencias
import os

# CONVERSION DE EUROS
def conversion_euros(euros, digitos):
    new_euros = ""

    if len(euros) != digitos:
        n = digitos - len(euros)
        for i in range(n):
            new_euros = new_euros + "0"
    
    euros = new_euros + euros

    return euros

# CONVERSION DE CENTIMOS
def conversion_centimos(centimos):
    if centimos == "0":
        centimos =  "00"

    if len(centimos) == 1:
        centimos = centimos + "0"
    
    if len(centimos) > 2:
        centimos = str(round(float(centimos), 2))

    return centimos

# FUNCIÓN PRINCIPAL "MAIN"
if __name__ == "__main__":

    # CONSEGUIR LOS DATOS DEL USUARIO
    producto = input("[+] Introduce el nombre del producto: ")

    try:
        precio = float(input(f"[+] Introduce el precio del {producto}: "))
        precio = str(round(precio, 2))
    except ValueError:
        print("Tienes que introducir un número, no letras.")
        os._exit(0)

    try:
        unidades = int(input(f"[+] Introduce el número de unidades de {producto}: "))
    except ValueError:
        print("No has introducido un número de unidades correcto.")
        os._exit(0)

    # PRECIO TOTAL
    precio_total = precio * unidades

    # DIVIDIR ENTRE EUROS Y CENTIMOS EN EL PRECIOO
    try:
        euros = precio.split(".")[0]
        euros_total  = precio_total.split(".")[0]
        centimos = precio.split(".")[1]
        centimos_total = precio_total.split(".")[1]
    except Exception as e:
        print(e)

    # CONVERSION DE EUROS
    euros = conversion_euros(euros, 6)
    euros_total = conversion_euros(euros, 8)

    # CONVERSION DE CENTIMOS        
    centimos = conversion_centimos(centimos)

    # IMPRIMIR RESULTADOS EN PANTALLA
    precio = f"{euros},{centimos}"
    precio_total = f"{euros_total},{centimos}"

    print("\n───────────────────────")
    print(f"El precio unitario del {producto} es: {precio}€ euros.")
    print(f"El precio total de {unidades} del {producto} es: {precio_total}€ euros.")