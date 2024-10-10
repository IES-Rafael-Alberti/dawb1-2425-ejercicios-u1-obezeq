#!/usr/bin/env python3

def grados_celsius(fahrenheit: float):
    
    celsius = fahrenheit / 33.8
    celsius = round(celsius, 2)
    
    return celsius

def main():
    grados_celsius(33.8)

if __name__ == '__main__':
    main()