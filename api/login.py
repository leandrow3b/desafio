# -*- coding: utf-8 -*-
from api import aplicacao
from flask import request
from api.login_service import Autenticacao


@aplicacao.route("/api/v1/login", methods=['POST'])
def login():
    dados = request.get_json()
    autenticacao = Autenticacao()
    resposta = autenticacao.validar_senha(dados['senha'])
    return {"resposta": resposta}
