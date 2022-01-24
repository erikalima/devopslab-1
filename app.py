from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

@app.route("/")
def pagina_inicial():
    return "Hello World - Marcelo Ambrosio de Góes - rm341073"

if __name__ == '__main__':
    app.run()
