class User(object):
    # Construtor da classe
    def __init__(self, user_id, username, name, token=None, tracks=None, playlists=None):
        # Verificando o parametro das músicas
        if tracks is None:
            tracks = {}

        # Verificando o parâmetro da playlist
        if playlists is None:
            playlists = {}

        # Atribuindo os dados
        self.__user_id = user_id
        self.__username = username
        self.__name = name
        self.__token = token
        self.__tracks = tracks
        self.__playlists = playlists

    """
    Métodos de GET
    """

    def get_user_id(self):
        return self.__user_id

    def get_username(self):
        return self.__username

    def get_name(self):
        return self.__name

    def get_token(self):
        return self.__token

    def get_tracks(self):
        return self.__tracks

    def get_playlists(self):
        return self.__playlists

    def set_user_id(self, user_id):
        self.__user_id = user_id

    """
    Métodos de SET
    """

    def set_username(self, username):
        self.__username = username

    def set_name(self, name):
        self.__name = name

    def set_token(self, token):
        self.__token = token

    def set_tracks(self, tracks):
        if tracks is None:
            tracks = {}
        self.__tracks = tracks

    def set_playlists(self, playlists):
        if playlists is None:
            playlists = {}
        self.__playlists = playlists

    """
    Sobrescrita do str
    """

    def __str__(self) -> str:
        return str(self.__dict__)

    """
    Métodos estáticos
    """

    # Lê o token de acesso ao spotify
    @staticmethod
    def reader_token():
        print("\nAcesse: https://developer.spotify.com/console/get-current-user-saved-tracks/ e clique 'GET TOKEN'")
        print(
            "Será necessário permissão para:"
            "\n* user-library-read               leitura das músicas em sua biblioteca"
            "\n* playlist-read-private           leitura das suas platlits privadas"
            "\n* playlist-read-collaborative     leitura das suas playlists colaborativas\n"
        )
        print("Nenhuma informação é compartilhada. Apenas consultamos os dados. Não mudamos nada")
        return input("Informe o token de acesso: ")

    # Lê os dados do usuário para consultar as informalções no banco de dados e retornar a instância do usuário
    # Caso não tenha registro referente a esse usuário no banco de dados, libera a opção de criar um novo registro
    @staticmethod
    def read_info():
        from database.database import select

        # Leitura do ID do usuário
        username = input("Informe o ID do usuário: ")
        # Verificando se o usuário existe na base de dados
        user = select("SELECT * FROM users WHERE username = %s", (username,), True)

        # Se o usuário não existe, solicita a criação dele
        if user is None:
            # Importação da função de limpar o terminal
            from functions import clear_terminal

            # Lendo a escolha do usuário: se deseja tentar novamente ou criar um novo usuário
            response = input("Usuário não encontrado na base de dados. Deseja criar um novo agora ou tentar com outro id? (New/Try)\n")

            # Verifica a resposta do usuário
            if response.lower() == "n" or response.lower() == "new":
                # Limpa o terminal
                clear_terminal()
                # Chama a função para criar um novo usuário
                return User.create_user()
            else:
                # Limpa o terminal
                clear_terminal()
                # Chama novamente a função (recursivdmente)
                return User.read_info()
        else:
            # Cria a instância do usuário e retorna ele
            return user

    # Lê os dados do usuário e cria um novo registro na base de dados
    @staticmethod
    def create_user():
        # Instâcia de retorno
        user = None

        # Leitura do nome do usuário
        username = input("Informe o seu ID do Spotify: ")
        name = input("Informe o seu nome: ")

        import database
        # Tenta salvar o registro na base de dados
        user_id = database.insert("INSERT INTO users (username, name) VALUES (%s, %s)", (username, name))
        if user_id:
            # Informa ao usuário que foi registrado com sucesso
            print("Dados gravados com sucesso!")
            # Cria a instância do usuário e a retorna
            user = User(user_id, username, name)
        else:
            # Informa ao usuário que ocorreu um erro
            try_again = input("Ocorreu um erro inesperado. Deseja tentar novamente? (Yes/No)\n")

            # Caso o usuário tenha optado por tentar novamente, chama a função
            if try_again.lower() == "yes" or try_again.lower() == "y":
                user = User.create_user()

        # Verifica se o usuário quer atualizar as informações
        check_token = input("Deseja informar o token de acesso ao Spotify agora e já importar seus dados? (Yes/No)\n")

        # Caso o usuário informe sim, que deseja atualizar, consulta os dados e já popula as tabelas
        if check_token.lower() == "yes" or check_token.lower() == "y":
            # Leitura do token
            User.reader_token()

        return user
