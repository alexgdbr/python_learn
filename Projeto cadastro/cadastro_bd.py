# Projeto cadastro - está atualizado para um banco de dados SQlite

import sqlite3
from validador import validar_cpf, validar_emailinst, validar_data

BANCO = "banco_cadastros.db"


def conectar():
    """Cria e retorna uma conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(BANCO)
    # Permite acessar os resultados como dicionários (ex: pessoa['nome'])
    conn.row_factory = sqlite3.Row
    return conn


def inicializar_banco():
    """Cria a tabela se ela ainda não existir."""
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT UNIQUE NOT NULL,
                email_institucional TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                vinculo TEXT,
                cargo TEXT,
                ramal TEXT
            )
        """)
        conn.commit()


def cadastrar_pessoa():
    while True:
        nome = input("Digite o nome da pessoa (mínimo de 3 letras): ")
        if len(nome.strip()) >= 3:
            break
        print("Nome inválido. Deve ter pelo menos 3 letras.")

    while True:
        cpf = input("Digite o CPF da pessoa (apenas números): ")
        if validar_cpf(cpf):
            break
        print("CPF inválido. Digite um CPF válido.")

    while True:
        email_institucional = input("Digite o e-mail institucional da pessoa: ")
        if validar_emailinst(email_institucional):
            break
        print("E-mail institucional inválido. Deve terminar com @saude.gov.br")

    while True:
        data_nascimento = input("Digite a data de nascimento da pessoa (dd/mm/aaaa): ")
        if validar_data(data_nascimento):
            break
        print("Data inválida! Use o formato dd/mm/aaaa.")

    vinculo = input("Digite o vínculo da pessoa: ")
    cargo = input("Digite o cargo da pessoa: ")
    ramal = input("Digite o ramal da pessoa: ")

    try:
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO pessoas (nome, cpf, email_institucional, data_nascimento, vinculo, cargo, ramal)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (nome.strip(), cpf.strip(), email_institucional.strip(), data_nascimento.strip(), vinculo.strip(),
                  cargo.strip(), ramal.strip()))
            conn.commit()
            print("\nPessoa cadastrada com sucesso!\n")
    except sqlite3.IntegrityError:
        print("\nErro: Já existe uma pessoa cadastrada com este CPF!\n")


def listar_cadastros():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pessoas")
        pessoas = cursor.fetchall()

    if not pessoas:
        print("\nNenhuma pessoa cadastrada.\n")
        return []

    print("\n--- Lista de Pessoas Cadastradas ---")
    for pessoa in pessoas:
        print(
            f"ID: {pessoa['id']} | Nome: {pessoa['nome']} | CPF: {pessoa['cpf']} | E-mail: {pessoa['email_institucional']}")
    print("------------------------------------\n")
    return pessoas


def buscar_por_cpf():
    cpf_busca = input("Digite o CPF para buscar (apenas números): ").strip()

    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pessoas WHERE cpf = ?", (cpf_busca,))
        pessoa = cursor.fetchone()

    if pessoa:
        print("\n--- Cadastro Encontrado ---")
        print(f"ID: {pessoa['id']}")
        print(f"Nome: {pessoa['nome']}")
        print(f"CPF: {pessoa['cpf']}")
        print(f"E-mail: {pessoa['email_institucional']}")
        print(f"Data de Nascimento: {pessoa['data_nascimento']}")
        print(f"Vínculo: {pessoa['vinculo']}")
        print(f"Cargo: {pessoa['cargo']}")
        print(f"Ramal: {pessoa['ramal']}")
        print("---------------------------\n")
    else:
        print("\nNenhum cadastro encontrado com esse CPF.\n")


def buscar_por_nome():
    nome_busca = input("Digite o nome da pessoa que deseja buscar: ").strip()

    with conectar() as conn:
        cursor = conn.cursor()
        # % permite buscar por trechos do nome (case-insensitive por padrão no SQLite para caracteres ASCII)
        cursor.execute("SELECT * FROM pessoas WHERE nome LIKE ?", (f"%{nome_busca}%",))
        pessoas = cursor.fetchall()

    if pessoas:
        print("\n--- Cadastros Encontrados ---")
        for pessoa in pessoas:
            print(
                f"ID: {pessoa['id']} | Nome: {pessoa['nome']} | CPF: {pessoa['cpf']} | E-mail: {pessoa['email_institucional']}")
        print("-----------------------------\n")
    else:
        print("\nNenhum cadastro encontrado com esse nome.\n")


