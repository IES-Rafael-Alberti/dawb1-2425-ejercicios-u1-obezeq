#!/usr/bin/env python3

try:
    numero = int(input("Introduce un número de inicio: "))
except ValueError:
    print("ERROR: No has introducido un número!")

incremento = 0
while incremento < 1:
    try:
        incremento = int(input("\nIntroduce un incremento: "))
        if incremento < 1:
            print("ERROR: El incremento tiene que ser mayor a 0.")
    except ValueError:
        print("ERROR: No has introducido un número!")

total = 0
while total < 1:
    try:
        total = int(input("\nIntroduce un número total de la serie: "))
        if total < 1:
            print("ERROR: El total de la serie tiene que ser mayor a 0")
    except ValueError:
        print("ERROR: No has introducido un número!")

list = []
n = numero

if numero <= incremento:

    ultimo = total - incremento + numero
    penultimo = ultimo - incremento

else:

    if (total - incremento - incremento + numero) == total:
        ultimo = total
        penultimo = ultimo - incremento
    else:
        diferencia = (numero - incremento)
        diferencia = numero + diferencia - incremento
        ultimo = total - diferencia
        penultimo = ultimo - incremento

        # ultimo = total - incremento
        # penultimo = ultimo - incremento

        # penultimo = 87
        # ultimo = 94

print(ultimo)
print(penultimo)


print("SERIE => ", end="")
while n <= total:

    if n == numero:
        print(f"{n}", end="-")

    elif n == penultimo:
        print(f"{n}", end="-")

    elif n == ultimo:
        print(f"{n}", end="")

    elif n >= (n+incremento) or n <= (penultimo - incremento):
        print(f"{n}", end="..")

    n = n + incremento



"""
if (incremento - numero) == 0:
    limit = 1
else:
    limit = (incremento + numero +1)
    print(limit)

print("SERIE => ", end="")
while n <= total:
    # list.append(n)

    # error with 5-10-100

    if n == numero:
        print(f"{n}-", end="")
    elif n == (total-limit):
        print(f"{n}-{n+incremento}", end="")
    elif n < (total - incremento):
        print(f"{n}", end="..")
    elif n == (total-incremento):
        print(f"{n}-{n+incremento}", end="")

    n = n + incremento
"""