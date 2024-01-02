from psycopg2 import connect, extensions;
from psycopg2.extras import DictCursor
import os, time

def getConn() -> tuple[extensions.connection, extensions.cursor, extensions.cursor]:
    attemptTime = 5
    hostname = 'postgresDB'
    database = os.getenv('POSTGRES_DB')
    username = os.getenv('POSTGRES_USER')
    pwd = os.getenv('POSTGRES_PASSWORD')
    port_id = 5432

    for attempt in range(attemptTime):
        print(f"attempt to connect {attempt+1}/{attemptTime}")
        try:
            conn = connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
            print("success")
            break
        except:
            time.sleep(2)
            continue
        
    dicCur = conn.cursor(cursor_factory=DictCursor)
    cur = conn.cursor()
    
    return (conn,dicCur,cur)

def close(conn:extensions.connection, dicCur: extensions.cursor, cur: extensions.cursor) -> None:
    conn.close()
    dicCur.close()
    cur.close()