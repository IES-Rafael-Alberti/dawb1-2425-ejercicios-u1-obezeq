#!/usr/bin/env python3

fecha = input("Introduce tu fecha de nacimiento en este formato (dd/mm/aaaa): ")

try:
    fecha = fecha.split("/")

    dia = int(fecha[0])
    mes = int(fecha[1])
    ano = int(fecha[2])

    correct = True

    if len(dia) != 1 or len(dia) != 2:
        correct = False
    if len(mes) != 1 or len(mes) != 2:
        correct = False
    if len(ano) != 4:
        correct = False

    if correct:
        print(f"Dia: {dia}")
        print(f"Mes: {mes}")
        print(f"Año: {ano}")
    else:
        print("No has introducido la fecha en el formato correcto.")
    
except IndexError:
    print("No has introducido la fecha en el formato correcto.")

except BaseException:
    print("Tienes que introducir una fecha en números con el formato pedido, no en letras.")