#!/usr/bin/env python3

phone = input("Introduce un número de telefono en este formato (+34-913724710-56): ")

try:
    phone_number = phone.split('-')

    prefix = phone_number[0]
    number = phone_number[1]
    extension = phone_number[2]

    print(number + "-" + extension)

except IndexError:
    print("No has introducido el número en el formato correcto!")