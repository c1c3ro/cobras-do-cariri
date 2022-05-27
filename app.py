from flask import Flask, render_template, request, abort
from utils.database import *
from flask_wtf.csrf import CSRFProtect
from formOcorrencia import OcorrenciaForm
from formLogin import LoginForm
from flask_session import Session
from werkzeug.utils import secure_filename
import mysql.connector
import os

app = Flask(__name__)
CSRFProtect(app)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_SSL_STRICT'] = False

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 50
app.config['UPLOAD_EXTENSIONS'] = [".png", ".jpg", ".jpeg", ".gif"]
app.config['UPLOAD_PATH'] = 'registros'

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
    if form.validate_on_submit():
        localizacao = request.form['localizacao']
        informacao_adc = request.form['informacao_adc']
        data = request.form['data']
        try: 
            hora = request.form['hora1']
        except(KeyError):
            hora = request.form['hora2']
        try:
            localizacao_lat = request.form['localizacao_lat'] 
            localizacao_log = request.form['localizacao_log']
            imagem = request.files['file']
            #lidando com a imagem
            nomeImg = secure_filename(imagem.filename)
            if nomeImg != '':
                if len(nomeImg) > 50:
                    nomeImg = nomeImg[0:51]
                file_ext = os.path.splitext(nomeImg)[1]
                if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                    abort(400)
                imagem.save(os.path.join(app.config['UPLOAD_PATH'], nomeImg))
        except(KeyError):
            localizacao_lat = ''
            localizacao_log = ''
            nomeImg = ''
        hora = hora + ":00"
        dateTime = data + " " + hora
        insert_registro(localizacao, informacao_adc, dateTime, localizacao_lat, localizacao_log, nomeImg)
        close_conn()
    return render_template("registro.html", form = form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)