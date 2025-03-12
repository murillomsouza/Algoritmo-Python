"""Exercicio 15"""
reais = float(input('Digite o valor a ser convertido (em reais): '))
#considerando dolar a R$5,00
conversao = reais/5.00
print(f'Você teria U${conversao:.2f}, após a conversão')