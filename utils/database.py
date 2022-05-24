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

def insert_registro(localizacao, informacao_adc,
                    dateTime, localizacao_lat = None, 
                    localizacao_log = None, imgPath = None):
    try:
        if (localizacao_lat is None or localizacao_log is None) and (imgPath is not None):
            insert_query = ("INSERT INTO REGISTRO (localizacao, imagem, informacao_adc, data_hora) VALUES (%s, %s, %s, %s)", (localizacao, imgPath, informacao_adc, dateTime))
        elif (localizacao_lat is None or localizacao_log is None) and (imgPath is None):
            insert_query = ("INSERT INTO REGISTRO (localizacao, informacao_adc, data_hora) VALUES (%s, %s, %s)", (localizacao, informacao_adc, dateTime))
        else:
            insert_query = ("INSERT INTO REGISTRO (localizacao, localizacao_lat, localizacao_log, imagem, informacao_adc, data_hora) VALUES (%s, %s, %s, %s, %s, %s)", (localizacao, localizacao_lat, localizacao_log, imgPath, informacao_adc, dateTime))
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(insert_query)
        print(cursor.rowcount, "Registro salvo com sucesso")
        cursor.close()
    except mysql.connector.Error as error:
        print("Falha ao inserir o registro no banco de dados: {}".format(error))

    finally:
        if conn.is_connected():
            conn.close()



