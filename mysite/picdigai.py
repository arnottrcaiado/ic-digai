#
# FACULDADE SENAC PE
# PROJETO DE INICIAÇÃO CIENTÍFICA - PIC
#
# PROJETO: DIGAI
#
# ORIENTADOR: PROF. ARNOTT RAMOS CAIADO
#

# -*- coding: UTF-8 -*-


from flask import Flask
from flask import request,json
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
        cor ="laranja"
        if request.args.get('cor') != None :
            cor = request.args.get('cor')
        return render_template('digai_escolha_palavra_input.html', cor=cor )
    if request.method == 'POST':
        palavras=[]
        for i in range (0,4 ):
            vlinha = "p"+str(i+1)
            for j in range (0,5) :
                variavel = vlinha + str(j+1)
                if request.form.get( variavel ) != None :
                    if len(request.form.get( variavel )) > 1 :
                        palavras.append( request.form.get( variavel ))

        return json.dumps({'Digai':'ok', 'Palavras':palavras }, ensure_ascii=False)

@app.route('/digaidesafio',  methods=['GET', 'POST'])
def escolha_desafio():
    if request.method == 'GET':
        cor ="vermelho"
        if request.args.get('cor') != None :
            cor = request.args.get('cor')
        return render_template('digai_desafio_input.html', cor=cor )
    if request.method == 'POST':
        palavras=[]
        for i in range (0,7 ):
            vlinha = "d"+str(i+1)
            for j in range (0,1) :
                variavel = vlinha + str(j+1)
                if request.form.get( variavel ) != None :
                    if len(request.form.get( variavel )) > 1 :
                        palavras.append( request.form.get( variavel ))

        return json.dumps({'DigaiDesafio':'ok', 'Desafios':palavras }, ensure_ascii=False)


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

@app.route('/digai/interacao', methods=['GET', 'POST'])
def interacao():
    nome="* Estudante *"
    secao="# Ab01"
    ninter = 100
    cor ="vermelho"
    if request.method == 'GET':
        if request.args.get('cor') != None :
            cor = request.args.get('cor')

        return render_template('digai_interacao.html', cor=cor, nome=nome, secao=secao, ninter=ninter)
    if request.method == 'POST' :
        who=[]
        dig=[]
        if request.form.get('all') != None :
            who.append('all')
        if request.form.get('you') != None :
            who.append('you')
        if request.form.get('teacher') != None :
            who.append('teacher')
        if request.form.get('power') != None :
            dig.append('power')
        if request.form.get('answer') != None :
            dig.append('answer')
        if request.form.get('question') != None :
            dig.append('question')
        if request.form.get('gifts') != None :
            dig.append('gifts')
        if request.form.get('challenge') != None :
            dig.append('challenge')
        if request.form.get('help') != None :
            dig.append('help')

        return json.dumps({'Estudante': nome, 'Secao': secao, 'Inter:': ninter,'DigaiInteracao':'ok', 'Who':who, 'Dig': dig }, ensure_ascii=False)

@app.route('/digai')
def segunda():
    return 'DIGAI. Gostaram?'

@app.route('/entra/<string:frase>')
def terceira( frase ):
    return 'DIGAI. Sua frase: '+frase
