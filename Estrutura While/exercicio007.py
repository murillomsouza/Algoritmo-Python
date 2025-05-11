#Exercicio 7
dolar = 5.35
euro = 6.90
while True:
    cont = float(input('Digite quantos doláres deseja converter: '))
    if cont <= 0:
        print('Número inválido tente novamente.')
        break
    else:
        cont *= dolar
        print(f'A conversão fica {cont/euro:.2f}')
