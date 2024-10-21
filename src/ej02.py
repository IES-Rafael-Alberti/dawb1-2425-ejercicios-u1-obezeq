#!/usr/bin/env python3

try:
    hours = int(input("Horas de trabajo: "))
    cost = int(input("Coste por hora: "))
    print(f"Importe total: {hours*cost}")
except ValueError:
    print("No has introducido numero!")