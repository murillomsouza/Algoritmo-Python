"""Exercicio 14"""
consumo = float(input('Digite a quantidades de kV/h foram consumidos:'))
valor = float(input('Digite o valor do kW/h (em reais): '))
conta = consumo*valor
print(f'Sua conta será no valor de R${conta}.')