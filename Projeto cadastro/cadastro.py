cadastros = []

def cadastro_pessoa():
    nome = input("Digite o nome da pessoa: ")
    vinculo = input("Digite o vínculo da pessoa: ")
    cargo = input("Ditite o cargo da pessoa: ")
    data_nascimento = input("Digite a data de nascimento da pessoa (dd/mm/aaaa): ")
    cpf = input("igite o CPF da pessoa (apenas números): ")
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
    while True:
        print("Menu de Cadastro de Pessoas")
        print("1. Cadastrar Pessoa")
        print("2. Listar Pessoas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente!\n")

menu()