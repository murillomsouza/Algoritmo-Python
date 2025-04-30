#Exercicio 20
cont = 0
num = int(input('Digite o número a ser verificado se é primo: '))
for i in range(1, num+1, 1):
    if num % i == 0:
        cont += 1
if cont <= 2:
    print('É primo!')
else:
    print('Não é primo!')
