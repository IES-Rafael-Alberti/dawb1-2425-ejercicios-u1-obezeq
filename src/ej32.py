#!/usr/bin/env python3
# Cálculo de un número aleatorio entre dos valores

import random

def numero_aleatorio(a: int, b: int) -> int:

    n = random.randrange(a, b)
    return n

def main():
    a = int(input("Introduce un número: "))
    b = int(input("Introduce otro número: "))
    numero_random = numero_aleatorio(a, b)

    print(f"El número random entre {a} y {b} = {numero_random}")

if __name__ == '__main__':
    main()