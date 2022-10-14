from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = 'Leandro'
    dados = {"prof": "Publicitário" , "portfolio": "https://leandrovieirareis.github.io/lvr/" }
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')