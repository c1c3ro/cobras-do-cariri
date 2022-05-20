from flask import Flask, render_template, request
from utils.database import *
from flask_wtf.csrf import CSRFProtect
from formOcorrencia import OcorrenciaForm
import mysql.connector
import os

app = Flask(__name__)
CSRFProtect(app)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=('GET', 'POST'))
def login():
    return render_template("login.html")

@app.route("/registro", methods=('GET', 'POST'))
def registro():
    form = OcorrenciaForm()
    if form.validate_on_submit():
        localizacao = request.form['localizacao']
        informacao_adc = request.form['informacao_adc']
        print(localizacao, informacao_adc)
    return render_template("registro.html", form = form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)