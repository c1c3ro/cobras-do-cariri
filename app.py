from flask import Flask, render_template, request, abort, g
from utils.database import *
from flask_wtf.csrf import CSRFProtect
from formOcorrencia import OcorrenciaForm
from formLogin import LoginForm
from flask_session import Session
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CSRFProtect(app)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_SSL_STRICT'] = False

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 50
app.config['UPLOAD_EXTENSIONS'] = [".png", ".jpg", ".jpeg", ".gif"]
app.config['UPLOAD_PATH'] = os.path.join('static', 'registros')

Session(app)

@app.route("/")
def index():
    cobras_info, nomes_pop = get_cobras_info()
    #print(nomes_pop)
    return render_template("index.html", cobras_info=cobras_info, nomes_pop=nomes_pop)

@app.route("/login", methods=('GET', 'POST'))
def login():
    form = LoginForm()
    return render_template("login.html", form = form)

@app.route("/hospitais")
def hospitais():
    hospitais = get_hospitais()
    return render_template("hospitais.html", hospitais=hospitais)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/registro", methods=('GET', 'POST'))
def registro():
    form = OcorrenciaForm()
    registroId = 0
    if form.validate_on_submit():
        localizacao = request.form['localizacao']
        informacao_adc = request.form['informacao_adc']
        data = request.form['data']
        try:
            hora = request.form['hora1']
        except(KeyError):
            try:
                hora = request.form['hora2']
            except(KeyError):
                hora = '00:00'

        hora = hora + ":00"
        dateTime = data + " " + hora

        try:
            localizacao_lat = request.form['localizacao_lat']
            localizacao_log = request.form['localizacao_log']
        except KeyError as err:
            print(err)
            localizacao_lat = ''
            localizacao_log = ''
        try:
            nomesImg = []
            #lidando com as imagens
            imagens = request.files.getlist('imagem')
            if imagens:
                isImg = 1
            else:
                raise KeyError
            # pegando o id do registro para criar uma pasta que conterá as imagens
            registroId = insert_registro(localizacao, informacao_adc, dateTime, localizacao_lat, localizacao_log, isImg)
            os.mkdir(os.path.join(app.config['UPLOAD_PATH'], str(registroId)))
            for imagem in imagens:
                if imagem.filename != '':
                    nomesImg.append(secure_filename(imagem.filename))
                    file_ext = os.path.splitext(nomesImg[-1])[1]
                    if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                        abort(400)
                    imagem.save(os.path.join(app.config['UPLOAD_PATH'], str(registroId),nomesImg[-1]))
        except(KeyError):
            isImg = 0
            registroId = insert_registro(localizacao, informacao_adc, dateTime, localizacao_lat, localizacao_log, isImg)
    return render_template("registro.html", form = form, registroId = registroId)

@app.route("/cobras/<search>")
def pesquisa(search):
    cobras_info, nomes_pop = get_cobras_info(search)
    if not cobras_info:
        print("entrei no if")
    else:
        print("entrei no else")
    return render_template("pesquisa.html", cobras_info=cobras_info, nomes_pop=nomes_pop, search=search)


if __name__ == "__main__":
    app.run(debug=True)