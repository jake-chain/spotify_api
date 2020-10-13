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
