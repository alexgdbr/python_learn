# Manejo de Exceções em Pyton #
"""
Try - O bloco try contém o código que pode gerar uma exceção. 
Se ocorrer uma exceção dentro do bloco try, 
o fluxo de execução é transferido para o bloco except correspondente.
"""
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0 # Divisão por zero, que gera uma exceção
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero!")


try:
    numero1 = int(input("Digite o numerador: "))
    numero2 = int(input("Digite o denominador: "))
    resultado = numero1 / numero2
except ZeroDivisionError:
    print("Erro: Não é possível dividir por sero!")
except ValueError:
    print(" Erro: Por favor, digirte um número Válido!")
else:
    print(f"O resultado da divisão é: {resultado}")
finally:
    print("Operação finalizada.")

try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")


try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção

"""
Além das exceções incorporadas no Python, você também pode criar suas próprias exceções personalizadas. Isso é útil quando deseja lidar com situações específicas do seu programa.

Para criar uma exceção personalizada, você deve criar uma classe que herde da classe base Exception ou de uma de suas subclasses.

"""

def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição do erro")

try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")