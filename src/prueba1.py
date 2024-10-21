#!/usr/bin/env python3

def mayor(a: int, b: int):
    if a == b:
        return 0
    else:
        return a if a > b else b
    
def main():
    mayor(1, 3)

if __name__ == '__main__':
    main()