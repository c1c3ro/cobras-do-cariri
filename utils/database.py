import mysql.connector
import os

def get_conn(host = "mysql04-farm2.uni5.net",
            user = "bessapontes23", password = "6qSLjgbR",
            database = "bessapontes23"):
    try:
        conn = mysql.connector.connect(host = host,
            user = user,
            password = password,
            database = database)
    except mysql.connector.Error as error:
        print("Falha ao se conectar no banco de dados: {}".format(error))
        conn = None
    return conn

def close_conn():
    global conn
    if conn is not None and conn.is_connected():
        conn.close()

def get_cobras():
    # função que retorna o nome científico das cobras no banco
    global conn
    cursor = conn.cursor()

    query = ("SELECT familia, especie FROM COBRA")
    cursor.execute(query)

    cobras = []
    for familia, especie in cursor:
        cobras.append("{} {}".format(familia, especie))

    cursor.close()
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

def insert_registro(localizacao, informacao_adc,
                    dateTime, localizacao_lat = '', 
                    localizacao_log = '', imgPath = ''):
    global conn
    cursor = conn.cursor()
    try:
        insert_query = """INSERT INTO REGISTRO (localizacao, localizacao_lat, localizacao_log, imagem, informacao_adc, data_hora) 
                        VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, (localizacao, localizacao_lat, localizacao_log, imgPath, informacao_adc, dateTime))
        print(cursor.rowcount, "Registro salvo com sucesso")
        cursor.close()
    except mysql.connector.Error as error:
        print("Falha ao inserir o registro no banco de dados: {}".format(error))

# usar essa variável global para executar queries no banco de dados
conn = get_conn()