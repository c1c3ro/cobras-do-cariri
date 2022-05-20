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

#Saving the Actions performed on the DB
#conn.commit()

#Closing the cursor
#cursor.close()

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