from conn import Conectar


def NovoImigrante():
    print("***************************************")
    print("Cadastrar imigrante")
    print("***************************************")
    print("")

    # solicitando dados do imigrante

    nome = input("Informe o nome")
    nacionalidade = input("Informe a nacionalidade: ")
    dataNascimento = input("Informe a data de nascimento: ")
    documento = input("Informe o documento: ")

    # criando a conexão

    conn = Conectar()
    cursor = conn.cursor()

    # enviar o comando para o banco de dados

    cursor.execute(
        "INSERT INTO IMIGRANTE (NOME, NACIONALIDADE, DT_NASCIMENTO, DOCUMENTO) VALUES (%s, %s, %s, %s)",
        (nome, nacionalidade, dataNascimento, documento)
    )
    # confirmando a inserção no banco de dados
    conn.commit()

    print("")
    print("Imigrante cadastrado com sucesso!")
    # esse comando é para parar a execução do programa até pessionar enter
    input("Pressione enter para continuar...")

    # fechando as coxeções
    cursor.close()
    conn.close()


def ListarTodosImigrantes():
    print("***************************************")
    print("Lista de imigrante")
    print("***************************************")
    print("")

    # criando a conexão
    conn = Conectar()
    cursor = conn.cursor()

    # enviar o comando para o banco de dados

    cursor.execute(
        "SELECT IDIMIGRANTE, NOME, NACIONALIDADE, DT_NASCIMENTO, DOCUMENTO FROM IMIGRANTE")

    # ercorrendo o resultado e mostrando em tela

    for id, nome, nacionalidade, dt_nascimento, documento in cursor.fetchall():
        print(f"{id} - {nome} = {nacionalidade} - {dt_nascimento} - {documento}")

        cursor.close()
        conn.close()
