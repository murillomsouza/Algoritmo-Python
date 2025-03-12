"""Exercicio 6"""
numero = float(input('Digite um numero:'))
par = numero % 2
impar = numero / 2
if par == 0:
    print('Esse numero é par')
else:
    print('Esse numero é impar')