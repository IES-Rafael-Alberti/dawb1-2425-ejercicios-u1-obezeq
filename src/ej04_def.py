#!/usr/bin/env python3

def conversion():
    fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
    
    celsius = fahrenheit / 33.8
    celsius = round(celsius, 2)
    
    return celsius

try:
    
    celsius = conversion()

    print(f"La temperatura en grados Celsius es {celsius}ºC")
    
except ValueError:
    print("No has introducido una temperatura!")
    