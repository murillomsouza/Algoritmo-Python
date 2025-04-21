#Exercicio 16
soma = 1
multi_3 = 0
multi_5 = 0
sequencia = int(input('Digite o ultimo número da sequência: '))
for i in range(1, sequencia+1, 1):
    if i % 3 == 0:
        multi_3 += soma
    elif i % 5 == 0:
        multi_5 += soma
print(f'A quantidade de multiplos de 3 é de {multi_3}')
print(f'A quantidade de multiplos de 5 é de {multi_5}')
