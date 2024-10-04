#!/usr/bin/env python3

# Dependencies
import os
import time
import sys
import subprocess

# CLASE DE COLORES
class Colors:
    """Codigos de color ANSI"""
    WHITE = "\033[1;37m"
    GREEN = "\033[1;32m"
    RED = "\033[0;31m"
    UNDERLINE = "\033[4m"
    ITALIC  = "\033[3m"
    END = "\033[0m"
    NEGATIVE = "\033[7m"

# FUNCION PARA EFECTO TYPING
def efecto_type(texto, delay=0.069):
    try:
        for c in texto:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(delay)
    except TypeError:
        return TypeError("En la función 'efecto_type' no se ha proporcionado una entrada tipo 'string'")

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
        print(f"{Colors.END}{Colors.RED}[-] ERROR AL LIMPIAR LA CONSOLA{Colors.END}")
        os._exit(0) # ABORTAR EL PROGRAMA DEBIDO AL ERROR

# PANTALLA WELCOME
def welcome():
    try:
        with open("banner.txt", 'r') as f:
            ejecutar_limpiar_consola()
            banner = f.read()
            print(f"{Colors.END}{Colors.GREEN}{banner}{Colors.WHITE}")
            f.close()
            os.system('title MENU EJ01-EJ30') if os.name == 'nt' else os.system('echo -ne "\033]0;MENU EJ01-EJ30\007"')
        return True
    except FileNotFoundError:
        return FileNotFoundError(f"{Colors.RED}[-] ERROR: Necesitas el archivo 'banner.txt'{Colors.WHITE}")

# ARRAY DE FUNCIONES DE CADA PROGRAMA
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
def validacion_entrada(num: str):
    # La entrada se da en un formato STRING por le usuario, al ser introducida desde un INPUT
    num = num.replace(' ', '')
    
    # COMPROBAR SI SE HA INTRODUCIDO UN NÚMERO
    if num.isdigit():
        if int(num) < 1 or int(num) > 30:
            return None # NO SE HA INTRODUCIDO UN PROGRAMA VALIDO
        else:
            if int(num) > 0 and int(num) < 10:
                numero_programa = f"0{int(num)}"
            else:
                numero_programa = num
                
            return numero_programa
        
    # NO SE HA INTRODUCIDO UN NÚMERO
    else:
        if num == '':
            return -2 # SALIR DEL PROGRAMA
        else:
            return -1 # NO SE HA INTRODUCIDO UN NÚMERO

# FUNCION TITULO PROGRAMA
def titulo_programa(num, funciones_programa):
    num = str(num)
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
    if opcion == "y" or opcion == "yes" or opcion == "s" or opcion == "si" or opcion == "claro" or opcion == "yeah" or opcion == "sip" or opcion == "yep":
        return 1 # EL USUARIO QUIERE EJECUTAR EL PROGRAMA
    elif opcion == "n" or opcion == "no":
        return -1 # EL USUARIO NO QUIERE EJECUTAR EL PROGRAMA
    else:
        return 0 # NO HA INTRODUCIDO UNA OPCIÓN VÁLIDA

# FUNCION PARA CONVERTIR NUMERO DE PROGRAMA A NOMBRE PROGRAMA
def convertir_numero_programa(num, base_path):
    try:
        nombre_programa = f"ej{num}.py"

        # OBTENER EL DIRECTORIO ACTUAL Y DEL ARCHIVO A EJECUTAR
        if base_path is None:
            dirname_path = os.path.dirname(__file__)
        else:
            dirname_path = base_path

        # COMPROBAR QUE EL ARCHIVO EXISTE
        program_path = os.path.join(dirname_path, nombre_programa)
        if not os.path.isfile(program_path):
            return FileNotFoundError(f"El archivo '{nombre_programa}' no se encuentra en el directorio '{dirname_path}'.")
        else:
            return program_path
    
    except Exception as e:
        return Exception(f"Se ha producido un ERROR desconocido:\n{e}")

# FUNCION EJECUTAR PROGRAMA
def ejecutar_programa(program_dirname):
    comandos = [
        ['python', program_dirname],
        ['python3', program_dirname],
        ['py', program_dirname]
    ]
    
    if not os.path.isfile(program_dirname):
        return FileNotFoundError("No se ha encontrado el directorio del programa\n")
    else:
        for comando in comandos:
            try:
                subprocess.run(comando, check=True)
                return True # EL PROGRAMA FUE EJECUTADO SATISFACTORIAMENTE
            
            except FileNotFoundError:
                # SI EL COMANDO NO ES ENCONTRADO, PASA AL SIGUIENTE COMANDO
                continue
            
            except subprocess.CalledProcessError as e:
                # ERROR MIENTRAS SE EJECUTABA EL PROGRAMA
                return RuntimeError(f"ERROR mientras se ejecutaba el programa:\n{e}\n\nCon el siguiente estado de salida:\n{e.returncode}\n")

