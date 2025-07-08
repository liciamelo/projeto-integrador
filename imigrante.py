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


def DetalheImigrante(id):
    print("***************************************")
    print("Cadastrar imigrante")
    print("***************************************")
    print("")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()

    # a vírgula no final é pro py entender que é uma lista
    cursor.execute(
        'SELECT IDIMIGRANTE, NOME, NACIONALIDADE, DT_NASCIMENTO, DOCUMENTO FROM IMIGRANTE WHERE IDIMIGRANTE = %s', (id,))
    for id, nome, nacionalidade, dt_nascimento, documento in cursor.fetchall():
        print(f"ID: {id}")
        print(f"Nome: {nome}")
        print(f"Nacionalidade: {nacionalidade}")
        print(f"Data de Nascimento: {dt_nascimento}")
        print(f"Documento: {documento}")
        print("")

    cursor.close()
    conn.close()

    input("Pressione enter para voltar ao menu")


def AlterarImigrante(id):
    print("***************************************")
    print("Alterando imigrante")
    print("***************************************")
    print("")

    print("Informe os novos valores do imigrante: ")
    nome = input("Informe o nome")
    nacionalidade = input("Informe a nacionalidade: ")
    dt_nascimento = input("Informe a data de nascimento: ")
    documento = input("Informe o documento: ")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()

    # enviando o comando para o banco de dados para alterar o imigrante
    cursor.execute("UPDATE IMIGRANTE SET NOME = %s, NACIONALIDADE = %s, DT_NASCIMENTO = %s, DOCUMENTO = %s WHERE IDIMIGRANTE = %s",
                   (nome, nacionalidade, dt_nascimento, documento, id))

    conn.commit()

    conn.close()
    conn.close()

    print("Imigrante atualizado com suceso")
    input("Pressione enter para voltar ao menu")


def ExcluirImigrante(id):
    print("***************************************")
    print("Excluindo imigrante")
    print("***************************************")
    print("")

    confirmar = input(
        "Deseja realmente excluir o imigrante? (informe 1 para confirmar: ")
    if (confirmar == '1'):
       # criando conexao
        conn = Conectar()
        cursor = conn.cursor()

    # enviando comando sql para excluir o imigrante
    cursor.execute("DELETE FROM IMIGRANTE WHERE IDIMIGRANTE = %s", (id,))
    conn.commit()

    cursor.close()
    conn.close()
