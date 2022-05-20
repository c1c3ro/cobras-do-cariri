from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from formOcorrencia import OcorrenciaForm
from flask_session import Session
import mysql.connector
import os

app = Flask(__name__)
CSRFProtect(app)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_SSL_STRICT'] = False
Session(app)


conn = mysql.connector.connect(host = "mysql04-farm2.uni5.net",
user = "bessapontes23",
password = "6qSLjgbR",
database = "bessapontes23")
"""
#Creating a connection cursor
#cursor = conn.cursor()

#Executing SQL Statements
#cursor.execute(" INSERT INTO usuario (idUSUARIO, password, user, email) VALUES(1, '123456', 'csamuelssm', 'csamuelssm@gmail.com') ")

cursor.execute(''' INSERT INTO cobra (familia, especie, peconhenta, idUSUARIO)
                VALUES('Anilius', 'scytale', 0, 2),
                ('Apostolepis', 'cearensis', 0, 2),
                ('Atractus', 'ronnie', 0, 2),
                ('Boa', 'constrictor', 0, 2),
                ('Bothrops', 'atrox', 1, 2),
                ('Bothrops', 'erythromelas', 1, 2),
                ('Chironius', 'flavolineatus', 0, 2),
                ('Corallus', 'hortulanus', 0, 2),
                ('Dipsas', 'mikanii', 0, 2),
                ('Drymoluber', 'brazili', 0, 2),
                ('Drymoluber', 'dichrous', 0, 2),
                ('Epicrates', 'assisi', 0, 2),
                ('Epictia', 'borapeliotes', 0, 2),
                ('Erythrolamprus', 'poecilogyrus', 0, 2),
                ('Erythrolamprus', 'viridis', 0, 2),
                ('Helicops', 'angulatus', 0, 2),
                ('Imantodes', 'cenchoa', 0, 2),
                ('Leptodeira', 'annulata', 0, 2),
                ('Lygophis', 'dilepis', 0, 2),
                ('Micrurus', 'ibiboboca', 0, 2),
                ('Micrurus', 'lemniscatus', 0, 2),
                ('Oxybelis', 'aeneus', 0, 2),
                ('Oxyrhopus', 'trigeminus', 0, 2),
                ('Philodryas', 'nattereri', 0, 2),
                ('Philodryas', 'olfersii', 0, 2),
                ('Pseudoboa', 'nigra', 0, 2),
                ('Psomophis', 'joberti', 0, 2),
                ('Taeniophallus', 'occipitalis', 0, 2),
                ('Tantilla', 'melanocephala', 0, 2),
                ('Thamnodynastes', 'almae', 0, 2),
                ('Thamnodynastes', 'sertanejo', 0, 2),
                ('Thamnodynastes', 'phoenix', 0, 2),
                ('Spilotes', 'pullatus', 0, 2),
                ('Xenodon', 'merremii', 0, 2); ''')


#Saving the Actions performed on the DB
conn.commit()

#Closing the cursor
cursor.close()

#Closging the connection
conn.close() """

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