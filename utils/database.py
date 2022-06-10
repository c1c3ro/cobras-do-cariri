from asyncio import constants
from flask import abort
import mysql.connector
import os

conn = None

def start_conn(host = "mysql04-farm2.uni5.net",
            user = "bessapontes23", password = "6qSLjgbR",
            database = "bessapontes23"):
    global conn
    if conn is not None and conn.is_connected():
        return conn
    try:
        conn = mysql.connector.connect(host = host,
            user = user,
            password = password,
            database = database)
    except mysql.connector.Error as error:
        print("Falha ao se conectar no banco de dados: {}".format(error))
        abort(500)

def close_conn():
    global conn
    if conn is not None:
        conn.close()
        conn = None

def get_cobras(search):
    # função que retorna o nome científico das cobras no banco
    global conn
    start_conn()
    cursor = conn.cursor()

    query = """SELECT COBRA.idCOBRA, COBRA.familia, COBRA.especie, COBRA.peconhenta, COBRA_NOME_POP.nome FROM COBRA
            INNER JOIN COBRA_NOME_POP ON COBRA.idCOBRA = COBRA_NOME_POP.idCOBRA """

    if search is not None:
        pos_query = "WHERE"
        searchSplit = search.replace('-', ' ').split()
        if 'cobra' in search or 'serpente' in search:
            if len(searchSplit) <= 1:
                searchSplit = []
                pos_query = ""
            else:
                for i in searchSplit:
                    if 'cobra' in i or 'serpente' in i:
                        searchSplit.remove(i)
        search = ['%' + i + '%' for i in searchSplit]
        for p in range(len(search)):
            pos_query += """ CONCAT(COBRA.familia, COBRA.especie, COBRA_NOME_POP.nome) LIKE %s"""
            if p < len(search) - 1:
                pos_query += " OR"
    else:
        pos_query = "ORDER BY familia;"

    query = query + pos_query
    print(query)
    cursor.execute(query, search)

    cobras = []
    nomes_pop = {}
    peconha = {}
    ids = {}
    for id, familia, especie, peconhenta, nome_pop in cursor:
        nome_cientifico = "{} {}".format(familia, especie)
        cobras.append(nome_cientifico)
        peconha[nome_cientifico] = peconhenta
        ids[nome_cientifico] = id
        if nome_cientifico not in nomes_pop.keys():
            nomes_pop[nome_cientifico] = []
        nomes_pop[nome_cientifico].append(nome_pop)

    cursor.close()
    close_conn()
    return ids, cobras, nomes_pop, peconha

def get_cobras_info(search = None):
    ids, cobras, nomes_pop, peconhenta = get_cobras(search)
    cobras_info = {}
    for cobra in cobras:
        for filename in os.listdir("./static/serpentesFotos/{}".format(cobra)):
            if cobra not in cobras_info.keys():
                cobras_info[cobra] = []
            cobras_info[cobra].append(filename)
    return ids, cobras_info, nomes_pop, peconhenta

def get_hospitais():
    global conn
    start_conn()
    cursor = conn.cursor()
    query = ("SELECT idHOSPITAL, nome, localizacao, municipio, telefone FROM HOSPITAL WHERE 1=1")
    cursor.execute(query)
    hospitais = {}
    for id, nome, localizacao, municipio, telefone in cursor:
        if nome not in hospitais.keys():
            hospitais[nome] = {}
        hospitais[nome]['id'] = id
        hospitais[nome]['localizacao'] = localizacao
        hospitais[nome]['municipio'] = municipio
        hospitais[nome]['telefone'] = telefone

    return hospitais

def insert_registro(localizacao, informacao_adc,
                    dateTime, localizacao_lat = '',
                    localizacao_log = '', isImg = 0):
    global coon
    start_conn()
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
        idRegistro = -1
    finally:
        cursor.close()
        close_conn()
    return idRegistro

def match_login(usuario, senha_cript):
    global conn
    start_conn()
    cursor = conn.cursor()
    login = (usuario, senha_cript)

    query = """SELECT COUNT(idUSUARIO) AS Count FROM USUARIO WHERE USUARIO.user = %s AND USUARIO.password = %s"""
    cursor.execute(query, login)

    for count in cursor:
        if count[0] == 1:
            return True
        else:
            return False

def novo_usuario(usuario, senha_cript, email):
    global conn
    start_conn()
    cursor = conn.cursor()
    values= (usuario, senha_cript, email)

    query = """INSERT INTO USUARIO (user, password, email) VALUES (%s, %s, %s)"""
    try:
        cursor.execute(query, values)
        print(cursor.rowcount, "Registro salvo com sucesso")
        conn.commit()
        idRegistro = cursor.lastrowid
    except mysql.connector.Error as error:
        print("Falha ao inserir o registro no banco de dados: {}".format(error))
        idRegistro = -1
    finally:
        cursor.close()
        close_conn()
    return idRegistro

def get_cobra(id):
    global conn
    start_conn()
    cursor = conn.cursor()
    #value = (id)

    query = f"SELECT  COBRA.familia, COBRA.especie, COBRA.peconhenta, COBRA_NOME_POP.nome FROM COBRA INNER JOIN COBRA_NOME_POP ON COBRA.idCOBRA = COBRA_NOME_POP.idCOBRA WHERE COBRA.idCOBRA = {id}"

    cursor.execute(query)

    info_cobra = {}
    for familia, especie, peconhenta, nome_pop in cursor:
        info_cobra['familia'] = familia
        info_cobra['especie'] = especie
        info_cobra['peconhenta'] = peconhenta
        if 'nome_pop' not in info_cobra.keys():
            info_cobra['nome_pop'] = []
        info_cobra['nome_pop'].append(nome_pop)

    for filename in os.listdir("./static/serpentesFotos/{} {}".format(info_cobra['familia'], info_cobra['especie'])):
        if 'filenames' not in info_cobra.keys():
            info_cobra['filenames'] = []
        info_cobra['filenames'].append(filename)

    print(info_cobra)
    return info_cobra


