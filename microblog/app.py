#python -m venv venv
#.\venv\Scripts\activate
#pip install flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html", tel="(81) 988889898", nome="Joao")

@app.route("/user/<nome>", defaults={"sobrenome": "Silva"})
@app.route("/user/<nome>/<sobrenome>")
def user(nome, sobrenome):
    return f"Olá, {nome} {sobrenome}!"

# Calculadora para somar dois números passados por parâmetro
@app.route("/soma/<int:num1>/<int:num2>")
def soma(num1, num2):
    return f"O resultado da soma é: {num1 + num2}"

# Minha página pessoal
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/dados", methods=["GET", "POST"])
def dados():
    if request.method == "GET":
        return render_template("dados.html")
    elif request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        msg = request.form["mensagem"]
        return f"Nome: {nome}, Email: {email}, Mensagem: {msg}"
    else:
        return "Método não permitido"

if __name__ == '__main__':
    app.run()
