"""Exercicio 3"""
idade = int(input('Digite sua idade:'))
if 0 <= idade < 13:
    print('Você é uma criança.')
elif 13 <= idade < 18:
    print('Você é adolecente.')
elif 18 <= idade < 65:
    print('Você é um adulto.')
else:
    print('Você já é idoso.')