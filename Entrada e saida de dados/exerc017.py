"""Exercicio 17"""
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
kmr = float(input('Digite quantos Km esse carro andou durante esse período: '))
conta = (dias * 90) + (kmr * 0.20)
print(f'O preço total desse aluguel ficou em R${conta}')