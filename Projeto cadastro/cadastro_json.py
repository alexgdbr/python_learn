import os
import json
# Importamos todas as validações de um único módulo!
from validador import validar_cpf, validar_emailinst, validar_data

ARQUIVO = "cadastros.json"
cadastros = []

def carregar_cadastros():
    global cadastros
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            cadastros = json.load(f)

def salvar_cadastros():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(cadastros, f, ensure_ascii=False, indent=4)

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

    pessoa = {
        "nome": nome.strip(),
        "vinculo": vinculo.strip(),
        "cargo": cargo.strip(),
        "data_nascimento": data_nascimento.strip(),
        "cpf": cpf.strip(),
        "email_institucional": email_institucional.strip(),
        "ramal": ramal.strip(),
    }
    cadastros.append(pessoa)
    salvar_cadastros()
    print("\nPessoa cadastrada com sucesso!\n")


def listar_cadastros():
    if not cadastros:
        print("\nNenhuma pessoa cadastrada.\n")
    else:
        print("\n--- Lista de Pessoas Cadastradas ---")
        for i, pessoa in enumerate(cadastros, start=1):
            print(f"{i}. Nome: {pessoa['nome']} | CPF: {pessoa['cpf']} | E-mail: {pessoa['email_institucional']}")
        print("------------------------------------\n")

def buscar_por_cpf():
    if not cadastros:
        print("\nNenhum cadastro na base de dados para pesquisar.\n")
        return

    cpf_busca = input("Digite o CPF para buscar (apenas números): ").strip()
    
    for pessoa in cadastros:
        if pessoa['cpf'] == cpf_busca:
            print("\n--- Cadastro Encontrado ---")
            print(f"Nome: {pessoa['nome']}")
            print(f"CPF: {pessoa['cpf']}")
            print(f"E-mail: {pessoa['email_institucional']}")
            print(f"Data de Nascimento: {pessoa['data_nascimento']}")
            print(f"Vínculo: {pessoa['vinculo']}")
            print(f"Cargo: {pessoa['cargo']}")
            print(f"Ramal: {pessoa['ramal']}")
            print("---------------------------\n")
            return

    print("\nNenhum cadastro encontrado com esse CPF.\n")

def buscar_por_nome():
    if not cadastros:
        print("\nNenhum cadastro na base de dados para pesquisar.\n")
        return

    nome_busca = input("Digite o nome da pessoa que deseja buscar: ").strip().lower()
    encontrado = False

    for pessoa in cadastros:
        # .lower() converte ambos para minúsculo e 'in' permite buscar partes do nome
        if nome_busca in pessoa["nome"].lower():
            print("\n--- Cadastro Encontrado ---\n")
            print(f"Nome: {pessoa['nome']}")
            print(f"CPF: {pessoa['cpf']}")
            print(f"E-mail: {pessoa['email_institucional']}")
            print(f"Data de Nascimento: {pessoa['data_nascimento']}")
            print(f"Vínculo: {pessoa['vinculo']}")
            print(f"Cargo: {pessoa['cargo']}")
            print(f"Ramal: {pessoa['ramal']}")
            print("---------------------------\n")
            encontrado = True

            # Como pode haver mais de uma pessoa com o mesmo nome/sobrenome,
            # verificamos a flag após percorrer toda a lista
    if not encontrado:
        print("\nNenhum cadastro encontrado com esse nome.\n")
    else:
        print()



def editar_cadastro():
    if not cadastros:
        print("\nNenhum cadastro para editar.\n")
        return
    
    listar_cadastros()
    
    while True:
        try:
            indice = int(input("Digite o número da pessoa que deseja editar: "))
            if 1 <= indice <= len(cadastros):
                pessoa = cadastros[indice - 1]
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

                pessoa.update({
                    "nome": novo_nome.strip(),
                    "vinculo": novo_vinculo.strip(),
                    "cargo": novo_cargo.strip(),
                    "data_nascimento": nova_data.strip(),
                    "cpf": novo_cpf.strip(),
                    "email_institucional": novo_email.strip(),
                    "ramal": novo_ramal.strip()
                })

                salvar_cadastros()
                print("\nCadastro atualizado com sucesso!\n")
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

def excluir_cadastro():
    if not cadastros:
        print("\nNenhum cadastro para excluir.\n")
        return
    
    listar_cadastros()
    
    while True:
        try:
            indice = int(input("Digite o número da pessoa que deseja excluir: "))
            if 1 <= indice <= len(cadastros):
                pessoa_removida = cadastros.pop(indice - 1)
                salvar_cadastros()
                print(f"\nCadastro de {pessoa_removida['nome']} excluído com sucesso!\n")
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

def menu():
    carregar_cadastros()
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