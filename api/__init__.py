from flask import Blueprint

aplicacao = Blueprint("aplicacao", __name__)

from api import login
