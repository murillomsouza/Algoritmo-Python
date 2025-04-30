#Exercicio 2
list = []
desicao = input('Digite o que deseja fazer: \n 0 - Sair \n 1 - Verificar maior e menor \n')
if desicao == '0':
    print('Obrigado por usar esse sistema!')
elif desicao == '1':
    num = float(input('Digite o número a ser analisado: '))
    while num != 0:
        num = float(input('Digite o número a ser analisado: '))
        list.append(num)
    print(f'O maior dos números digitados foi {max(list)}')
    print(f'O menor dos números digitados foi {min(list)}')
