from psycopg2 import connect, extensions;
from psycopg2.extras import DictCursor

def getConn() -> tuple[extensions.connection, extensions.cursor, extensions.cursor]:
    hostname = 'localhost'
    database = 'petfinder'
    username = 'user'
    pwd = '1234'
    port_id = 5432

    conn = connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)
    dicCur = conn.cursor(cursor_factory=DictCursor)
    cur = conn.cursor()
    
    return (conn,dicCur,cur)

def close(conn:extensions.connection, dicCur: extensions.cursor, cur: extensions.cursor) -> None:
    conn.close()
    dicCur.close()
    cur.close()