#!/usr/bin/env python3
# Calcular el área de un triángulo a partir de tres lados

import math

def calcular_area(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))

    return area

def calcular_triangulo_valido(a, b, c):
    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
        return True
    else:
        return False

def comprobacion_input(a, b, c):
    if a.find(',') != -1:
        a = a.replace(',', '.')
        b = b.replace(',', '.')
        c = c.replace(',', '.')
    try:
        a = float(input("Introduce el lado a del triangulo: "))
        b = float(input("Introduce el lado b del triangulo: "))
        c = float(input("Introduce el lado c del triangulo: "))

        return True
    
    except ValueError:
        return False

def main():
    a = input("Introduce el lado a del triangulo: ")
    b = input("Introduce el lado b del triangulo: ")
    c = input("Introduce el lado c del triangulo: ")

    input_valido = comprobacion_input(a, b, c)
    if input_valido:
        triangulo_valido = calcular_triangulo_valido(a, b, c)
        if triangulo_valido:
            area_triangulo = calcular_area(a, b, c)
            print(f"El area del triangulo es: {round(area_triangulo, 2)} u.")
        else:
            print(f"El triangulo no es valido.")
    else:
        print(f"Uno de los lados que has introducido no lo ha introducido en el formato correcto.")

if __name__ == '__main__':
    main()