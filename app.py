from flask import Flask, render_template, request
from utils.database import *
from flask_wtf.csrf import CSRFProtect
from formOcorrencia import OcorrenciaForm
from formLogin import LoginForm
from flask_session import Session
import mysql.connector
import os

app = Flask(__name__)
CSRFProtect(app)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_SSL_STRICT'] = False
Session(app)

@app.route("/")
def index():
    cobras_info = get_cobras_info()
    print(cobras_info)
    return render_template("index.html", cobras_info=cobras_info)

@app.route("/login", methods=('GET', 'POST'))
def login():
    form = LoginForm()
    return render_template("login.html", form = form)

@app.route("/registro", methods=('GET', 'POST'))
def registro():
    print("tá dando certo?")
    form = OcorrenciaForm()
<<<<<<< HEAD
    if form.validate_on_submit():
        localizacao = request.form['localizacao']
        informacao_adc = request.form['informacao_adc']
        data = request.form['data']
        hora = request.form['hora1']
        print(localizacao, informacao_adc)
        print(data)
        print(hora)
=======
    if request.method == "POST":
        if form.validate_on_submit():
            localizacao = request.form['localizacao']
            informacao_adc = request.form['informacao_adc']
            data = request.form['data']
            #hora = request.form['hora']
            print(localizacao, informacao_adc)
            #print(data)
            #print(hora)
        else:
            print("Algo deu errado")
            if form.errors != {}:
                for err in form.errors.values():
                    print(f"Houve um erro: {err}")
>>>>>>> 05bc27dab822f7891e3bd330b8373d350a11d481
    return render_template("registro.html", form = form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)