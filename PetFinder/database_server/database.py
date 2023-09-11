from psycopg2 import connect, extensions;
from psycopg2.extras import DictCursor

def getConn() -> tuple[extensions.connection, extensions.cursor, extensions.cursor]:
    hostname = 'localhost'
    database = 'petfinder'
    username = 'postgres'
    pwd = 'peng2008'
    port_id = 5432

    conn = None
    dicCur = None
    cur = None

    try:
        conn = connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)
        dicCur = conn.cursor(cursor_factory=DictCursor)
        cur = conn.cursor()
    except Exception as error:
        print(error)
        raise Exception()
    return (conn,dicCur,cur)

def close(conn:extensions.connection, dicCur: extensions.cursor, cur: extensions.cursor) -> None:
    conn.close()
    dicCur.close()
    cur.close()
        # create_script = '''
        #     CREATE TABLE IF NOT EXISTS employee(
        #     id      int PRIMARY KEY,
        #     name    VARCHAR(40) NOT NULL,
        #     salary  int,
        #     dept_id VARCHAR(30))
        # '''
        # cur.execute(create_script)

        # insert_script = 'INSERT INTO employee (id, name, salary, debt_id) VALUES (%s, %s, %s, %s)'
        # insert_value = (1, 'James', 12000, 'D1')
        # cur.execute(insert_script, insert_value)
        # cur.execute('DROP TABLE employee')

        # conn.commit()


# types = ['cat', 'dog', 'bird']
# conn, dicCur, cur = getConn()
# cur.execute('DROP TABLE IF EXISTS types;')
# cur.execute('''
#     CREATE TABLE types(
#             type            VARCHAR(20),
#             totalPages      INT
#     );
# ''')
# for item in types:
#     cur.execute(f'DROP TABLE IF EXISTS {item}')
#     cur.execute('INSERT INTO types(type, totalPages) VALUES(%(t)s, 3)', {'t': item})
#     cur.execute(f'''
#         CREATE TABLE {item}(
#                 id              INT PRIMARY KEY,
#                 name            VARCHAR(50),
#                 type            VARCHAR(50) DEFAULT '{item}',
#                 page            INT,
#                 description     TEXT,
#                 smallImage      TEXT,
#                 fullImage       TEXT
#         )
#     ''')
# conn.commit()
# cur.execute('SELECT * FROM types')
# for item in cur.fetchall():
#     print(item)
# dicCur.execute('SELECT * FROM types')
# for item in dicCur.fetchall():
#     print(item, type(item))

# print("")
# for item in [{'a':1, 'b':2, 'c':3},{'d':4, 'e':5, 'f':6}]:
#     print(item, type(item))

# print(type(cur))