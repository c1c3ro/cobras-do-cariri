from asyncio import constants
from flask import abort
import mysql.connector
import json
import os

conn = None
credentials = {}
with open('databaseCredentials.json') as j_file:
    credentials = json.load(j_file)

def execute_query(query, params = None, isAlteration = False, lastRowId = False, rowCount = False):
    global conn
    start_conn()
    results = {}
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        if isAlteration:
            conn.commit()
    except mysql.connector.Error as error:
        print("Falha ao executar a query: {}, parâmetros: {}, erro: {}".format(query, params, error))
    finally:
        results['rows'] = cursor.fetchall()
        if lastRowId:
            results['lastRowId'] = cursor.lastrowid
        elif rowCount:
            results['rowCount'] = cursor.rowcount
        cursor.close()
        close_conn()
    
    return results
    

def start_conn(host = credentials['host'],
            user = credentials['user'], password = credentials['password'],
            database = credentials['database']):
    global conn
    global credentials
    if conn is not None and conn.is_connected():
        return conn
    try:
        conn = mysql.connector.connect(host = credentials['host'],
            user = credentials['user'],
            password = credentials['password'],
            database = credentials['database'])
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

    query = """SELECT COBRA.idCOBRA, COBRA.familia, COBRA.especie, COBRA.peconhenta, COBRA_NOME_POP.nome, FAMILIA.nome FROM COBRA
            INNER JOIN COBRA_NOME_POP ON COBRA.idCOBRA = COBRA_NOME_POP.idCOBRA
            INNER JOIN FAMILIA ON COBRA.grupo = FAMILIA.idFam """

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
            pos_query += """ CONCAT(COBRA.familia, COBRA.especie, COBRA_NOME_POP.nome, FAMILIA.nome) LIKE %s"""
            if p < len(search) - 1:
                pos_query += " OR"
    else:
        pos_query = "ORDER BY familia;"

    query = query + pos_query

    cursor = execute_query(query, search)

    cobras = []
    nomes_pop = {}
    peconha = {}
    ids = {}
    for id, familia, especie, peconhenta, nome_pop, fam in cursor['rows']:
        nome_cientifico = "{} {}".format(familia, especie)
        cobras.append(nome_cientifico)
        peconha[nome_cientifico] = peconhenta
        ids[nome_cientifico] = id
        if nome_cientifico not in nomes_pop.keys():
            nomes_pop[nome_cientifico] = []
        nomes_pop[nome_cientifico].append(nome_pop)

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
    query = ("SELECT idHOSPITAL, nome, localizacao, municipio, telefone, mapa FROM HOSPITAL WHERE 1=1")
    cursor = execute_query(query)
    hospitais = {}
    for id, nome, localizacao, municipio, telefone, mapa in cursor['rows']:
        if nome not in hospitais.keys():
            hospitais[nome] = {}
        hospitais[nome]['id'] = id
        hospitais[nome]['localizacao'] = localizacao
        hospitais[nome]['municipio'] = municipio
        hospitais[nome]['telefone'] = telefone
        hospitais[nome]['mapa'] = mapa

    return hospitais

def insert_registro(localizacao, informacao_adc,
                    dateTime, localizacao_lat = '',
                    localizacao_log = '', isImg = 0):

    insert_query = """INSERT INTO REGISTRO (localizacao, localizacao_lat, localizacao_log, imagem, informacao_adc, data_hora)
                    VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (localizacao, localizacao_lat, localizacao_log, isImg, informacao_adc, dateTime)
    cursor = execute_query(insert_query, values, isAlteration = True, lastRowId=True)
    if cursor['lastRowId'] is not None:
        idRegistro = cursor['lastRowId']
    else:
        idRegistro = -1
    return idRegistro

def get_registros():
    query = "SELECT idREGISTRO, localizacao, localizacao_lat, localizacao_log, imagem, informacao_adc, data_hora FROM REGISTRO WHERE 1=1 ORDER BY data_hora DESC"
    cursor = execute_query(query)
    registros = {}
    for id, localizacao, loc_lat, loc_log, img, informacao_adc, dateTime in cursor['rows']:
        registros[id] = {}
        registros[id]['localizacao'] = localizacao
        registros[id]['localizacao_lat'] = loc_lat
        registros[id]['localizacao_log'] = loc_log
        registros[id]['imagem'] = img
        registros[id]['informacao_adc'] = informacao_adc
        registros[id]['dateTime'] = dateTime
    return registros

def insert_registro_cobra(idRegistro, idCobra, idUsuario):
    insert_query = """INSERT INTO REGISTRO_COBRA (idREGISTRO, IDCOBRA, idUSUARIO)
                    VALUES (%s, %s, %s)"""
    values = (idRegistro, idCobra, idUsuario)
    execute_query(insert_query, values, True)

def delete_registro(idRegistro):
    rowcount = 0
    query = """DELETE FROM REGISTRO WHERE idREGISTRO = %s;"""
    cursor = execute_query(query, [idRegistro], isAlteration = True, rowCount=True)
    if cursor['rowCount'] == 1:
        return 1
    else:
        return 0

def match_login(usuario, senha_cript):
    login = (usuario, senha_cript)

    query = """SELECT COUNT(idUSUARIO) AS Count FROM USUARIO WHERE USUARIO.user = %s AND USUARIO.password = %s"""
    
    cursor = execute_query(query, login)

    for count in cursor['rows']:
        if count[0] == 1:
            return True
        else:
            return False

def novo_usuario(usuario, senha_cript, email):
    values= (usuario, senha_cript, email)

    query = """INSERT INTO USUARIO (user, password, email) VALUES (%s, %s, %s)"""
    cursor = execute_query(query, values, lastRowId=True)
    if cursor['lastRowId'] is not None:
        idRegistro = cursor.lastrowid
    else:
        idRegistro = -1
    return idRegistro

def get_cobra(id):

    query = f"SELECT  COBRA.familia, COBRA.especie, COBRA.peconhenta, COBRA_NOME_POP.nome, FAMILIA.nome, DENTICAO.nome, DENTICAO.descricao, COBRA.tam_max FROM COBRA INNER JOIN COBRA_NOME_POP ON COBRA.idCOBRA = COBRA_NOME_POP.idCOBRA INNER JOIN FAMILIA ON COBRA.grupo = FAMILIA.idFam INNER JOIN DENTICAO ON DENTICAO.idDenticao = COBRA.idDenticao WHERE COBRA.idCOBRA = {id}"

    cursor = execute_query(query)

    info_cobra = {}
    for familia, especie, peconhenta, nome_pop, grupo, denticao, dent_desc, tam_max in cursor['rows']:
        info_cobra['familia'] = familia
        info_cobra['especie'] = especie
        info_cobra['peconhenta'] = peconhenta
        info_cobra['grupo'] = grupo
        info_cobra['denticao'] = denticao
        info_cobra['dent_desc'] = dent_desc
        info_cobra['tam_max'] = tam_max
        if 'nome_pop' not in info_cobra.keys():
            info_cobra['nome_pop'] = []
        info_cobra['nome_pop'].append(nome_pop)

    for filename in os.listdir("./static/serpentesFotos/{} {}".format(info_cobra['familia'], info_cobra['especie'])):
        if 'filenames' not in info_cobra.keys():
            info_cobra['filenames'] = []
        info_cobra['filenames'].append(filename)

    return info_cobra