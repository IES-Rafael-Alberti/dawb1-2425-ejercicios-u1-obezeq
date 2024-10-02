#!/usr/bin/env python3

import os
import time

funciones_programa = {
    "01": "Saludo",
    "02": "Calculadora coste por hora de trabajo",
    "03": "Calculadora ancho / alto",
    "04": "Conversor celsius > fahrenheit",
    "05": "Calculador precio con IVA",
    "06": "Calculador precio con IVA 10%",
    "07": "Suma de 3 numeros",
    "08": "Suma de 3 numeros",
    "09": "Suma de 3 numeros",
    "10": "Suma ((3+2)/(2*5))**2",
    "11": "Suma (n*(n+1))/2",
    "12": "Calculadora índice de masa corporal",
    "13": "División entre 2 números",
    "14": "Calculadora peso total del paquete",
    "15": "Intereses en tu cuenta de ahorro",
    "16": "Calcuradora barras de pan",
    "17": "Imprimir nombre de usuario n veces",
    "18": "Conversor de nombre y apellidos",
    "19": "Calculador de letras en un nombre de usuario",
    "20": "Comprobador de número de teléfono",
    "21": "Frase inversa",
    "22": "Frase y vocal",
    "23": "Comprobador de correo electrónico en formato correcto",
    "24": "Calcular euros y centimos de un precio",
    "25": "Conversor de fecha a Día / Mes / Año",
    "26": "Lista de la compra",
    "27": "Conversor de euros y centimos",
    "28": "Identificar el número menor y número mayor",
    "29": "¿Cuantos años te quedan por cumplir hasta 125 años?",
    "30": "Número - Incremento - Serie "
}

def ejecucion_programa():
    try:
        while True:
            if num == '':
                os._exit(0)

            # ERROR POR NO EJECUTAR UN PROGRAMA CORRECTO
            elif int(num) < 1 or int(num) > 30:
                print("> ERROR: Solo existen programas del 1 al 30")

            # PROGRAMA CORRECTO INTRODUCIDO
            else:
                num = int(num)
                if num >= 1 and num < 10:
                    num = f"0{num}"
                else:
                    num = str(num)            

                funcion = funciones_programa[num]
                os.system(f'title ej{num}: {funcion}')

                opcion = input("Deseas ejecutar el programa (Y/n): ").lower().replace(' ', '')
                if opcion == "y" or opcion == "yes" or opcion == "s" or opcion == "si":
                    print(f"Ejecutando programa ej{num}.py ...\n")
                    time.sleep(1)
                    dirname_path = os.path.dirname(__file__)
                    if os.name == 'nt':
                        program_dirname = f'{dirname_path}\\ej{num}.py'
                    else:
                        program_dirname = f'{dirname_path}/ej{num.py}'
                    
                    os.system(f"python {program_dirname}")
                    input("\n> Presiona ENTER para continuar...")
                    os.system('cls') if os.name == 'nt' else os.system('clear')
                    
                else:
                    os.system('cls') if os.name == 'nt' else os.system('clear')

    except ValueError:
        print("ERROR: No has introducido un número!")

def main():
    ejecucion_programa()

if __name__ == '__main__':
    main()