import unittest
from src.utilitarios_analise_texto import UtilitariosAnaliseTexto

class TestUtilitariosAnaliseTexto(unittest.TestCase):

    def setUp(self):
        self.util = UtilitariosAnaliseTexto("A man a plan a canal Panama. Hello world! Teste.")

    def test_frequencia_palavras(self):
        self.assertEqual(self.util.frequencia_palavras(), {'a': 3, 'man': 1, 'plan': 1, 'canal': 1, 'panama.': 1, 'hello': 1, 'world!': 1, 'teste.': 1})

    def test_encontrar_frases_palindromas(self):
        self.assertEqual(self.util.encontrar_frases_palindromas(), ['A man a plan a canal Panama'])

    def test_grupos_anagramas(self):
        lista_palavras = ["listen", "silent", "enlist", "google", "gogole"]
        self.assertEqual(self.util.grupos_anagramas(lista_palavras), [['listen', 'silent', 'enlist'], ['google', 'gogole']])

    def test_prefixo_comum(self):
        lista_palavras = ["prefixo", "preferencia", "preliminar"]
        self.assertEqual(self.util.prefixo_comum(lista_palavras), "pre")

    def test_detectar_palavras_chave(self):
        self.assertEqual(self.util.detectar_palavras_chave(), {'man': 1, 'plan': 1, 'canal': 1, 'panama': 1, 'hello': 1, 'world': 1, 'teste': 1})

    def test_contar_frases(self):
        self.assertEqual(self.util.contar_frases(), 3)

    def test_palavras_unicas_ordenadas(self):
        self.assertEqual(self.util.palavras_unicas_ordenadas(), ['a', 'canal', 'hello', 'man', 'panama', 'plan', 'teste', 'world'])

    def test_fatores_primos(self):
        self.assertEqual(self.util.fatores_primos(28), [2, 2, 7])

if __name__ == '__main__':
    unittest.main()
