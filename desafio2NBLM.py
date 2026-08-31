preco = float(input("Digite o valor da compra: \n"))

if preco >= 1500:
    preco_desconto = preco * 0.15
    print(f"O valor do desconto é de: {preco_desconto:.2f}")
    preco_final = preco - preco_desconto

    print(f"O valor da compra é de R$ {preco:.2f} e o valor com desconto é de R$ {preco_final:.2f}.")
else:
    print(f"O valor da compra é de R$ {preco:.2f} e não há desconto.")




