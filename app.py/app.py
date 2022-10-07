from flask import Flask
from flask import render_template
from flask import request
import csv
import pandas


app = Flask(__name__)
registros = []
lista = []


@app.route('/', methods = ['GET'])
def principal():
    return render_template('cadastro.html')

@app.route('/dados', methods = ['GET'])
def dados():
    lista_cadastro()
    return render_template('dados.html')



@app.route('/cadastro', methods = ['GET', 'POST'])

def cadastro():
    if request.method == 'POST':    
        registros.append(request.form.get('modelo'))  
        registros.append(request.form.get('marca'))  
        registros.append(request.form.get('placa'))  
        registros.append(request.form.get('nome'))
        registros.append(request.form.get('ano'))   
        registros.append(request.form.get('UF')) 
        registros.append(request.form.get('cidade')) 
        registros.append(request.form.get('endereco'))
        registros.append(request.form.get('foto'))
        registros.append(request.form.get('descricao'))
        print(registros)
    with open('cadastro.csv', 'a', newline='\n') as insere_linha:
            arquivo = csv.writer(insere_linha)
            arquivo.writerow(registros)        
            insere_linha.close()
            registros.clear()
            
            
            
    return render_template ('confirma.html')

@app.route('/lista_cadastro', methods = ['GET', 'POST'])
def lista_cadastro():
    lista.clear()
    with open('cadastro.csv') as listagem:
        csv_reader = csv.reader(listagem, delimiter=',')
        for row in csv_reader:
            print(row)
            lista.append(row)
            file = pandas.read_csv("cadastro.csv")            
        file.to_html("templates/dados.html")   
    return str(lista)

    
app.run(debug = True)


