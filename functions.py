import os
import time
import api
from files import files


def exe_commant(commant, user) -> bool:
    if commant == "update_tracks":
        user.set_tracks(update_tracks(user.get_token()))
        return True
    elif commant == "update_playlists":
        user.set_playlists(update_playlists(user.get_user_id(), user.get_token()))
        return True
    elif commant == "show_tracks":
        return False
    elif commant == "show_playlists":
        return False
    elif commant == "exit":
        exit()
    elif commant == "delete":
        if files.delete_data(user.get_user_id()) is not None:
            return True
        else:
            return False
    elif commant == "help":
        print("Comandos dispobíveis:\nupdate_tracks\nupdate_playlists\nshow_tracks\nshow_playlists\ndelete\nexit")
    else:
        print("Comando inválido")
        exe_commant("help", user)


def update_tracks(token) -> dict or bool:
    """
    Atualiza as músicas de um determinado usuário
    :param token: Código de acesso à conta do usuário
    :return:
    """
    try:
        return api.get_tracks(token)
    except Exception as e:
        return get_error(e)


def update_playlists(user_id, token) -> dict or None:
    """
    Atualiza as playlists e músicas em playlists de um determinado usuário
    :param user_id: ID do usuário (mesmo ID do Spotify)
    :param token: Código de acesso à conta do usuário
    :return: Lista de músicas do usuário ou um None em caso de falha
    """
    try:
        # Consultando todas as playlists
        playlists = api.get_playlists(user_id, token)
        # Consultando as músicas das playlists
        for playlist_id, playlist in playlists.items():
            playlist.set_tracks(api.get_tracks_by_playlist(playlist_id, token))
        # Retorno da função
        return playlists
    except Exception as e:
        return get_error(e)


def get_error(erro: Exception) -> None:
    """
    Tratamento de erros e geração do arquivo de log
    :param erro: Exception
    :return: None
    """
    file_log = files.open_file('logs', 'a')
    date_time = time.strftime("%H:%M:%S")
    file_log.write(f"Hora: {date_time} [{get_so(True)}]\nError: {str(erro)}\n{'=' * 120}\n")
    file_log.close()
    return None


def clear_terminal():
    """
    Apenas limpa o terminal
    :return: None
    """
    os.system('CLS') if get_so() == 'W' else os.system('clear')


def get_so(getting_name: bool = False) -> str:
    """
    Retorna o código ou o nome do sistema operacional atual
    No caso, o sistema que a aplicação está sendo executada
    :param getting_name: Se o retorno da função será apenas o código do SO ou o nome
    :return: Nome do SO ou o código, podendo ser: ['W', 'L', 'Windows', 'Linux']
    """
    if getting_name:
        return 'Windows' if os.name == 'nt' else 'Linux'
    else:
        return 'W' if os.name == 'nt' else 'L'
