from flask import Flask
from api import aplicacao


def main():
    ip = '0.0.0.0'
    port = 8080
    debug = True
    app = Flask(__name__)
    app.register_blueprint(aplicacao)
    app.run(host=ip, debug=debug, port=port)


if __name__ == '__main__':
    main()
