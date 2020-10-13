import os
import shutil


def open_file(file, method):
    """
    Retorna a instância de um arquivo
    :param file: Caminho com o nome do arquivo
    :param method: Forma de abertura
    :return: IO Instância do arquivo
    """
    return open(get_path(file), method)


def get_path(file="") -> str:
    """
    Retorna o nome do diretório atual para manipulação dos arquivos
    :param file: Nome do diretório - caso seja passado uma string vazia, retorna o diretório roots
    :return: Caminho do arquivo
    """
    return os.path.abspath(file)


def check_storage():
    """
    Verifica se o pacote de armazenamento existe
    :return: None
    """

    try:
        if not os.path.exists(get_path('../storage')):
            os.mkdir('../storage')
    except Exception as e:
        from functions import get_error
        get_error(e)


def delete_data(user_id) -> bool or None:
    """
    Apaga os arquivos exportados de um usuário
    :param user_id: ID do usuário (mesmo ID do spotify)
    :return: bool verdadeiro em caso de sucesso ou None em caso de erro
    """

    try:
        # Verifica se o usuário possui arquivos exportados
        if os.path.exists(get_path(f"./storage/{user_id}")):
            # Caso possua, exclui todos os arquivos exportados dele
            shutil.rmtree(get_path(f"./storage/{user_id}"))
        # Tendo ou não arquivos exportados, retorna True como forma de indicar que o usuário não possui mais nada armazenado
        return True
    except Exception as e:
        from functions import get_error
        return get_error(e)
