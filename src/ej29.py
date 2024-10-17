#!/usr/bin/env python3

nombre = input("Introduce tu nombre: ")
if nombre.replace(" ", "") == "":
    nombre = "Desconocido"
else:
    nombre =  nombre.title()
try:
    edad = -1
    while edad < 0 and edad < 126:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 125:
            print(f"ERROR: Tienes que introducir un edad entre (0-125)")

    print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {125-edad} años por cumplir")

except ValueError:
    print("ERROR: No has introducido una edad correcta.")