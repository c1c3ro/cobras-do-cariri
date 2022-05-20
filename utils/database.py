import mysql.connector

def get_conn(host = "mysql04-farm2.uni5.net",
            user = "bessapontes23", password = "6qSLjgbR",
            database = "bessapontes23"):
    conn = mysql.connector.connect(host = host,
        user = user,
        password = password,
        database = database)
    return conn

def get_cobras():
    # função que retorna o nome científica das cobras no banco
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