#!/usr/bin/env python3

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

new_frase = ""

for letter in frase:
    if letter == vocal:
        letter = letter.upper()
    new_frase = new_frase + letter

print(new_frase)    