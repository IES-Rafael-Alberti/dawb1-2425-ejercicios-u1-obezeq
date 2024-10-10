import unittest
from src.extra01 import titular_v1, titular_v2, titular_v3

class TestFuncionTitular(unittest.TestCase):
    
    def test_titular_v1(self):
        self.assertEqual(titular_v1("hola mundo desde python"), "Hola Mundo Desde Python")
        self.assertEqual(titular_v1("   hola mundo desde python   "), "Hola Mundo Desde Python")
        self.assertEqual(titular_v1("    DIEGO es GeNiAl   "), "Diego Es Genial")
        self.assertEqual(titular_v1(""), "")
        
    def test_titular_v2(self):
        self.assertEqual(titular_v2("hola mundo desde python"), "Hola Mundo Desde Python")
        self.assertEqual(titular_v2("   hola mundo desde python   "), "Hola Mundo Desde Python")
        self.assertEqual(titular_v2("    DIEGO es GeNiAl   "), "Diego Es Genial")
        self.assertEqual(titular_v2("    DIEGO     es          GeNiAl   "), "Diego Es Genial")
        self.assertEqual(titular_v2(""), "")
        
    def test_titular_v3(self):
        self.assertEqual(titular_v3("hola mundo desde python"), "Hola Mundo Desde Python")
        self.assertEqual(titular_v3("   hola mundo desde python   "), "Hola Mundo Desde Python")
        self.assertEqual(titular_v3("    DIEGO es GeNiAl   "), "Diego Es Genial")
        self.assertEqual(titular_v3("    DIEGO     es          GeNiAl   "), "Diego Es Genial")
        self.assertEqual(titular_v3(""), "")
        
if __name__ == "__main__":
    unittest.main()