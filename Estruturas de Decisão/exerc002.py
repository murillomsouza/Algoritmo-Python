"""Exercicio 2"""
idade = int(input('Digite sua idade:'))
if idade < 18:
    print('Você é menor de idade.')
elif 18 <= idade < 65:
    print('Você é maior de idade.')
else:
    print('Você já idoso')