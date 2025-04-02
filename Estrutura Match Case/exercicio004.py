#-----Exercicio 4-----
#-----Seleção de categoria-----
categoria = input('Digite o tipo do produto comprado: \n Eletrônico \n Roupas \n Alimentos \n Movéis \n').lower()
match categoria:
    case 'eletronico':
        preco = float(input('Digite o valor: '))
        print(f'O desconto é de 20%, sendo assim o total fica em R${preco - (preco * 0.2):.2f}.')
    case 'roupas':
        preco = float(input('Digite o valor: '))
        print(f'O desconto é de 15%, sendo assim o total fica em R${preco - (preco * 0.15):.2f}.')
    case 'alimentos':
        preco = float(input('Digite o valor: '))
        print(f'O desconto é de 10%, sendo assim o total fica em R${preco - (preco * 0.1):.2f}.')
    case 'moveis':
        preco = float(input('Digite o valor: '))
        print(f'O desconto é de 5%, sendo assim o total fica em R${preco - (preco * 0.05):.2f}.')
    case _:
        print('Opção inválida')