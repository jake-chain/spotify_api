import functions
from models.User import User

if __name__ == "__main__":
    # Limpa o terminal para uma melhor visualização
    functions.clear_terminal()

    # Leitura dos dados do usuário
    user = User.read_info()

    # Listener para aguardar instruções do usuário
    functions.clear_terminal()
    while True:
        print(f"\n{'=' * 66}")
        print("Digite help para mais informações")
        commant = input("Aguardando comando: ")
        functions.exe_commant(commant, user)
