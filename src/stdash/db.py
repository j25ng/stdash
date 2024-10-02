import pymysql
import os

def get_conn():
    db_host = os.getenv("DB_IP", "localhost")
    db_port = os.getenv("DB_PORT", 53306)
    conn = pymysql.connect(
            host = db_host,
            port = int(db_port),
            user = 'mnist',
            passwd = '1234',
            db = 'mnistdb',
            cursorclass=pymysql.cursors.DictCursor)

    return conn

def dml(sql, *values):
  conn = get_conn()

  with conn:
    with conn.cursor() as cursor:
        cursor.execute(sql, values)
        conn.commit()
        return cursor.rowcount
