from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


conn = mysql.connector.connect(host = "127.0.0.1",
user = "csamuelssm",
password = "S06h27c23a25",
database = "bessapontes23")

#Creating a connection cursor
cursor = conn.cursor()

#Executing SQL Statements
#cursor.execute(" INSERT INTO usuario (idUSUARIO, password, user, email) VALUES(1, '123456', 'csamuelssm', 'csamuelssm@gmail.com') ")

cursor.execute(''' INSERT INTO cobra (familia, especie, peconhenta, idUSUARIO)
                VALUES('Anilius', 'scytale', 0, 1)
                VALUES('Apostolepis, 'cearensis', 0, 1)
                VALUES('Atractus', 'ronnie', 0, 1)
                VALUES('Boa', 'constrictor', 0, 1)
                VALUES('Bothrops', 'atrox', 1, 1)
                VALUES('Bothrops', 'erythromelas', 1, 1)
                VALUES('Chironius', 'flavolineatus', 0, 1)
                VALUES('Corallus', 'hortulanus', 0, 1)
                VALUES('Dipsas', 'mikanii', 0, 1)
                VALUES('Drymoluber', 'brazili', 0, 1)
                VALUES('Drymoluber', 'dichrous', 0, 1)
                VALUES('Epicrates', 'assisi', 0, 1)
                VALUES('Epictia', 'borapeliotes', 0, 1)
                VALUES('Erythrolamprus', 'poecilogyrus', 0, 1)
                VALUES('Erythrolamprus', 'viridis', 0, 1)
                VALUES('Helicops', 'angulatus', 0, 1)
                VALUES('Imantodes', 'cenchoa', 0, 1)
                VALUES('Leptodeira', 'annulata', 0, 1)
                VALUES('Lygophis', 'dilepis', 0, 1)
                VALUES('Micrurus', 'ibiboboca', 0, 1)
                VALUES('Micrurus', 'lemniscatus', 0, 1)
                VALUES('Oxybelis', 'aeneus', 0, 1)
                VALUES('Oxyrhopus', 'trigeminus', 0, 1)
                VALUES('Philodryas', 'nattereri', 0, 1)
                VALUES('Philodryas', 'olfersii', 0, 1)
                VALUES('Pseudoboa', 'nigra', 0, 1)
                VALUES('Psomophis', 'joberti', 0, 1)
                VALUES('Taeniophallus', 'occipitalis', 0, 1) 
                VALUES('Tantilla', 'melanocephala', 0, 1) 
                VALUES('Thamnodynastes', 'almae', 0, 1) 
                VALUES('Thamnodynastes', 'sertanejo', 0, 1) 
                VALUES('Thamnodynastes', 'phoenix', 0, 1) 
                VALUES('Spilotes', 'pullatus', 0, 1)
                VALUES('Xenodon', 'merremii', 0, 1) ''')


#Saving the Actions performed on the DB
conn.commit()

#Closing the cursor
cursor.close()

#Closging the connection
conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)