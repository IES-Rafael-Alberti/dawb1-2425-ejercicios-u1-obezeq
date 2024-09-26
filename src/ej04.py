#!/usr/bin/env python3

try:
    celsius = float(input("Introduce la temperatura en grados celsius: "))
    fahrenheit = print(f"La temperatura {celsius} °C es {celsius*33.8} °F")
except ValueError:
    print("No has introducido una temperatura!")