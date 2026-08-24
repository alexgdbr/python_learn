# projeto sequêncial de um caixa
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o valor do produto: R$ "))
quantidade = int(input("Digite a quantidade de produtos: "))

subtotal = preco * quantidade
if subtotal >= 100:
    desconto = subtotal * 0,10
else:
    desconto = 0

total = subtotal - desconto

print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Subtotal: R$ {subtotal: .2f}")
print(f"Desconto: R$ {desconto: .2f}")
print(f"Total: R$ {total: .2f}")
