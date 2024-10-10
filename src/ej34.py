#!/usr/bin/env python3
# Mostrar todos los divisores de un número

def divisores(n):
    div = []
    for i in range(1,n+1):
        if n % i == 0:
            div.append(i)

    return div

def main():
    numero = int(input("Introduce un número: "))
    n_divisores = divisores(numero)
    if n_divisores == []:
        print(f"El número '{numero}', no tiene divisores.")
    else:
        print(f"El número '{numero}' tiene los siguientes divisores: ")
        for n in n_divisores:
            if n == numero:
                print(n, end=".")
            else:
                print(n, end=", ")

if __name__ == '__main__':
    main()