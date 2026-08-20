# Criar uma Classe
# Para criar uma classe, use a palavra-chave :class seguida do nome da classe e dois pontos.
# O nome da classe deve começar com uma letra maiúscula, e se for composto, cada palavra deve começar com uma letra maiúscula (CamelCase).

# class NomeDaClasse:
#     # Atributos e métodos da classe vão aqui
#     pass

class Myclass:
    x = 10

#Criar Objeto
#Agora podemos usar a classe chamada MyClass para criar objetos:

p1 = Myclass()
print(p1.x)

# Excluir Objetos
# Você pode excluir objetos usando a palavra-chave:del

del p1


# Múltiplos Objetos
# Você pode criar múltiplos objetos a partir da mesma classe:

p1 = Myclass()
p2 = Myclass()
p3 = Myclass()

print(p1.x)
print(p2.x)
print(p3.x)

# A Declaração de Passe
# class definições não podem ser vazias, mas se Por algum motivo, você tem uma definição sem conteúdo, coloque na declaração para evitar um erro.classpass

class Person:
    pass