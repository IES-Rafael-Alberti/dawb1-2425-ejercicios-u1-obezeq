#!/usr/bin/env python3

import os
import time
import subprocess

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

# FUNCION PARA VALIDAD LA ENTRADA PARA EL EJERCICIO CORRECTO
def validacion_entrada(num):
    # La entrada se da en un formato STRING por le usuario, al ser introducida desde un INPUT
    num = num.replace(' ', '')

    if num == '':
        return -1 # RETORNA -1 PARA LUEGO SALIR DEL PROGRAMA con os._exit(0)
    elif int(num) < 1 or int(num) > 30:
        return None # > ERROR: Solo existen programas del 1 al 30
    else:
        return int(num) # RETORNA EL NUMERO DEL PROGRAMA AL SER CORRECTO Y VÁLIDO

# FUNCION PARA LIMPIAR LA CONSOLA
def limpiar_consola():
    try:
        os.system('cls') if os.name == 'nt' else os.system('clear')
        return True
    except:
        return SystemError

# EJECUTAR LIMPIAR_CONSOLA
def ejecutar_limpiar_consola():
    try:
        limpiar_consola()
    except SystemError:
        print("[-] ERROR AL LIMPIAR LA CONSOLA")
        os._exit(0) # ABORTAR EL PROGRAMA DEBIDO AL ERROR

# FUNCION TITULO PROGRAMA
def titulo_programa(num, funciones_programa):
    funcion = funciones_programa[num]
    try:
        os.system(f'title ej{num}: {funcion}') if os.name == 'nt' else os.system(f'echo -ne "\033]0;ej{num}: {funcion}\007"') 
        return True
    except:
        print(f"ERROR: NO SE PUEDE PONER TITULO ej{num}.py")
        return SystemError

# FUNCION PREGUNTA SI DESEA EJECUTAR PROGRAMA DE NUEVO O NO
def validar_opcion_ejecutar(opcion):
    opcion = opcion.lower().replace(' ', '')
    if opcion == "y" or opcion == "yes" or opcion == "s" or opcion == "si":
        return True
    elif opcion == "n" or opcion == "no":
        return False
    else:
        return -1

# FUNCION PARA CONVERTIR NUMERO DE PROGRAMA A NOMBRE PROGRAMA
def convertir_numero_programa(num):
    try:
        num = int(num)
        if num >= 1 and num < 10:
            nombre_programa = f"ej0{num}.py"
        else:
            nombre_programa = f"ej{num}.py"

        # OBTENER EL DIRECTORIO ACTUAL Y DEL ARCHIVO A EJECUTAR
        dirname_path = os.path.dirname(__file__)

        # COMPROBAR QUE EL ARCHIVO EXISTE
        os.path.isfile(dirname_path)

        return f'{dirname_path}\\{nombre_programa}' if os.name == 'nt' else f'{dirname_path}/{nombre_programa}
    except:
        return FileNotFoundError


# FUNCION EJECUTAR PROGRAMA
def ejecutar_programa(program_dirname):
    try:
        subprocess.run(['python3', {program_dirname}])
        return True
    except:
        try:
            subprocess.run(['python', {program_dirname}])
            return True
        except:
            try:
                subprocess.run(['py', {program_dirname}])
                return True
            except:
                print("ERROR: NO SE HA PODIDO EJECUTAR EL PROGRAMA")
                return RuntimeError


def hola():
    print("hola")

def ejecucion_programa():
    """
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
                        program_dirname = f'{dirname_path}/ej{num}.py'
                    
                    os.system(f"python {program_dirname}")
                    input("\n> Presiona ENTER para continuar...")
                    limpiar_consola()
                    
                else:
                    limpiar_consola()

    except ValueError:
        print("ERROR: No has introducido un número!")
    """

def main():

    # BUCLE DEL PROGRAMA
    while True:
        program_choice = input("[+] Introduce el número del programa que desees ejecutar: ")

        # VALIDAR QUE SE HA INTRODUCIDO UN NÚMERO DE PROGRAMA CORRECTO
        validacion_numero = validacion_entrada()
        if validacion_entrada == -1:
            os._exit(0) # SALIR DEL PROGRAMA
        
        # LIMPIAR CONSOLA Y MOSTRAR ERROR QUE SOLO EXISTEN PROGRAMAS DEL 1 AL 30 Y LIMPIAR LA CONSOLA
        elif None:
            ejecutar_limpiar_consola()
            
            print("[-] ERROR: Solo existen programas del 1 al 30\n")

        # ENTRADA VALIDA
        else:
            numero_programa = validacion_numero
            ejecucion_titulo = titulo_programa(numero_programa, funciones_programa)

            # ERROR AL LIMPIAR TITULO
            if ejecucion_titulo == SystemError:
                os._exit(0) # SALIR DEL PROGRAMA PORQUE HA HABIDO UN ERROR AL CAMBIAR EL TITULO

            # TITULO LIMPIADO CORRECTAMENTEE
            else:
                opcion_ejecutar = input(f"¿Desea ejecutar el programa ej{numero_programa}.py?")
                validacion_opcion_ejecutar = validar_opcion_ejecutar(opcion_ejecutar)

                # EJECUTAR PROGRAMA
                if validacion_opcion_ejecutar:
                    programa_dirname = convertir_numero_programa(numero_programa)

                    # ERROR ARCHIVO NO ENCONTRADO
                    if programa_dirname == FileNotFoundError:
                        print("[-] ERROR: No se ha podido encontrar el archivo")
                        os._exit(0)

                    # ARCHIVO ENCONTRADO => PROCEDER A EJECUTAR EL PROGRAMMA
                    else:
                        print()

                # EL USUARIO NO HA INTRODUCIDO UNA OPCIÓN VÁLIDA
                elif validacion_opcion_ejecutar == False:
                    ejecutar_limpiar_consola()
                
                # EL USUARIO NO HA INTRODUCIDO UNA OPCIÓN
                elif validacion_opcion_ejecutar == -1:
                    print("[-] ERROR: NO HAS INTRODUCIDO UNA OPCIÓN VÁLIDA. Saliendo del programa...")
                    os._exit(0)

if __name__ == '__main__':
    main()