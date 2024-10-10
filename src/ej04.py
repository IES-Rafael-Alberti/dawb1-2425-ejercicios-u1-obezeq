#!/usr/bin/env python3

try:
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    fahrenheit = celsius * 33.8

    celsius = round(celsius, 2)
    fahrenheit = round(fahrenheit, 2)

    print(f"La temperatura en grados Farenheit es {celsius*33.8}ºF ({celsius}ºC)")
    
except ValueError:
    print("No has introducido una temperatura!")