"""Exericio 12"""
idade = int(input('Digite a idade do jogador:'))
if idade <= 17:
    categoria = 'Juvenil'
elif 18 <= idade <= 35:
    categoria = 'Adulto'
else:
    categoria = 'Veterano'
print(f'O jogador tem {idade} anos e está na categoria {categoria}.')