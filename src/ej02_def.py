#!/usr/bin/env python3

def importe(hours, cost):
    return hours * cost

try:
    hours = int(input("Horas de trabajo: "))
    cost = int(input("Coste por hora: "))
    print(f"Importe total: {importe(hours,cost)}")
except ValueError:
    print("No has introducido numero!")