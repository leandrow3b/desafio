import unittest
from api.login_service import Autenticacao


class TestApi(unittest.TestCase):
    def setUp(self):
        self.autenticacao = Autenticacao()

    def test_deve_validar_quantidade_de_caracteres_da_senha(self):

        self.assertEqual(
            self.autenticacao.tamanho_valido("LeandroCosta"), True)

    def test_deve_validar_se_tem_caracteres_especiais(self):
        self.assertEqual(
            self.autenticacao.tem_caracteres_especiais("@Leandro"), True)

    def test_deve_validar_se_existe_numero(self):
        self.assertEqual(
            self.autenticacao.tem_numero("1Leandro"), True)

    def test_deve_validar_se_tem_letra_minuscula(self):
        self.assertEqual(
            self.autenticacao.tem_letra_minuscula("Leandro"), True)

    def test_deve_validar_se_tem_letra_maiuscula(self):
        self.assertEqual(
            self.autenticacao.tem_letra_maiuscula("Leandro"), True)

    def test_deve_validar_se_repeticoes_de_caracteres(self):
        self.assertEqual(
            self.autenticacao.tem_caracteres_repetidos("@Leandro@"), False)

    def test_deve_confirmar_se_a_senha_é_valida(self):
        self.assertEqual(
            self.autenticacao.validar_senha("AbTp9!fok"), True)


if __name__ == '__main__':
    unittest.main()