def main():

    # BUCLE DEL PROGRAMA
    while True:
        welcome_status = welcome()
        if isinstance(welcome_status, FileNotFoundError):
            print(welcome_status)
            os._exit(0)
        elif welcome_status:
            program_choice = input(f"{Colors.GREEN}[+]{Colors.WHITE} {Colors.UNDERLINE}Introduce el número del programa que desees ejecutar:{Colors.END} {Colors.ITALIC}")

        # VALIDAR QUE SE HA INTRODUCIDO UN NÚMERO DE PROGRAMA CORRECTO
        validacion_numero = validacion_entrada(program_choice)
        
        if validacion_numero == -2:
            status_efecto_typeo = efecto_type(f"\n{Colors.END}{Colors.GREEN}{Colors.NEGATIVE}¡Hasta la próxima!{Colors.END}\n\n")
            if isinstance(status_efecto_typeo, TypeError):
                print(f"{Colors.END}{Colors.RED}[-] ERROR: {status_efecto_typeo}{Colors.UNDERLINE}{Colors.END}")
            os._exit(0)
        
        # ✗ NO SE HA INTRODUCIDO UN NÚMERO DE PROGRAMA CORRECTO
        elif validacion_numero == -1:
            ejecutar_limpiar_consola()
            print(f"{Colors.END}{Colors.RED}[-] ERROR: {Colors.UNDERLINE}No has introducido un número de programa correcto{Colors.END}\n")
        
        # ✗ LIMPIAR CONSOLA Y MOSTRAR ERROR QUE SOLO EXISTEN PROGRAMAS DEL 1 AL 30 Y LIMPIAR LA CONSOLA
        elif validacion_numero == None:
            ejecutar_limpiar_consola()
            print(f"{Colors.END}{Colors.RED}[-] ERROR: {Colors.UNDERLINE}Solo existen programas del 1 al 30{Colors.END}\n")

        # ✓ ENTRADA VALIDA
        else:
            numero_programa = validacion_numero
            ejecucion_titulo = titulo_programa(numero_programa, funciones_programa)

            # ✗ ERROR AL LIMPIAR TITULO
            if ejecucion_titulo == SystemError:
                os._exit(0) # SALIR DEL PROGRAMA PORQUE HA HABIDO UN ERROR AL CAMBIAR EL TITULO

            # ✓ TITULO LIMPIADO CORRECTAMENTEE
            else:
                opcion_ejecutar = input(f"{Colors.END}{Colors.GREEN}[+] {Colors.WHITE}{Colors.UNDERLINE}¿Desea ejecutar el programa ej{numero_programa}.py?:{Colors.END}{Colors.WHITE}{Colors.ITALIC} ")
                validacion_opcion_ejecutar = validar_opcion_ejecutar(opcion_ejecutar)

                # EJECUTAR PROGRAMA
                if validacion_opcion_ejecutar == 1:
                    programa_dirname = convertir_numero_programa(numero_programa, None)
                        
                    # ✗ ERROR ARCHIVO NO ENCONTRADO
                    if isinstance(programa_dirname, FileNotFoundError):
                        print(f"{Colors.END}{Colors.RED}[-] ERROR 'FileNotFoundError':\n{programa_dirname}{Colors.END}")
                        os._exit(0)
                        
                    # ✗ ERROR DESCONOCIDO
                    elif isinstance(programa_dirname, Exception):
                        print(f"{Colors.END}{Colors.RED}[-] ERROR: {programa_dirname}{Colors.END}")
                        os._exit(0)

                    # ✓ ARCHIVO ENCONTRADO => PROCEDER A EJECUTAR EL PROGRAMMA
                    else:
                        print(f"\n{Colors.END}─────────────────────────────────\n")
                        status_ejecucion = ejecutar_programa(programa_dirname)
                        
                        # PROGRAMA EJECUTADO SATISFACTORIAMENTE
                        if status_ejecucion != True:
                            if isinstance(status_ejecucion, RuntimeError):
                                print(f"{Colors.END}{Colors.RED}[-] ERROR: {status_ejecucion}{Colors.END}")
                            elif isinstance(status_ejecucion, FileNotFoundError):
                                print(f"{Colors.END}{Colors.RED}[-] ERROR: {status_ejecucion}{Colors.END}")
                        
                        # CONTINUAR
                        print("\n─────────────────────────────────\n")
                        input(f"{Colors.GREEN}[+] {Colors.NEGATIVE}ej{numero_programa}.py{Colors.END} {Colors.WHITE}ha sido ejecutado satisfactoriamente. {Colors.ITALIC}Presiona ENTER para continuar...{Colors.END}")
                        
                        # LIMPIAR CONSOLA
                        ejecutar_limpiar_consola()

                # ✗ EL USUARIO NO QUIERE EJECUTAR EL PROGRAMA
                elif validacion_opcion_ejecutar == -1:
                    ejecutar_limpiar_consola()
                
                # ✗ EL USUARIO NO HA INTRODUCIDO UNA OPCIÓN
                elif validacion_opcion_ejecutar == 0:
                    print(f"\n{Colors.END}{Colors.RED}[-] ERROR: NO TE HE ENTENDIDO. (La próxima vez diga si quiere ejecutar o no){Colors.WHITE}\n")
                    input("Presiona ENTER para reiniciar")

if __name__ == '__main__':
    main()