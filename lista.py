#Exercício de listas

# inserindo
# Para adicionar um item ao final da lista, use o método:append()
frutas = ["maçã", "banana", "laranja", "uva"]
frutas.append("jaca")
print(frutas)

# Para inserir um item de lista em um índice especificado, use o método.insert()
# adicionar um iten na lista na posição desejada
frutas = ["maçã", "banana", "laranja", "uva", "jaca"]
frutas.insert(0, "abacaxi")
print(frutas)

#Estender a Lista
#Para adicionar elementos de outra lista à lista atual, use o método.extend()
frutas = ["maçã", "pêra", "laranja", "uva"]
frutas_tropicais = ["abacaxi", "manga", "coco"]
frutas.extend(frutas_tropicais)
print(frutas)

# Adicionar qualquer iterável
# O método não precisa adicionar listas, você pode adicionar qualquer objeto iterável (tuplas, conjuntos, dicionários etc.).extend()
lista = ["maçã", "banana", "laranja"]
tupla = ("coco", "jaca", "mangaba")
lista.extend(tupla)
print(lista)

# Remover Item Especificado
# O método remove o item especificado.remove()
lista = ["maçã", "banana", "laranja", "uva"]
lista.remove("laranja")
print(lista)

#Se houver mais de um item com o valor especificado, o método remove o primeiro Ocorrência:remove()
lista = ["maçã", "banana", "laranja", "uva", "laranja"]
lista.remove("laranja")
print(lista)

# Remover Índice Especificado
# O método remove o especificado Índice.pop()
lista = ["maçã", "banana", "laranja", "uva"]
lista.pop(1)
print(lista)

# Se você não especificar o índice, o método remove o último item.
lista = ["maçã", "banana", "laranja", "uva"]
lista.pop()
print(lista)

# A palavra-chave também remove o especificado Índice:del
lista = ["maçã", "banana", "laranja", "uva"]
del lista[0]
print(lista)

# Limpar a Lista
# O método esvazia a lista.clear()
# A lista ainda permanece, mas não tem conteúdo.
lista = ["maçã", "banana", "laranja", "uva"]
lista.clear()
print(lista)