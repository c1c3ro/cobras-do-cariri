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

def get_cobras():
    # função que retorna o nome científico das cobras no banco
    conn = get_conn()
    cursor = conn.cursor()

    query = ("SELECT familia, especie FROM COBRA ORDER BY familia")
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

def insert_registro(localizacao, informacao_adc,
                    dateTime, localizacao_lat = '',
                    localizacao_log = '', isImg = 0):
    conn = get_conn()
    cursor = conn.cursor()
    idRegistro = None
    try:
        insert_query = """INSERT INTO REGISTRO (localizacao, localizacao_lat, localizacao_log, imagem, informacao_adc, data_hora)
                        VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (localizacao, localizacao_lat, localizacao_log, isImg, informacao_adc, dateTime)
        cursor.execute(insert_query, values)
        print(cursor.rowcount, "Registro salvo com sucesso")
        conn.commit()
        idRegistro = cursor.lastrowid
    except mysql.connector.Error as error:
        print("Falha ao inserir o registro no banco de dados: {}".format(error))
    finally:
        cursor.close()
        conn.close()
    return idRegistro
