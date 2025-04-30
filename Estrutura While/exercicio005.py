#Exercicio 5
dep = 0
saldo = 0
decisao = {}
while decisao != 4:
    decisao = int(input('=====BANCO===== \n Qual operação deseja realizar? \n Digite um número para selecionar a opção. \n 1 - Visualizar saldo \n 2 - Depositar \n 3 - Sacar \n 4 - Sair \n'))
    if decisao == 1:
        print(f'Seu saldo é de R${saldo}')
    elif decisao == 2:
        dep = float(input('Digite o valor a ser depositado: '))
        print('Depositado com sucesso!')
    saldo += dep