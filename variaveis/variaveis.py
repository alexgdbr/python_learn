# indentação de código em Python é feita com espaços em branco, geralmente 4 espaços por nível de indentação. 
# A indentação é obrigatória e define blocos de código, como funções, loops e condicionais. Por exemplo:
if True:
    print("Este bloco de código está indentado corretamente.")  


# Variáveis em Python são usadas para armazenar valores. 
# Você pode criar uma variável simplesmente atribuindo um valor a ela. Por exemplo:
# Criando uma variável chamada 'mensagem' e atribuindo um valor a ela  .
mensagem = "Olá, mundo!"
# Agora podemos imprimir o valor da variável 'mensagem' usando a função print().
print(mensagem)  # Isso imprimirá: Olá, mundo!

#Regras para variáveis em Python:
# O nome de uma variável deve começar com uma letra ou o caractere sublinhado
# Um nome de variável não pode começar com um número
# O nome de uma variável só pode conter caracteres alfanuméricos e sublinhados (A-z, 0-9 e _ )
# Nomes de variáveis são sensíveis a maiúsculas minúsculas (idade, idade e IDADE são três variáveis diferentes)
# O nome de uma variável não pode ser nenhuma das palavras-chave em Python.

# Nomes de variáveis com múltiplas palavras
# Nomes de variáveis com mais de uma palavra podem ser difíceis de ler.

# Existem várias técnicas que você pode usar para torná-las mais legíveis:

# Caso do camelo
# Cada palavra, exceto a primeira, começa com uma letra maiúscula:

myVariableName = "John"
# Caso Pascal
# Cada palavra começa com uma letra maiúscula:

MyVariableName = "John"
# Caso da Cobra
# Cada palavra é separada por um caractere sublinhado:

my_variable_name = "John"

# Muitos valores para múltiplas variáveis
# Python permite que você atribua valores a múltiplas variáveis em uma única linha:

x, y, z = 'laranja', 'maçã', 'pêra'

print(x)
print(y)
print(z)


frutas = ['laranja', 'maçã', 'pêra']
x, y, z = frutas
print(x)
print(y)
print(z)

# Variáveis de saída
# Você pode usar a função print() para exibir valores de variáveis na saída padrão (geralmente o console). Por exemplo:
idade = 25
print('Sua idade é: ', idade)

x = 'Python'
y = "é"
z = 'incrível'
print(x, y, z)

# também pode usar o operador para produzir Múltiplas variáveis:+
#Exemplo

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Para números, o caractere funciona como um operador matemático:+
#Exemplo
x = 5
y = 10
print(x + y)

#A melhor maneira de gerar múltiplas variáveis na função é separá-las com vírgulas, que até suportam diferentes tipos de dados:print()
#Exemplo
x = 5
y = "John"
print(x, y)