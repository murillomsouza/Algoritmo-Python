#Exercicio 5
saldo = 1000
saque = 0
while saldo > 0:
    saque = int(input('Digite um valor a ser sacado: '))
    if saque > saldo:
        print('Operação inválida, você não tem saldo suficiente.')
        break
    else:
        saldo -= saque
        print(f'Agora seu saldo é de R${saldo},00.')
