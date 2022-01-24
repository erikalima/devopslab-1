from flask import Flask
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)

app = Flask(__name__)
csrf.init_app(app)

@app.route("/")
def pagina_inicial():
    return "Hello World - Marcelo Ambrosio de Góes - rm341073"

if __name__ == '__main__':
    app.run()
