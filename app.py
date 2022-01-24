from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - Marcelo Ambrosio de Góes - rm341073"

if __name__ == '__main__':
    app.run()