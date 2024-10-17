## **Ejercicios Extra - Unidad 1** (OPCIONALES)

### **1. Desarrolla un programa "ej00.py" que gestione un menú para ejecutar otros programas**

En este ejercicio, debes crear un programa principal llamado **"ej00.py"** que actúe como un menú para llamar a otros programas que estén ubicados en la carpeta **"src"**. El programa debe funcionar de la siguiente manera:

1. **Solicitar al usuario que introduzca el número del programa a ejecutar**.
   
2. **Validación del número del programa**:
   - Si introduce un número entre **1** y **30**, se mostrará el **título del programa** para indicar lo que hace, por ejemplo, "ej01: Saludo". Luego, debes preguntar si desea ejecutar el programa.
   - La respuesta afirmativa debe aceptar cualquiera de las siguientes variantes: **s, si, S, SI, y, YES, Y, yes** o combinaciones con espacios antes, después o entre letras. Si no desea ejecutarlo, el programa limpiará la consola y volverá a solicitar el número del programa.
   
3. **Errores y validaciones**:
   - Si el número introducido no corresponde con un programa válido (es decir, no está entre **1** y **30**), debes mostrar un mensaje de error: **"ERROR: Solo existen programas del 1 al 30"**.
   
4. **Al finalizar el programa seleccionado** (o después de mostrar el error), debe aparecer el mensaje **"Presiona ENTER para continuar..."**. Tras presionar **ENTER**, la pantalla debe limpiarse y el programa debe volver a solicitar el número del programa.
   
5. **Salir del menú**: El programa debe finalizar si el usuario introduce una cadena vacía o solo presiona **ENTER** sin introducir ningún número.

#### **Test Unitario**:

- Implementa **tests unitarios** para las funciones o módulos que desarrollemos en el programa. Los tests deben verificar que las funciones de validación de entrada y de ejecución de los programas funcionen correctamente.
- Utiliza el módulo **`unittest`** para crear estos tests.
- Asegúrate de probar casos válidos y casos que generen errores o mensajes de advertencia (por ejemplo, números fuera del rango permitido).

#### **Ejemplo de ejecución**:

```plaintext
Introduzca el número del programa: 55
> **ERROR** Solo existen programas del 1 al 30
> Presione ENTER para continuar...
```
(Si el usuario pulsa **ENTER**, la consola se limpia y vuelve a mostrar el mensaje inicial)

```plaintext
Introduzca el número del programa: 1
> ej01: Saludo
> ¿ejecutar? (sí o no) s
Escribe tu nombre: Manuel
Hola, Manuel.
> Presione ENTER para continuar...
```
(Si el usuario pulsa **ENTER**, la consola se limpia y vuelve a mostrar el mensaje inicial)

---

### **2. Desarrolla un programa "extra01.py" que incluya la función "titular()"**

En este ejercicio, debes crear un programa llamado **"extra01.py"** que incluya una función **`titular(frase)`**. Esta función recibe una frase como parámetro y devuelve esa frase con las **palabras capitalizadas** y **sin espacios** antes de la primera palabra o después de la última, si los hubiera.

#### Restricciones:
- No puedes usar las funciones predefinidas **`str.title()`** ni **`str.capitalize()`**.

#### Requisitos:
- Debes implementar tres versiones diferentes de la función **`titular()`** de la siguiente manera:

1. **`titular_v1(frase)`**: 
   - Debe realizarse **solo usando un bucle**, sin convertir la frase en una lista de palabras.

2. **`titular_v2(frase)`**: 
   - Debe utilizar una **lista**, pero no puedes modificar los elementos de la lista directamente.

3. **`titular_v3(frase)`**: 
   - Debes usar una **lista** y modificar directamente sus elementos (convertir cada palabra a su versión capitalizada dentro de la lista).

#### **Test Unitario**:

- Implementa **tests unitarios** para cada versión de la función **`titular()`** (`titular_v1()`, `titular_v2()`, y `titular_v3()`).
- Verifica que las funciones capitalicen correctamente las palabras y eliminen los espacios innecesarios al principio y al final de la frase.
- Prueba diferentes casos, como frases que ya están correctamente capitalizadas, frases en minúsculas y frases con espacios al inicio y final.

#### Ejemplo:
Si la frase introducida es:  
```plaintext
"   hola mundo desde python   "
```
Las tres versiones de la función deben devolver:  
```plaintext
"Hola Mundo Desde Python"
```

---

### **3. Control de errores en tiempo de ejecución sin usar try-except**

En este ejercicio debes desarrollar una estrategia para **controlar posibles errores** en tiempo de ejecución en todos los programas que hayas desarrollado en la Unidad 1, **sin utilizar la estructura try-except**.

#### Requisitos:
- Deberás **prevenir errores** de entrada del usuario (como valores no numéricos donde se esperan números) utilizando técnicas de validación antes de la conversión de los datos.
- Intenta modularizar tu código para evitar repetir las mismas validaciones en diferentes partes del programa. Esto te permitirá reutilizar el mismo código para validar diferentes entradas del usuario en distintos programas.

#### Sugerencias:
- Utiliza funciones auxiliares para validar entradas antes de realizar operaciones. Por ejemplo, puedes crear una función para validar si una cadena representa un número entero o flotante, y usarla en varios programas.

---

### **Objetivo general de los ejercicios:**
- Practicar la programación estructurada y modular en Python.
- Implementar técnicas de validación de entrada.
- Desarrollar control de errores sin la ayuda de `try-except`.
- Trabajar con manipulación de cadenas y listas en Python.
- Desarrollar **tests unitarios** para garantizar el correcto funcionamiento de las funciones desarrolladas.

---

### **Entrega**:
- Todos los programas deben estar correctamente indentados y documentados.
- Guarda los archivos en la carpeta llamada **`src`**.
- Asegúrate de probar todas las funcionalidades antes de la entrega, incluyendo la ejecución de los **tests unitarios**.
