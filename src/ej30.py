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

while n <= total:
    list.append(n)
    n = n + incremento

counter = 0
end = len(list)

print(f"SERIE => ", end="")
for i in list:
    counter += 1
    if counter == 1:
        print(f"{i}", end="-")
    elif counter == (len(list) - 1):
        print(f"{i}", end="-")
    elif counter == len(list):
        print(f"{i}", end="")
    else:
        print(f"{i}", end="..")