from flask import Flask, render_template
import cunsulta_api

app=Flask(__name__)

@app.route("/")
def abre_index():

    dados_buscado=cunsulta_api.consulta_marca('cars')
    return render_template ('index.html',lista_marca=dados_buscado)

app.run(debug=True)