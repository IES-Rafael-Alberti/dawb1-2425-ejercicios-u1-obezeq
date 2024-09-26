#!/usr/bin/env python3

email = input("Introduce tu correo eletrónico: ")

try:
    filtered_email = email.split("@")
    new_email = f"{filtered_email[0]}@ceu.es"

    print(new_email)

except IndexError:
    print("El formato del email no es correcto.")