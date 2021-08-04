from flask import Flask, redirect
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/digaiword',  methods=['GET', 'POST'])
def primeira():
    if request.method == 'GET':
        return render_template('Digai_tela_PalavraUnica.html' )
    if request.method == 'POST':
        return render_template('digai_dashboard_aluno.html')
#        return {'Digai': 'Termino ok!'}


@app.route('/digai')
def segunda():
    return 'DIGAI. Gostaram?'

@app.route('/entra/<string:frase>')
def terceira( frase ):
    return 'DIGAI. Sua frase: '+frase
