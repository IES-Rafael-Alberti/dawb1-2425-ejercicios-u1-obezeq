#!/usr/bin/env python3
# Escribir un programa que determine si un número es primo

def primo(n: int) -> int:
    primo = True

    if n >= 0 and n <= 1:
        primo = False
    else:
        for i in range(2,n):
            if n % i == 0:
                primo = False

    return primo

def main():
    n = int(input("Introduce un número: "))
    es_primo = primo(n)
    if es_primo:
        print(f"El número {n} es primo.")
    else:
        print(f"El número {n} no es primo.")

if __name__ == '__main__':
    main()