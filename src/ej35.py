#!/usr/bin/env python3
# Calcular la serie de Fibonacci hasta un número dado

import argparse

def check_args():
    parser = argparse.ArgumentParser(
        description="Just a fibonnaci Sequence"
    )
    parser.add_argument('-i', '--illustrated', action='store_true', help='Enable Fibonnaci Sequence Illustration')
    return parser.parse_args()

def fibonnaci_sequence(n: int) -> list:
    if n == 1:
        fibonnaci = [1]
    elif n == 2:
        fibonnaci = [1, 1]
    else:
        fibonnaci = [1, 1]
        for i in range(2, n):
            next_n = fibonnaci[-1] + fibonnaci[-2]
            fibonnaci.append(next_n)
            
    return fibonnaci

def fibonnaci_ilustration(sequence: list):
    for i in sequence:
        print(f"{i}: " + "█" * i)

def check_input(n: str):
    try:
        if float(n) < 0:
            return ValueError
        if float(n).is_integer():
            return int(n)
        else:
            return TypeError
    except ValueError:
        return ValueError

def main():
    n = input("Introduce la cantidad de veces máxima para la serie fibonnaci: ")
    
    n = check_input(n)
    if n == ValueError:
        print(f"ERROR: No has introducido un número correcto.")
    elif n == TypeError:
        print(f"ERROR: La secuencia fibonnaci tiene que tener como entrada un número entero.")
    elif n == 0:
        print(f"ERROR: La secuencia fibonnaci tiene que ser mayor a 0.")
    else:
        sequence = fibonnaci_sequence(n)
        args = check_args()
        if args.illustrated:
            fibonnaci_ilustration(sequence)
        else:
            for n in sequence:
                if n == sequence[-1]:
                    print(n, end=".")
                else:
                    print(n, end=", ")

if __name__ == '__main__':
    main()