#!/usr/bin/env python3

peso_payaso = 112
peso_muneca = 75

try:
    payaso = int(input("Introduce el número de payasos vendido en el último pedido (en gramos): "))
    muneca = int(input("Introduce el número de muñecas vendido en el último pedido (en gramos): "))

    peso = (payaso*peso_payaso) + (muneca*peso_muneca)

    print(f"El peso total del paquete que será enviado será: {peso}g.")

except ValueError:
    print(f"\nNo has introducido un número entero!")