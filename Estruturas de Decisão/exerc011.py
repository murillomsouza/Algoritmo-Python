"""Exercicio 11"""
#----Considerando que o usuário tem R$1000.00 disponíveis
saldo_inicial= 1000.00
print('Para inciar por favor insira o cartão.')
#-----Entrada de decisão-----
decisao = input('Para consultar saldo digite 1 \n '
'Para sacar digite 2 \n '
'Para realizar depósito digite 3\n')
#-----Verificar Saldo Inicial-----
if decisao == '1':
    print('Seu saldo é de R$1000.00')
#-----Saque-----
elif decisao == '2':
    saque = float(input('digite o valor desejado:'))
    if saque > saldo_inicial: #Saque maior que saldo
        print('Saldo insufiente para operação.')
    else: #Saque realizado com Sucesso
        saldo_apos_saque = saldo_inicial - saque
        print(f'Saque realizado! Seu saldo actualization é de R${saldo_apos_saque:.2f}')
#-----Depósito-----
elif decisao == '3':
    deposito = float(input('Digite o valor a ser depositado: '))
    saldo_apos_deposito = saldo_inicial + deposito
    if deposito <= 0: #Deposito inválido (Menor ou igual a 0)
        print('Valor inválido, tente novamente.')
    else:
        print(f'Deposito realizado com sucesso. O saldo atual de sua conta é de R${saldo_apos_deposito:.2f}')
else:   #Erro, nenhuma opção selecionada ou não compreendida
    print('Erro, nemnhuma opção selecionada.')