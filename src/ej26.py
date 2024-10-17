#!/usr/bin/env python3

lista = input("Introduce los productos de tu cesta de la compra (separalos por comas): ")

# En caso que solo se introduzca un producto sin coma, solamente existirá ese producto en la cesta de la compra.
# Pues en una cesta de la compra puedes tener también solamente un producto.

productos = lista.split(",")

print("La lista de la compra es: ")
for producto in productos:
    print(f"- {producto}")