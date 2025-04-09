#Exercicio 13
soma_par = 0
soma_impar = 0
fim = int(input('Digite o fim da sequência: '))
for i in range(fim + 1):
    if i % 2 == 0: soma_par += i
    else: soma_impar += i
print(f'A soma dos pares é {soma_par}.')
print(f'A soma dos ímpares é {soma_impar}.')