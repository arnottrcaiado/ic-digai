#
# FACULDADE SENAC PE
# PROJETO DE INICIAÇÃO CIENTÍFICA - PIC
#
# PROJETO: DIGAI
#
# ORIENTADOR: PROF. ARNOTT RAMOS CAIADO
#
# -*- coding: utf-8 -*-


from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/digaiword',  methods=['GET', 'POST'])
def input_palavra():
    if request.method == 'GET':
        return render_template('Digai_tela_PalavraUnica.html' )
    if request.method == 'POST':
        return render_template('digai_dashboard_aluno.html')
 #       return {'Digai': 'Termino ok!'}

@app.route('/digaipalavra',  methods=['GET', 'POST'])
def escolha_palavra():
    if request.method == 'GET':
        return render_template('digai_escolha_palavra_input.html' )
    if request.method == 'POST':
        palavras=[]
        for i in range (0,4 ):
            vlinha = "p"+str(i+1)
            for j in range (0,5) :
                variavel = vlinha + str(j+1)
                if request.form.get( variavel ) != None :
                    palavras.append( request.form.get( variavel ))

        return {'Digai':'ok', 'Palavras':palavras }

  #      if request.form.get('p11') != None :
  #         palavras.append(request.form.get('p11'))
  #      if request.form.get('p12') != None :
  #         palavras.append(request.form.get('p12'))
  #      if request.form.get('p13') != None :
  #         palavras.append(request.form.get('p13'))
  #      if request.form.get('p14') != None :
  #         palavras.append(request.form.get('p14'))
  #      if request.form.get('p21') != None :
  #         palavras.append(request.form.get('p21'))
  #      if request.form.get('p22') != None :
  #         palavras.append(request.form.get('p22'))
  #      if request.form.get('p23') != None :
  #         palavras.append(request.form.get('p23'))
  #      if request.form.get('p24') != None :
  #         palavras.append(request.form.get('p24'))



@app.route('/digai')
def segunda():
    return 'DIGAI. Gostaram?'

@app.route('/entra/<string:frase>')
def terceira( frase ):
    return 'DIGAI. Sua frase: '+frase
