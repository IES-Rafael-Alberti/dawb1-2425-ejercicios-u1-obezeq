#!/usr/bin/env python3

name = input("Cual es tu nombre? ")
surname1 = input("Cual es tu primer apellido? ")
surname2 = input("Cual es tu segundo apellido? ")

name_surname = name + " " + surname1 + " " + surname2

print(name_surname.lower())
print(name_surname.upper())
print(name_surname.title())