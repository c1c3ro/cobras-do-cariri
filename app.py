from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


conn = mysql.connector.connect(host = "mysql04-farm2.uni5.net",
user = "bessapontes23",
password = "marleyanos32",
database = "bessapontes23")

#Creating a connection cursor
cursor = conn.cursor()
 
#Executing SQL Statements
cursor.execute(''' INSERT INTO COBRA (familia, especie, peconhenta, idUSUARIO) 
                    VALUES(teste0, teste1, 0, 1) ''')
 
#Saving the Actions performed on the DB
conn.commit()
 
#Closing the cursor
cursor.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)