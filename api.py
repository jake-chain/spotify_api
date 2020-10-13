import requests
import functions
from models.Playlist import Playlist
from models.Track import Track


def get_header(token: str) -> dict:
    """
    Apenas retorno dos dados do cabeçalho da consulta aplicando o token passado nos parâmetros
    :param token: Código de acesso à conta do usuário
    :return: header da requisição
    """
    return {
        'Accept': "application/json",
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + token
    }


def made_request(url, token) -> requests.Response:
    """
    Realiza a requisição à API
    :param url: URL da consulta
    :param token: Código de acesso à conta do usuário
    :return: Response
    """
    return requests.get(url, headers=get_header(token))


def get_tracks(token) -> dict or None:
    """
    Consulta as músicsa de um determinado usuário
    :param token: Código de acesso à conta do usuário
    :return:
    """
    try:
        tracks = {}  # Variável de retorno da função
        current = 0  # Contagem da quantidade de músicas encontradas
        offset = 0  # Offset da consulta para buscar todos os dados
        total = 1  # Total de músicas retornadas da consulta

        # Enquanto não consultar todas as músicas, não interrompe a consulta
        while current <= total:
            funded_something_track = False

            # Configurando a URL
            url = "https://api.spotify.com/v1/me/tracks?offset={0}".format(offset)

            # Realizando a consulta
            response = made_request(url, token)
            # Convertendo o resultado de json pra dicionário
            data = response.json()

            if 'error' in data:
                print(data['error']['message'])
                return []

            # Verificando se existe a informação da quantidade de músicas encontradas na consulta
            if 'total' in data:
                total = data['total']

            # Verificando se retornou alguma música da consulta
            if 'items' in data:
                # Percorrendo as músicas retornadas
                for item in data['items']:
                    funded_something_track = True
                    current += 1
                    offset += 1

                    # Console
                    functions.clear_terminal()
                    print("{0} músicas encontradas na sua biblioteca".format(current))

                    # Consultando os artistas que participam da música
                    artists = ""
                    for artist in item['track']['artists']:
                        artists += artist['name'] if artists == "" else ", " + artist['name']

                    # Atribuindo os valores no dicionário
                    tracks[item['track']['id']] = Track(item['track']['id'], item['track']['name'], artists, item['track']['album']['name'])
            else:
                # Se não retornou nada, interrompe a consulta não manter um loop infinito na execução
                break

            # Verifica se a quantidade de músicas teve alteração, se não, interrompe a consulta para impedir loop infinito
            if not funded_something_track:
                break

        # Retornando as músicas encontradas
        return tracks
    except Exception as e:
        return functions.get_error(e)


def get_playlists(user_id, token) -> dict or None:
    """
    Consulta as playlists do usuário
    :param user_id: ID do usuário no Spotify
    :param token: Código de acesso à conta do usuário
    :return:
    """
    try:
        playlists = {}  # Variável de retorno da função
        current = 0  # Contagem da quantidade de músicas encontradas
        offset = 0  # Offset da consulta para buscar todos os dados
        total = 1  # Total de músicas retornadas da consulta

        # Enquanto não consultar todas as playlists, não interrompe a consulta
        while current <= total:
            funded_something_playlist = False

            # Configurando a URL
            url = "https://api.spotify.com/v1/users/{0}/playlists?limit=10&offset={1}".format(user_id, offset)

            # Realizando a consulta
            response = made_request(url, token)
            # Convertendo o resultado de json pra dicionário
            data = response.json()

            if 'error' in data:
                print(data['error']['message'])
                return []

            # Verificando se existe a informação da quantidade de músicas encontradas na consulta
            if 'total' in data:
                total = data['total']

            # Verificando se retornou alguma música da consulta
            if 'items' in data:
                # Percorrendo as músicas retornadas
                for item in data['items']:
                    funded_something_playlist = True
                    current += 1
                    offset += 1

                    # Console
                    functions.clear_terminal()
                    print("{0} playlists encontradas".format(current))

                    # Atribuindo os valores no dicionário
                    playlists[item['id']] = Playlist(item['id'], item['name'])
            else:
                # Se não retornou nada, interrompe a consulta não manter um loop infinito na execução
                break

            # Verifica se a quantidade de músicas teve alteração, se não, interrompe a consulta para impedir loop infinito
            if not funded_something_playlist:
                break

        # Retorno das playlists encontradas
        return playlists
    except Exception as e:
        return functions.get_error(e)


def get_tracks_by_playlist(playlist_id, token) -> dict or None:
    """
    Consulta as músicsa de uma determinada playlist
    :param playlist_id: ID da playlist no Spotify
    :param token: Código de acesso à conta do usuário
    :return:
    """
    try:
        tracks = {}  # Variável de retorno da função
        # Configurando a URL
        url = "https://api.spotify.com/v1/playlists/" + playlist_id

        # Configurando o cabeçalho
        headers = get_header(token)

        # Realizando a consulta
        response = requests.get(url, headers=headers)
        # Convertendo o resultado de json pra dicionário
        data = response.json()

        if 'error' in data:
            print(data['error']['message'])
            return []

        # Verificando se retornou alguma música da consulta
        if 'tracks' in data:
            if 'items' in data['tracks']:
                # Percorrendo as músicas retornadas
                for item in data['tracks']['items']:
                    if 'track' in item:
                        # Atribuindo os valores no dicionário
                        tracks[item['track']['id']] = item['track']['name']

        # Retorna a playlist modificada
        return tracks
    except Exception as e:
        return functions.get_error(e)
