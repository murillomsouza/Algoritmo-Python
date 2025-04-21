#Exercicio 18
sequencia = int(input('Digite o número final da sequência: '))
for i in range(1, sequencia+1, 1):
    if i % 3 == 0:
        print(f'{i} é multiplo de 3')
        if i % 5 == 0:
            print(f'{i} é multiplo de 5')
    elif i % 5 == 0:
        print(f'{i} é multiplo de 5')
        