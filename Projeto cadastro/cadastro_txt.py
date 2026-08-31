import os

ARQUIVO = "cadastros.txt"

cadastros = []

def carregar_cadastros():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            for linha in f:
                nome, vinculo, cargo, data_nascimento, cpf, email_institucional, ramal = linha.strip().split(",")
                pessoa = {
                    "nome": nome,
                    "vinculo": vinculo,
                    "cargo": cargo,
                    "data_nascimento": data_nascimento,
                    "cpf": cpf,
                    "email_institucional": email_institucional,
                    "ramal": ramal
                }
                cadastros.append(pessoa)

def salvar_cadastros():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for pessoa in cadastros:
            f.write(f"{pessoa['nome']},{pessoa['vinculo']},{pessoa['cargo']},{pessoa['data_nascimento']},{pessoa['cpf']},{pessoa['email_institucional']},{pessoa['ramal']}\n")

def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    vinculo  = input("digite o vínculo da pessoa: ")
    cargo = input("Digite o cargo da pessoa: ")
    data_nascimento = input("Digite a data de nascimento da pessoa (dd/mm/aaaa): ")
    cpf = input("Digite o CPF da pessoa (apenas números): ")
    email_institucional = input("Digite o e-mail institucional da pessoa: ")
    ramal = input("Digite o ramal da pessoa: ")

    pessoa = {
        "nome": nome,
        "vinculo": vinculo,
        "cargo": cargo,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "email_institucional": email_institucional,
        "ramal": ramal
    }
    cadastros.append(pessoa)
    salvar_cadastros()
    print("Cadastro realizado com sucesso!")

def listar_pessoas():
    if not cadastros:
        print("Nenhum cadastro encontrado. \n")
        return
    else:
        print("Lista de pessoas cadastradas:")
        for i, pessoa in enumerate(cadastros, start=1):
            print(f"{i}. Nome: {pessoa['nome']}, Vínculo: {pessoa['vinculo']}, Cargo: {pessoa['cargo']}, Data de Nascimento: {pessoa['data_nascimento']}, CPF: {pessoa['cpf']}, E-mail Institucional: {pessoa['email_institucional']}, Ramal: {pessoa['ramal']}")
        print()

def menu():
    carregar_cadastros()
    while True:
        print("Menu de Cadastro de Pessoas")
        print("1. Cadastrar Pessoa")
        print("2. Listar Pessoas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente!\n")

menu()