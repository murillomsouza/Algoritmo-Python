"""Exercicio 10"""
preco = float(input('Digite o valor do produto em reais:'))
desconto = preco * 0.10
precofinal = preco - desconto
if desconto >= 100.00:
    print(f'O valor descontado é de R${desconto}, e o valor final do produto é R${precofinal}')
else:
    print(f'O valor do produto com desconto é de R${precofinal}')