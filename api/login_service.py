# -*- coding: utf-8 -*-
import re


class Autenticacao:
    def aplicar_regras(self, senha):

        tamanho_valido = self.tamanho_valido(senha)
        tem_caracters_especiais = self.tem_caracteres_especiais(senha)
        tem_letra_minuscula = self.tem_letra_minuscula(senha)
        tem_letra_maiuscula = self.tem_letra_maiuscula(senha)
        tem_numero = self.tem_numero(senha)
        tem_caracters_repetidos = self.tem_caracteres_repetidos(senha)
        resposta = (
            tamanho_valido
            and tem_numero
            and tem_caracters_especiais
            and tem_letra_maiuscula
            and tem_letra_minuscula
            and tem_caracters_repetidos
        )

        return resposta

    def tem_caracteres_especiais(self, senha):

        caracters_especiais = "!@#$%^&*()-+"
        return any(caracters in caracters_especiais for caracters in senha)

    def tamanho_valido(self, senha):
        return len(senha) > 8

    def tem_numero(self, senha):
        numero = re.search(r'{\d}', senha) is None
        return numero

    def tem_letra_minuscula(self, senha):
        return re.search(r'{[a-z]}', senha) is None

    def tem_letra_maiuscula(self, senha):
        return re.search(r'{[A-Z]}', senha) is None

    def tem_caracteres_repetidos(self, senha):
        return len(senha) == len(set(senha))

    def validar_senha(self, senha):
        return self.aplicar_regras(senha)
