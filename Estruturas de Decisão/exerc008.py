"""Exercicio 8"""
nota = int(input('Digite a nota do aluno de 1 a 100:'))
if nota > 90:
    print('Nota A')
elif 80 <= nota <= 89:
    print('Nota B')
elif 70 <= nota <= 79:
    print('Nota C')
elif 60 <= nota <= 69:
    print('Nota D')
else:
    print('Nota F')