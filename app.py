
from flask import Flask, render_template,request
import cunsulta_api

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def abre_index():
    tipo_selecionado='cars'

    if request.method=='POST':
        tipo_selecionado=request.form['tipo']
        id_marca=request.form['id_marca']


    dados_buscado=cunsulta_api.consulta_marca(tipo_selecionado)
    dados_modelo=cunsulta_api.consulta_modelo_ano(tipo_selecionado,id_marca)
    return render_template ('index.html',lista_marca=dados_buscado,lista_modelo=dados_modelo)

app.run(debug=True)