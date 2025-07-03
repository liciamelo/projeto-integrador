import os
from imigranteTela import ImigranteMenu


def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')


def Menu():
    while True:

        # limpando a tela
        LimpaTela()

        # criando o menu princiapl
        print(" === Menu principal ===")
        print("1. Imigrante")
        print("2. Informação complementar do imigrante")
        print("3. Serviço de apoio")
        print("9. Sair")

        opcao = input("Escolha uma opção:")

        if opcao == '1':
            ImigranteMenu()
        elif opcao == '2':
            print("Opção complementar")
        elif opcao == '3':
            print("Opção Serviços")
        elif opcao == '9':
            print("Obrigado por utilizar esse aplicativo")
            break
        else:
            print("Opção invalida")


if __name__ == "__main__":
    Menu()
