import functions
from models.User import User

if __name__ == "__main__":
    functions.clear_terminal()

    # Leitura dos dados do usuário
    user = User.__init_by_list__(list(User.read_info()))

    functions.clear_terminal()

    while True:
        print(f"\n{'=' * 66}")
        print("Digite help para mais informações")
        commant = input("Aguardando comando: ")
        functions.exe_commant(commant, user)
