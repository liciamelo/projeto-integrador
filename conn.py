import mysql.connector


def Conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='DBPROJETO_INTEGRADOR'
    )


conn = Conectar()
conn.close()
