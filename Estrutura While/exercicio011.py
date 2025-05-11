#Exercicio 11
soma = 0
while True:
    decisao = input('Deseja somar ou sair? Para somar digite "somar" para somar e "sair" para sair.').lower()
    if decisao == 'somar':
        price = float(input(f'Digite o preço do produto: '))
        quant = int(input('Digite a quantidade desse produto: '))
        soma += price * quant
    if decisao == 'sair':
        print(f'A soma da compra é igual a R${soma:.2f}. Volte sempre!')
    else:
        print('Valor inválido tente novamente.')