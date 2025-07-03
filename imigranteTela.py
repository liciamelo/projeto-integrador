import os
from imigrante import NovoImigrante, ListarTodosImigrantes


def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')


def ImigranteMenu():
    while True:

        # limpando a tela
        LimpaTela()

        # criando o menu imigrante
        print(" === Menu Imigrante ===")
        print("1. Cadastrar imigrante")
        print("2. Listar imigrante")
        print("9. Sair")

        opcao = input("Escolha uma opção:")

        if opcao == '1':
            NovoImigrante()
        elif opcao == '2':
            ListarTodosImigrantes()
            input("Pressione enter para continuar...")
        elif opcao == '9':
            break
        else:
            print("Opção invalida")
