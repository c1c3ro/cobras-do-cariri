import mysql.connector
import os

def get_conn(host = "mysql04-farm2.uni5.net",
            user = "bessapontes23", password = "6qSLjgbR",
            database = "bessapontes23"):
    conn = mysql.connector.connect(host = host,
        user = user,
        password = password,
        database = database)
    return conn

def get_cobras():
    # função que retorna o nome científico das cobras no banco
    conn = get_conn()
    cursor = conn.cursor()

    query = ("SELECT familia, especie FROM COBRA")
    cursor.execute(query)

    cobras = []
    for familia, especie in cursor:
        cobras.append("{} {}".format(familia, especie))

    cursor.close()
    conn.close()

    return cobras

def get_cobras_info():
    cobras = get_cobras()
    cobras_info = {}
    for cobra in cobras:
        for filename in os.listdir("./static/serpentesFotos/{}".format(cobra)):
            if cobra not in cobras_info.keys():
                cobras_info[cobra] = []
            cobras_info[cobra].append(filename)
    return cobras_info