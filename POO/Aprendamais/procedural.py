# Abordagem Procedural (procedural.py)

# Variáveis separadas para cada funcionário
nome_func1 = "Maria Silva"
salario_func1 = 5000
cargo_func1 = "Desenvolvedora"

nome_func2 = "João Santos"
salario_func2 = 4500
cargo_func2 = "Analista"

# Funções separadas que manipulam os dados
def calcular_bonus(salario):
    return salario * 0.10

def exibir_dados(nome, salario, cargo):
    print(f"Nome: {nome}")
    print(f"Cargo: {cargo}")
    print(f"Salário: R$ {salario}")

# Uso
bonus1 = calcular_bonus(salario_func1)
exibir_dados(nome_func1, salario_func1, cargo_func1)

bonus2 = calcular_bonus(salario_func2)
exibir_dados(nome_func2, salario_func2, cargo_func2)