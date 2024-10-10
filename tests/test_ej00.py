#!/usr/bin/env python3
import unittest
from unittest.mock import patch, mock_open, MagicMock
import subprocess
import os
import sys
from src.ej00 import (
    limpiar_consola,
    welcome,
    validacion_entrada,
    titulo_programa,
    validar_opcion_ejecutar,
    convertir_numero_programa,
    ejecutar_programa,
)

class TestEj00(unittest.TestCase):
    
    # TESTING DE EFECTO TYPE
    @patch('os.system')
    def test_limpiar_consola(self, mock_system):
        limpiar_consola()
        # SE ASEGURA QUE SE LLAME A 'os.system' AL MENOS UNA VEZ
        mock_system.assert_called_once()
        
    # TEST WELCOME (SATISFACTORIO)
    @patch('builtins.open', new_callable=mock_open, read_data='Banner')
    def test_welcome(self, mock_open):
        resultado = welcome()
        self.assertTrue(resultado)
        mock_open.assert_called_once_with("banner.txt", 'r')
    
    # TEST WELCOME (ERROR: ARCHIVO NO ENCONTRADO)
    def test_welcome_archivo_no_encontrado(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            result = welcome()
            self.assertIsInstance(result, FileNotFoundError)
            
    # TEST VALIDACION ENTRADA
    def test_validacion_entrada(self):
        self.assertEqual(validacion_entrada("5"), "05") # VALIDO
        self.assertEqual(validacion_entrada("0"), None) # ERROR porque tiene que ser > 0
        self.assertEqual(validacion_entrada("35"), None) # ERROR porque tiene que ser < 30
        self.assertEqual(validacion_entrada("texto"), -1) # ERROR porque no es un número
        self.assertEqual(validacion_entrada(""), -2) # USUARIO DECIDE SALIR
    
    # TEST CAMBIAR TITULO PROGRAMA (SATISFACTORIO)
    @patch('os.system')
    def test_titulo_programa(self, mock_system):
        resultado = titulo_programa("01", {"01": "Saludo"})
        self.assertTrue(resultado)
        mock_system.assert_called_once()
    
    # TEST CAMBIAR TITULO PROGRAMA (CON ERROR)
    @patch('os.system', side_effect=Exception)
    def test_titulo_programa_error(self, mock_system):
        with self.assertRaises(SystemError):
            titulo_programa("01", {"01": "Error Testeo"})
            
    # TEST CAMBIAR TITULO PROGRAMA (CON ERROR "KeyError")
    @patch('os.system', side_effect=Exception)
    def test_titulo_programa_error_key_error(self, mock_system):
        with self.assertRaises(KeyError):
            titulo_programa("33", {"01": "Error Testeo"})
            
    # TEST VALIDAR OPCION EJECUTAR
    def test_validar_opcion_ejecutar(self):
        self.assertEqual(validar_opcion_ejecutar("s"), 1) # EL USUARIO QUIERE EJECUTAR
        self.assertEqual(validar_opcion_ejecutar("si"), 1) # EL USUARIO QUIERE EJECUTAR
        self.assertEqual(validar_opcion_ejecutar("y"), 1) # EL USUARIO QUIERE EJECUTAR
        self.assertEqual(validar_opcion_ejecutar("YeAh"), 1) # EL USUARIO QUIERE EJECUTAR
        self.assertEqual(validar_opcion_ejecutar("YeS"), 1) # EL USUARIO QUIERE EJECUTAR
        self.assertEqual(validar_opcion_ejecutar("n"), -1) # EL USUARIO NO QUIERE EJECUTAR
        self.assertEqual(validar_opcion_ejecutar("No   "), -1) # EL USUARIO NO QUIERE EJECUTAR
        self.assertEqual(validar_opcion_ejecutar("Diego"), 0) # OPCIÓN NO VÁLIDA
        self.assertEqual(validar_opcion_ejecutar(""), 0) # OPCIÓN NO VÁLIDA
        
    # TEST CONVERTIR NUMERO PROGRAMA
    @patch('os.path.isfile', return_value=True)
    @patch('os.path.join', return_value='ej01.py')
    def test_convertir_numero_programa(self, mock_join, mock_isfile):
        resultado = convertir_numero_programa("01", None)
        self.assertEqual(resultado, 'ej01.py')
        
    # TEST CONVERTIR NUMERO PROGRAMA (ERROR ARCHIVO NO ENCONTRADO)
    @patch('os.path.isfile', return_value=False)
    def test_convertir_numero_programa_file_not_found(self, mock_isfile):
        resultado = convertir_numero_programa("01", None)
        self.assertIsInstance(resultado, FileNotFoundError)
        
    # TEST EJECUTAR PROGRAMA (SATISFACTORIO)
    @patch('subprocess.run')
    @patch('os.path.isfile', return_value=True)
    def test_ejecutar_programa(self, mock_isfile, mock_run):
        resultado = ejecutar_programa('ej01.py')
        self.assertTrue(resultado)
        
    # TEST EJECUTAR PROGRAMA (ERROR)
    @patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'ej01.py'))
    @patch('os.path.isfile', return_value=True)
    def test_ejecutar_programa_error(self, mock_isfile, mock_run):
        resultado = ejecutar_programa('ej01.py')
        self.assertIsInstance(resultado, RuntimeError)
    
if __name__ == '__main__':
    unittest.main()