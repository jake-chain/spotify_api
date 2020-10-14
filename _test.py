import random
import string
from random import randint

"""
===============================================================================
"""


def multiplication_table(min_multiplier: float = 1, max_multiplier: float = 10, min_multiplying: float = 1, max_multiplying: float = 10) -> str:
    """
    Função que retorna a tabuada de acordo com as configurações de parâmetro
    :param min_multiplier: valor inicial do multiplicador
    :param max_multiplier: valor máximo do multiplicador
    :param min_multiplying: valor inicial do multiplicando
    :param max_multiplying: valor máximo do multiplicando
    :return:
    """

    # Variável para armazenar a tabela que será retornada (em forma de string)
    table = ""
    # Dado o valor inicial do multiplizador da tabela, é percorrido até alcançar o seu valor máximo
    while min_multiplier <= max_multiplier:
        # Adicionando separador para identação da tabela
        table += "| "
        # Variável temporária para armazenar o valor inicial do multiplicando (isso para não perder o valor original)
        temp_min_multiplying = min_multiplying
        # Dado o valor inicial do multiplicando, é percorrido até alcançar o seu valor máximo
        while temp_min_multiplying <= max_multiplying:
            # Adicionando a linha à variável de retorno
            table += f"{temp_min_multiplying:^3} * {min_multiplier:^3} = {min_multiplier * temp_min_multiplying:^3} | "
            # Incrementando +1 na variável de index
            temp_min_multiplying += 1
        # Apenas uma quebra de linha para a tabela
        table += "\n"
        min_multiplier += 1
    return table


def division_table(min_dividend: float = 1, max_dividend: float = 10, min_divider: float = 1, max_divider: float = 10) -> str:
    """
    Função que retorna a tabuada de divisão de acordo com as configurações de parâmetro
    :param min_dividend: valor inicial do dividendo
    :param max_dividend: valor máximo do dividendo
    :param min_divider: valor inicial do divisor
    :param max_divider: valor máximo do divisor
    :return:
    """

    # Variável para armazenar a tabela que será retornada (em forma de string)
    table = ""
    # Dado o valor inicial do multiplizador da tabela, é percorrido até alcançar o seu valor máximo
    while min_dividend <= max_dividend:
        # Adicionando separador para identação da tabela
        table += "| "
        # Variável temporária para armazenar o valor inicial do multiplicando (isso para não perder o valor original)
        temp_min_multiplying = min_divider
        # Dado o valor inicial do multiplicando, é percorrido até alcançar o seu valor máximo
        while temp_min_multiplying <= max_divider:
            # Adicionando a linha à variável de retorno
            table += f"{min_dividend * temp_min_multiplying:^3}/{temp_min_multiplying:^3}={min_dividend:^3} | "
            # Incrementando +1 na variável de index
            temp_min_multiplying += 1
        # Apenas uma quebra de linha para a tabela
        table += "\n"
        min_dividend += 1
    return table


"""
===============================================================================
"""


def convert_objects_to_dict(list_objects: dict) -> dict:
    """
    Nessa função, é recebido um dict de objects e retorna em formato de dict de dict
    Ou seja, ele converte os objects do dict em dict
    :param list_objects: dict com os dados a serem convertidos
    :return:
    """

    # Varipavel usada para armazenar o retorno da função
    converted_data = {}
    # Percorrendo o dict para capturar os objects
    for key, current_object in list_objects.items():
        # Convetendo o object para dict
        converted_data[key] = current_object.__dict__
    # Retorno da função
    return converted_data


def teste_dict_of_objects_to_dict_of_dict():
    """
    teste para a função de retorno de um dict de objetos para um dict de dict
    :return: None
    """

    # Classe de teste
    class Teste(object):
        def __init__(self, class_id, name) -> None:
            self.__class_id = class_id
            self.__name = name

    # Criando o dict com vários objetos
    dict_of_object = {
        'id_01': Teste('id_01', "teste 01"),
        'id_02': Teste('id_01', "teste 02"),
        'id_03': Teste('id_01', "teste 03"),
        'id_04': Teste('id_01', "teste 04"),
    }

    # Imprimindo para teste
    print("Essa é a impressão normal do Python para dicionários com objetos")
    print(dict_of_object)
    print("\nEssa é a impressão usando a função de conversão")
    print(convert_objects_to_dict(dict_of_object))


"""
===============================================================================
"""


