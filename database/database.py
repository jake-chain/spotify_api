from functions import get_error

data_access = {
    'user': "root",
    'passwd': "123456",
    'host': "localhost",
    'db': "spotifyapi",
}


def connect():
    try:
        import MySQLdb
        return MySQLdb.connect(user=data_access['user'], passwd=data_access['passwd'], host=data_access['host'], db=data_access['db'])
    except Exception as e:
        return get_error(e)


def select(script, param=None, featchone=False, featchmany=None):
    try:
        database = connect()
        cursor = database.cursor()
        cursor.execute(script, param)

        if featchone:
            response = cursor.fetchone()
        elif featchmany is not None:
            response = cursor.fetchmany(int(featchmany))
        else:
            response = cursor.fetchall()

        database.close()
        return response
    except Exception as e:
        return get_error(e)


def execute_script(script: str, param: tuple = None, returning_id: bool = False) -> bool or None:
    try:
        database = connect()
        cursor = database.cursor()
        cursor.execute(script, param)
        database.commit()
        database.close()
        return cursor.lastrowid if returning_id else True
    except Exception as e:
        return get_error(e)


def insert(script: str, param: tuple) -> int or bool or None:
    try:
        return execute_script(script, param)
    except Exception as e:
        return get_error(e)


def update(table: str, columns: str, where: str, param: tuple) -> bool or None:
    try:
        return execute_script(f"UPDATE {table} SET {columns} WHERE {where}", param)
    except Exception as e:
        return get_error(e)


def delete(table: str, where: str) -> bool or None:
    try:
        return execute_script(f"DELETE FROM {table} WHERE {where}")
    except Exception as e:
        return get_error(e)
