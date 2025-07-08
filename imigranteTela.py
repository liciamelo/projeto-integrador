import os
from imigrante import NovoImigrante, ListarTodosImigrantes, DetalheImigrante, AlterarImigrante, ExcluirImigrante


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
        print("3 - Ver datalhes do imigrante")
        print("4 - Alterar imigrante")
        print("5 - Excluir imigrante")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # chamando o metodo que cadastra um novo imigrante
            NovoImigrante()
            # chamando o metodo pra listar todos os imigrantes
        elif opcao == '2':
            ListarTodosImigrantes()
            input("Pressione enter para continuar...")
        elif opcao == '3':
            # chamando o metodo que lista todos os imigrantes para que o usuario escolha um
            ListarTodosImigrantes()
            id = input("Informe o id do imigrante para ver detalhes: ")
        elif opcao == '4':
           # chamando o metodo para listar todos os iigrantes para escolher um
            ListarTodosImigrantes()
            print("")
            id = input("Informe o id do imigrante para alterar: ")
            AlterarImigrante(id)
            # chamando o metodo que mostra os detalhes do imigrante
            DetalheImigrante(id)
        elif opcao == '5':
            ExcluirImigrante()
            id = input("Informe o id do imigrante para excluir: ")
        elif opcao == '9':
            break
        else:
            print("Opção invalida")