def caca_palavras():
    # Primeiro define o tamanho que será a matriz
    linhas = 15  # Quantidade de linhas
    colunas = 15  # Quantidade de colunas

    matriz = []  # Variável que irá armazenar a matriz

    # Definindo as palavras que terá no caça palavras
    palavras = ["rafaela", "apenas", "quero", "dizer", "vai", "dormir", "precisa", "descansar"]

    # 1 - inicia as posições da matriz todas vazias
    # Primeiro laço de repetição para iniciar as linhas
    for linha in range(linhas):
        # Em cada linha, insere um vetor, tornando em uma matriz
        matriz.append([])
        # Segundo laço de repetição para iniciar as colunas
        for coluna in range(colunas):
            matriz[linha].append("")

    # 2 - Percorre as palavras definidas anteriormente para coloca-lás na matriz
    for palavra in palavras:
        # Gera a posição inicial em que a palavra será colocada
        position = gera_posicao(matriz, palavra, linhas, colunas)
        linha = position['linha']
        coluna = position['coluna']

        # Para cada caractere contida na palavra, coloca em uma posição diferente da matriz
        for caractere in palavra:
            matriz[linha][coluna] = caractere
            coluna += 1

    # 3 - Preenchendo os espaços vagos da matriz por letras aleatórias
    for linha in range(linhas):
        for coluna in range(colunas):
            if matriz[linha][coluna] == "":
                # Gerando uma letra aleatória e inserindo na matriz
                matriz[linha][coluna] = ''.join(random.choices(string.ascii_uppercase, k=1))
                # Apenas para teste
                matriz[linha][coluna] = '-'

    # 4 - Exibindo a matriz
    print_matriz(matriz)


def print_matriz(matriz):
    # Inicia a variável que guardará a matriz
    str_matriz = ""
    # Percorrendo as linhas
    for i in range(len(matriz)):
        # Percorrendo as colunas
        for j in range(len(matriz[i])):
            # Gerando a linha da matriz
            str_matriz += f" {matriz[i][j]} "
        # Inserindo uam quebra de linha para passar para próxima linha da matriz
        str_matriz += "\n"
    # Imprimindo a variável que contêm a matriz
    print(str_matriz)


def gera_posicao(matriz, palavra, quantidade_linhas, quantidade_colunas):
    while True:
        # Apenas gera um número aleatória para a linha, o valor está entre 0 e a quantidade de colunas da matriz - 1
        # (se a matriz contêm 10 colunas, a posição inicial sendo 0, o valor gerado deve ser até 9)
        linha = randint(0, quantidade_linhas - 1)

        coluna = randint(0, quantidade_colunas - 1)
        while True:
            # Se a posição inicial somada com o tamanho da palavra não ultrapassar o tamanho da matriz, então esse posição pode usada
            if coluna + len(palavra) < quantidade_colunas:
                break
            # Se a coluna não pode ser usada, gera um novo valor
            coluna = randint(0, quantidade_colunas - 1)

        # Verifica se algumas posição gerada para a pavra está preenchida
        usada = False
        for coluna_atual in range(quantidade_colunas):
            if matriz[linha][coluna_atual] != "":
                usada = True

        # Se não tá sendo usada, retorna as posições
        if not usada:
            return {
                'linha': linha,
                'coluna': coluna
            }


def gera_posicao_recursiva(matriz, palavra, linhas, colunas):
    # Apenas gera um número aleatória para a linha, o valor está entre 0 e a quantidade de colunas da matriz - 1
    # (se a matriz contêm 10 colunas, a posição inicial sendo 0, o valor gerado deve ser até 9)
    linha = randint(0, colunas - 1)
    # Usa a função para gerar a posição inicial da palavra
    coluna = sei_la_recursivo(len(palavra), linhas)

    # Verifica se algumas posição gerada para a pavra está preenchida
    usada = False
    for coluna_atual in range(colunas):
        if matriz[linha][coluna_atual] != "":
            usada = True

    # Se alguma posição já tá sendo usada, tenta de novo chamando a mesma função
    if usada:
        return gera_posicao(matriz, palavra, linhas, colunas)
    else:
        # Se não tá sendo usada, retorna as posições
        return {
            'linha': linha,
            'coluna': coluna
        }


def sei_la_recursivo(tamanho_palavra, tamanho_maximo):
    # Apenas gera um número aleatória para a linha, o valor está entre 0 e a quantidade de colunas da matriz - 1
    # (se a matriz contêm 10 colunas, a posição inicial sendo 0, o valor gerado deve ser até 9)
    linha = randint(0, tamanho_maximo - 1)
    # Se a posição inicial somada com o tamanho da palavra não ultrapassar o tamanho da matriz, então esse posição pode usada
    if linha + tamanho_palavra < tamanho_maximo:
        return linha
    else:
        # Mas se ultrapassar o tamanho da matriz, então tenta gerar uma nova posição
        return sei_la_recursivo(tamanho_palavra, tamanho_maximo)


caca_palavras()