def editar_cadastro():
    pessoas = listar_cadastros()
    if not pessoas:
        return

    try:
        id_pessoa = int(input("Digite o ID da pessoa que deseja editar: "))

        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pessoas WHERE id = ?", (id_pessoa,))
            pessoa = cursor.fetchone()

            if not pessoa:
                print("ID não encontrado.")
                return

            print("\nEditando cadastro. Pressione [ENTER] sem digitar nada para manter o valor atual.")

            # Nome
            while True:
                novo_nome = input(f"Nome ({pessoa['nome']}): ") or pessoa['nome']
                if len(novo_nome.strip()) >= 3:
                    break
                print("Nome inválido. Deve ter pelo menos 3 letras.")

            # CPF
            while True:
                novo_cpf = input(f"CPF ({pessoa['cpf']}): ") or pessoa['cpf']
                if validar_cpf(novo_cpf):
                    break
                print("CPF inválido. Digite novamente.")

            # E-mail
            while True:
                novo_email = input(f"E-mail ({pessoa['email_institucional']}): ") or pessoa['email_institucional']
                if validar_emailinst(novo_email):
                    break
                print("E-mail inválido! Deve terminar com @saude.gov.br")

            # Data
            while True:
                nova_data = input(f"Data de Nascimento ({pessoa['data_nascimento']}): ") or pessoa['data_nascimento']
                if validar_data(nova_data):
                    break
                print("Data inválida! Use o formato dd/mm/aaaa.")

            novo_vinculo = input(f"Vínculo ({pessoa['vinculo']}): ") or pessoa['vinculo']
            novo_cargo = input(f"Cargo ({pessoa['cargo']}): ") or pessoa['cargo']
            novo_ramal = input(f"Ramal ({pessoa['ramal']}): ") or pessoa['ramal']

            cursor.execute("""
                UPDATE pessoas 
                SET nome = ?, cpf = ?, email_institucional = ?, data_nascimento = ?, vinculo = ?, cargo = ?, ramal = ?
                WHERE id = ?
            """, (novo_nome.strip(), novo_cpf.strip(), novo_email.strip(), nova_data.strip(), novo_vinculo.strip(),
                  novo_cargo.strip(), novo_ramal.strip(), id_pessoa))

            conn.commit()
            print("\nCadastro atualizado com sucesso!\n")

    except ValueError:
        print("Entrada inválida. Digite apenas números para o ID.")


def excluir_cadastro():
    pessoas = listar_cadastros()
    if not pessoas:
        return

    try:
        id_pessoa = int(input("Digite o ID da pessoa que deseja excluir: "))

        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM pessoas WHERE id = ?", (id_pessoa,))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"\nCadastro de ID {id_pessoa} excluído com sucesso!\n")
            else:
                print("\nID não encontrado.\n")

    except ValueError:
        print("Entrada inválida. Digite apenas números para o ID.")


def menu():
    inicializar_banco()
    while True:
        print("=== SISTEMA DE CADASTRO INSTITUCIONAL ===")
        print("****************************")
        print("*  1. Cadastrar pessoa     *")
        print("****************************")
        print("*  2. Listar cadastros     *")
        print("****************************")
        print("*  3. Buscar pessoa por CPF*")
        print("****************************")
        print("*  4. Buscar nome          *")
        print("****************************")
        print("*  5. Editar cadastro      *")
        print("****************************")
        print("*  6. Excluir cadastro     *")
        print("****************************")
        print("*  7. Sair                 *")
        print("****************************")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_cadastros()
        elif opcao == "3":
            buscar_por_cpf()
        elif opcao == "4":
            buscar_por_nome()
        elif opcao == "5":
            editar_cadastro()
        elif opcao == "6":
            excluir_cadastro()
        elif opcao == "7":
            print("\nEncerrando o programa... Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu()