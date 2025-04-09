#Exercicio 12
tabuada = int(input('Digite a tabuada qu deseja visualizar: '))
if tabuada % 3 == 0: print('Multiplo de três')
else:
    for i in range(11):
        print(f'{tabuada} x {i} = {tabuada * i}')

