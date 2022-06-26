from flask import Flask, render_template, request, abort, redirect, url_for, session, send_file
from utils.database import *
from flask_wtf.csrf import CSRFProtect
from formOcorrencia import OcorrenciaForm
from formLogin import LoginForm
from formCadastro import CadastroForm
from flask_session import Session
from werkzeug.utils import secure_filename
from hashlib import sha256
from datetime import timedelta
import os, io, zipfile, time

app = Flask(__name__)
CSRFProtect(app)
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_SSL_STRICT'] = False

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 50
app.config['UPLOAD_EXTENSIONS'] = [".png", ".jpg", ".jpeg", ".gif"]
app.config['UPLOAD_PATH'] = os.path.join('static', 'registros')

Session(app)
app.permanent_session_lifetime = timedelta(minutes=10)

@app.route("/")
def index():
    ids, cobras_info, nomes_pop, peconhenta = get_cobras_info()
    noReturn = request.args.get('noReturn', None)
    if not session.get('username'):
        return render_template("index.html", cobras_info=cobras_info, nomes_pop=nomes_pop, peconhenta=peconhenta, ids=ids, noReturn=noReturn)
    else:
        return render_template("index.html", cobras_info=cobras_info, nomes_pop=nomes_pop, peconhenta=peconhenta, noReturn=noReturn, ids=ids, username=session['username'])

@app.route("/identificar")
def identificar():
    if not session.get('username'):
        return render_template("identificar.html")
    else:
        return render_template("identificar.html", username=session['username'])

@app.route("/login", methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            usuario = request.form['usuario']
            senha = request.form['senha']
            senha_cript = sha256(senha.encode('utf-8')).hexdigest()
            if(match_login(usuario, senha_cript)):
                # Login realizado com sucesso
                session['username'] = usuario
                session['logged'] = True
                return redirect(url_for('admin'))
            else:
                return render_template("login.html", form = form, loginFailed = True)

    if not session.get('username'):
        return render_template("login.html", form = form, loginFailed = False)
    else:
        return render_template("login.html", form = form, loginFailed = False, username=session['username'])

@app.route("/hospitais")
def hospitais():
    hospitais = get_hospitais()
    if not session.get('username'):
        return render_template("hospitais.html", hospitais=hospitais)
    else:
        return render_template("hospitais.html", hospitais=hospitais, username=session['username'])

@app.route("/sobre")
def sobre():
    if not session.get('username'):
        return render_template("sobre.html")
    else:
        return render_template("sobre.html", username=session['username'])

@app.route("/registro", methods=('GET', 'POST'))
def registro():
    form = OcorrenciaForm()
    registroId = 0
    if form.validate_on_submit():
        localizacao = request.form['localizacao']
        informacao_adc = request.form['informacao_adc']
        try:
            hora = request.form['hora1']
        except(KeyError):
            hora = request.form.get('hora2', '00:00')
        
        dateTime = request.form['data'] + " " + hora + ":00"
        localizacao_lat = request.form.get('localizacao_lat', '')
        localizacao_log = request.form.get('localizacao_log', '')

        #lidando com as imagens
        try:
            nomesImg = []
            imagens = request.files.getlist('imagem')
            if imagens[0].filename != '':
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
                    imagem.save(os.path.join(app.config['UPLOAD_PATH'], str(registroId), nomesImg[-1]))
        except(KeyError):
            isImg = 0
            registroId = insert_registro(localizacao, informacao_adc, dateTime, localizacao_lat, localizacao_log, isImg)
    if not session.get('username'):
        return render_template("registro.html", form = form, registroId = registroId)
    else:
        return render_template("registro.html", form = form, registroId = registroId, username=session['username'])

@app.route("/cobras/<search>")
def pesquisa(search):
    ids, cobras_info, nomes_pop, peconhenta = get_cobras_info(search)
    if not cobras_info:
        return redirect(url_for(".index", noReturn=True))
    if not session.get('username'):
        return render_template("pesquisa.html", cobras_info=cobras_info, nomes_pop=nomes_pop, search=search, ids=ids, peconhenta=peconhenta)
    else:
        return render_template("pesquisa.html", cobras_info=cobras_info, nomes_pop=nomes_pop, search=search, ids=ids, peconhenta=peconhenta, username=session['username'])

@app.route("/cobra/<id>")
def cobra(id):
    info_cobra = get_cobra(id)
    if not session.get('username'):
        return render_template('cobra.html', info_cobra=info_cobra, cobra="{} {}".format(info_cobra['familia'], info_cobra['especie']))
    else:
        return render_template('cobra.html', info_cobra=info_cobra, username=session['username'], cobra="{} {}".format(info_cobra['familia'], info_cobra['especie']))

@app.route("/admin")
def admin():
    cadastro = request.args.get('cadastro', None)
    if not session.get('logged'):
        return render_template("proibido.html")
    else:
        return render_template("admin.html", username=session['username'], cadastro=cadastro)

@app.route("/cadastro", methods=('GET', 'POST'))
def cadastro():
    if not session.get('logged'):
        return render_template("proibido.html")
    else:
        form = CadastroForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                usuario = request.form['usuario']
                senha = request.form['senha']
                email = request.form['email']
                senha_cript = sha256(senha.encode('utf-8')).hexdigest()
                if novo_usuario(usuario, senha_cript, email) != -1:
                    return redirect(url_for("admin", cadastro=True))
                else:
                    return render_template("cadastro.html", username=session['username'], form=form, cadastro=False)
        return render_template("cadastro.html", username=session['username'], form=form)

@app.route("/admin/registros")
def admin_registros():
    if not session.get('logged'):
        return render_template("proibido.html")
    else:
        registros = get_registros()
        deleteRegistro = request.args.get('deleteRegistro', None)
        if deleteRegistro is not None:
            return render_template("admin_registros.html", username=session['username'], registros=registros, deleteRegistro=deleteRegistro)
        else:
            return render_template("admin_registros.html", username=session['username'], registros=registros)

@app.route("/download/<id>")
def download(id):
    if not session.get('logged'):
        return render_template("proibido.html")
    else:
        timestr = time.strftime("%Y%m%d-%H%M%S")
        fileName = "registro{}.zip".format(id)
        memory_file = io.BytesIO()
        file_path = 'static/registros/{}/'.format(id)
        with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    zipf.write(os.path.join(root, file))
                    print(os.path.join(root, file))
        memory_file.seek(0)
        return send_file(memory_file, attachment_filename=fileName, as_attachment=True)


@app.route("/excluir/<id>")
def excluir(id):
    if not session.get('logged'):
        return render_template("proibido.html")
    else:
        status = delete_registro(id)
        return redirect(url_for("admin_registros", deleteRegistro=status))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)