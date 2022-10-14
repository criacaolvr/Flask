from crypt import methods

from django.shortcuts import redirect
from app import app
from flask import render_template
from flask import request
from flask import flash
from flask import redirect

@app.route('/')
@app.route('/index')
def index():
    nome = 'Leandro'
    dados = {"prof": "Publicitário" , "portfolio": "https://leandrovieirareis.github.io/lvr/" }
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if(usuario == 'admin' and senha== 'senha123'):
        return "Usuario:{} e Senha {}".format(usuario, senha)
    else:
        flash("Dados Inválidos!")
        return redirect('/usuario')