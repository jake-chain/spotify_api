import json
import os
import shutil

# Retorna a instancia da abertura do arquivo
import time


def open_file(file, method):
    return open(get_path(file), method)


# Verifica se o pacote de armazenamento existe
def check_storage():
    if not os.path.exists(get_path('storage')):
        os.mkdir('storage')


# Retorna o nome do diretório atual para manipulação dos arquivos
def get_path(file="") -> str:
    return os.path.abspath(file)


# Apaga os registros de um usuário
def delete_data(user_id) -> bool:
    if os.path.exists(get_path(f"./storage/{user_id}")):
        shutil.rmtree(get_path(f"./storage/{user_id}"))
        return True
    else:
        return False


# Leitura dos dados do usuário e populando as variáveis
def reader_files(user) -> dict:
    # Armazena os dados retornados da função
    data = {
        'tracks': {},
        'playlists': {},
    }

    try:
        # Verifica se o diretório di usuário existe
        if not os.path.exists(get_path("./storage/" + user.get_user_id())):
            # Se não existe cria o diretório
            os.mkdir(get_path("./storage/" + user.get_user_id()))
        else:
            # Verificando o arquivo das músicas
            if os.path.exists(get_path(f"./storage/{user.get_user_id()}/tracks.dat")):
                # Leitura do arquivo de músicas
                tracks_file = open(get_path(f"./storage/{user.get_user_id()}/tracks.dat"), 'r')
                data['tracks'] = json.loads(tracks_file.read())
                tracks_file.close()

            # Verificando o arquivo das playlists
            if os.path.exists(get_path(f"./storage/{user.get_user_id()}/playlists.dat")):
                # Leitura do arquivo de playlists
                playlists_file = open(get_path(f"./storage/{user.get_user_id()}/playlists.dat"), 'r')
                data['playlists'] = json.loads(playlists_file.read())
                playlists_file.close()
    except Exception as erro:
        file_log = open_file('logs', 'a')
        file_log.write("Hora: " + time.strftime("%H:%M:%S") + "\nError: " + str(erro) + "\n\n")
        file_log.close()

    return data
