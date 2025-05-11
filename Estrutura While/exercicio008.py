#Exercicio 8
estoque = 0
while True:
    decisao = input('O que deseja fazer? Escolha uma das opções abaixo: \n 1 - Visualizar estoque \n 2 - Adicionar \n 3 - Excluir')
    match decisao:
        case "1":
            print(f'O estoque atual é de {estoque}')
        case '2':
            add = int(input('Quantas unidades deseja adicionar? '))
            if add >= 0:
                estoque += add
            else:
                print('Inválido, para adicionar o número tem que ser maior que zero (0).')
                break
        case '3':
            delete = int(input('Quantas unidades deseja excluir? '))
            if delete > estoque or delete < 0:
                print('O estoque não pode ficar negativo, delete a quantidade válida.')
                break
            else: 
                estoque -= delete