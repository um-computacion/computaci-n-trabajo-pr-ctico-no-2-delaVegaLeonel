import unittest 
from palindromo import palindromes 
from palindromo import obtener_cantidad_de_palabras_palindromes


class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        input = "a"
        result = palindromes(input)
        self.assertTrue(result)


    def test_with_ala(self):
        input = "ala"
        result = palindromes(input)
        self.assertTrue(result)


    def test_with_neuquen(self):
        input = "neuquen"
        result = palindromes(input)
        self.assertTrue(result)


    def test_with_hola(self):
        input = "hola"
        result = palindromes(input)
        self.assertFalse(result)


    def test_with_mixed_case(self):
        self.assertFalse(palindromes("Ala"))
    
    def test_with_mixed_case(self):
        input = "NeuQueN"
        result = palindromes(input)
        self.assertTrue(result)

class TestCantidadDePalabrasPalindromes(unittest.TestCase):
    def test_cantidad_de_palabras_palindromes_simple(self):
        palabras = ["ala"]
        resultado = obtener_cantidad_de_palabras_palindromes(palabras)
        self.assertEqual(resultado, 1)

    def test_cantidad_de_palabras_palindromes_con_2(self):
        palabras = ["ala", "neuquen"]
        resultado = obtener_cantidad_de_palabras_palindromes(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_3(self):
        palabras = ["ala", "neuquen", "hola"]
        resultado = obtener_cantidad_de_palabras_palindromes(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_4(self):
        palabras = ["ala", "neuquen", "hola", "programacion"]
        resultado = obtener_cantidad_de_palabras_palindromes(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_5(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap"]
        resultado = obtener_cantidad_de_palabras_palindromes(palabras)
        self.assertEqual(resultado, 3)

    def test_cantidad_de_palabras_palindromes_complejo(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]
        resultado = obtener_cantidad_de_palabras_palindromes(palabras)
        self.assertEqual(resultado, 3)
        

    def test_cantidad_de_palabras_palindromes_complejo_2(self):
        palabras = [
            "ala",
            "neuquen",
            "hola",
            "programacion",
            "palap",
            "neu  quen",
            "agita falsos usos la fatiga",
            "presidente de la camara de diputados: martin menem",
			"A man, a plan, a canal - Panama"
        ]
        resultado = obtener_cantidad_de_palabras_palindromes(palabras)
        self.assertEqual(resultado, 6)

if __name__ == "__main__":
    unittest.main()
