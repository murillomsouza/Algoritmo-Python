"""Exercicio 10"""
number1 = float(input('Digite o primeiro número: '))
number2 = float(input('Digite o segundo número: '))
if number1 % number2 == 0:
    print('São multiplos')
elif number2 % number1 == 0:
    print('São multiplos')
else:
    print('Não são multiplos')