from functions import get_error

data_access = {
    'user': "root",
    'passwd': "123456",
    'host': "localhost",
    'db': "spotifyapi",
}


# Realiza a conexão com o banco de dados e retorna a instância da conexão
def connect():
    try:
        import MySQLdb
        return MySQLdb.connect(user=data_access['user'], passwd=data_access['passwd'], host=data_access['host'], db=data_access['db'])
    except Exception as e:
        return get_error(e)


# Realiza uma consulta no banco de dados
def select(script, param=None, featchone=False, featchmany=None):
    try:
        # Abrindo conexão com o banco de dados
        database = connect()
        # Capturando a instância do cursor
        cursor = database.cursor()
        # Executando o insert
        cursor.execute(script, param)

        if featchone:
            # Lendo os resultados
            response = cursor.fetchone()
            # Fechando conexão com o banco de dados
            database.close()
            # Retornando os resultados
            return response
        elif featchmany is not None:
            # Lendo os resultados
            response = cursor.fetchmany(int(featchmany))
            # Fechando conexão com o banco de dados
            database.close()
            # Retornando os resultados
            return response
        else:
            # Lendo os resultados
            response = cursor.fetchall()
            # Fechando conexão com o banco de dados
            database.close()
            # Retornando os resultados
            return response
    except Exception as e:
        return get_error(e)


# Realiza a inserção de dados no banco
def insert(script, param=None) -> int or bool:
    try:
        # Abrindo conexão com o banco de dados
        database = connect()
        # Capturando a instância do cursor
        cursor = database.cursor()
        # Executando o insert
        cursor.execute(script, param)
        # Salvando os dados
        database.commit()
        # Fechando a conexão com a base de dados
        database.close()
        # Retorna o ID criado
        return cursor.lastrowid
    except Exception as e:
        return get_error(e)
