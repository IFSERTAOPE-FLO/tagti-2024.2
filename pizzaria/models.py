from database import db

class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return f"<Usuario {self.id} - {self.nome} - {self.email} - {self.senha}>"

class Pizza(db.Model):
    __tablename__ = "pizza"
    id = db.Column(db.Integer, primary_key=True)
    sabor = db.Column(db.String(280), nullable=False)
    imagem = db.Column(db.String(280), nullable=False)
    ingredientes = db.Column(db.String(280), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __init__(self, sabor, imagem, ingredientes, preco):
        self.sabor = sabor
        self.imagem = imagem
        self.ingredientes = ingredientes
        self.preco = preco

    def __repr__(self):
        return f"<Pizza {self.sabor}>"
    
class Pedido(db.Model):
    __tablename__ = "pedido"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizza.id"), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
   
    def __init__(self, usuario_id, pizza_id, data):
        self.usuario_id = usuario_id
        self.pizza_id = pizza_id
        self.data = data

    def __repr__(self):
        return f"<Pedido {self.id}>"