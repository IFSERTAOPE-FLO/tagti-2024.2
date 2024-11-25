#python -m venv venv
#.\venv\Scripts\activate
#pip install flask
# pip install python-dotenv
#pip freeze > requirements.txt
#pip install -r requirements.txt
from flask import Flask, render_template, request

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run()
