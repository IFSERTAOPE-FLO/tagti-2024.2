#python -m venv venv
#.\venv\Scripts\activate
#pip install flask
# pip install python-dotenv
#pip freeze > requirements.txt
#pip install -r requirements.txt
from flask import Flask, render_template, request, redirect, flash
from database import db
from flask_migrate import Migrate
from models import Usuario, Pizza, Pedido

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"

conexao = "sqlite:///pizzaria.db"
app.config["SQLALCHEMY_DATABASE_URI"] = conexao
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cardapio')
def cardapio():
    pizzas = [
        {
            "nome": "Calabresa",
            "ingredientes": "Molho de tomate, mussarela, calabresa, cebola e orégano",
            "preco": 30.00
        },
        {
            "nome": "Mussarela",
            "ingredientes": "Molho de tomate, mussarela e orégano",
            "preco": 25.00
        },
        {
            "nome": "Portuguesa",
            "ingredientes": "Molho de tomate, mussarela, presunto, ovos, cebola, azeitona e orégano",
            "preco": 35.00
        }
    ]
    return render_template("cardapio.html", pizzas=pizzas)

@app.route('/avaliacoes')
def avaliacoes():
    avaliacoes = [
        {
            "nome": "João",
            "comentario": "Muito bom, recomendo!",
            "nota": 5
        },
        {
            "nome": "Maria",
            "comentario": "Gostei, mas achei um pouco caro",
            "nota": 4
        }
    ]
    return render_template("avaliacoes.html", avaliacoes=avaliacoes)

@app.route('/faleconosco', methods=["GET", "POST"])
def faleconosco():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        mensagem = request.form["mensagem"]
        return f"Nome: {nome}, E-mail: {email}, Mensagem: {mensagem}"
    else:
        return render_template("faleconosco.html")
    
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form["email"]
        senha = request.form["senha"]
        if email == "admin@gmail.com" and senha == "admin":
            flash("Login realizado com sucesso!", "success")
            return redirect("/login")
        else:
            flash("E-mail ou senha inválidos", "danger")
            return redirect("/login")

@app.route('/criar_usuario')
def criar_usuario():
    usuario = Usuario("João", "joao@gmail.com", "123")
    db.session.add(usuario)
    db.session.commit()
    return "Usuário cadastrado com sucesso!"

@app.route('/ler_usuario')
def ler_usuario():
    usuario = Usuario.query.all()
    for u in usuario:
        print(u)
    return f"{usuario[0].id} - {usuario[0].nome} - {usuario[0].email}"

@app.route('/ler_usuario/<int:id>')
def ler_usuario_id(id):
    usuario = Usuario.query.get(id)
    return f"{usuario.nome} - {usuario.email}"

@app.route('/atualizar_usuario')
def atualizar_usuario():
    usuario = Usuario.query.get(1)
    usuario.nome = "Maria"
    db.session.add(usuario)
    db.session.commit()
    return f"{usuario.nome}"

@app.route('/deletar_usuario')
def deletar_usuario():
    usuario = Usuario.query.get(1)
    db.session.delete(usuario)
    db.session.commit()
    return f"{usuario.nome}"

if __name__ == '__main__':
    app.run()
