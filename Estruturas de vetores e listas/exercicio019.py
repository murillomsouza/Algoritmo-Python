# Simule um carrinho de compras: adicione produtos até que o usuário digite 'fim' e, no final, mostre o carrinho.
carrinho = []
while True:
    produto = str(input('Digite o produto a ser comprado: ')).lower()
    if produto != 'fim':
        carrinho.append(produto)
        print(f'Item adicionado ao carrinho!')
    else:
        print(f'Seu carrinho possui os seguintes itens: {carrinho}.')
        break