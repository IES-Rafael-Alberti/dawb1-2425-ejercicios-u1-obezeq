#!/usr/bin/env python3
# Calcular la serie de Fibonacci hasta un número dado

def secuencia_fibonnaci(n):
    fibonnaci = [1,1]
    counter = 2
    while counter < 8:

        if fibonnaci 

        if len(fibonnaci) >= 2:
            left = fibonnaci[counter-1]
            right = fibonnaci[counter-2]
            next_n = left + right
            fibonnaci.append(next_n)

        counter += 1

    return fibonnaci

def main():
    n = int(input("Introduce un número: "))
    print(secuencia_fibonnaci(n))

if __name__ == '__main__':
    main()