#!/usr/bin/env python3

def checker(n):
    if n >= 0:
        suma = (n*(n+1))/2
        return f"({n}*({n}+1))/2 = {suma}"
    else:
        return "ERROR: El número es negativo."