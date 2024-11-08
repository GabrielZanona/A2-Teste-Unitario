import re
from collections import Counter, defaultdict

class UtilitariosAnaliseTexto:
    def __init__(self, texto=""):
        self.texto = texto

    def frequencia_palavras(self):
        palavras = self.texto.lower().split()
        return dict(Counter(palavras))

    def encontrar_frases_palindromas(self):
        frases = re.split(r'[.!?]', self.texto)
        palindromas = []
        for frase in frases:
            frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()
            if frase_limpa == frase_limpa[::-1] and frase_limpa:
                palindromas.append(frase.strip())
        return palindromas

    def grupos_anagramas(self, lista_palavras):
        dicionario_anagramas = defaultdict(list)
        for palavra in lista_palavras:
            palavra_ordenada = ''.join(sorted(palavra.lower()))
            dicionario_anagramas[palavra_ordenada].append(palavra)
        return list(dicionario_anagramas.values())

    def prefixo_comum(self, lista_palavras):
        if not lista_palavras:
            return ""
        prefixo = lista_palavras[0]
        for palavra in lista_palavras[1:]:
            while not palavra.startswith(prefixo) and prefixo:
                prefixo = prefixo[:-1]
        return prefixo

    def detectar_palavras_chave(self, palavras_comuns=None):
        if palavras_comuns is None:
            palavras_comuns = {"de", "a", "o", "e", "do", "da"}
        palavras = [palavra.lower() for palavra in re.findall(r'\b\w+\b', self.texto) if
                    palavra.lower() not in palavras_comuns]
        return dict(Counter(palavras))

    def contar_frases(self):
        frases = re.split(r'[.!?]', self.texto)
        return len([frase for frase in frases if frase.strip()])

    def fatores_primos(self, numero):
        if numero <= 1:
            return []
        fatores = []
        divisor = 2
        while numero > 1:
            while numero % divisor == 0:
                fatores.append(divisor)
                numero //= divisor
            divisor += 1
        return fatores

    def palavras_unicas_ordenadas(self):
        palavras = set(re.findall(r'\b\w+\b', self.texto.lower()))
        return sorted(palavras)
