#-----Exercicio 9-----
produto = input('Qual produto deseja comprar? \n Celular \n Lavaroupa \n Televisão \n Videogame \n').lower()
match produto:
    case 'celular':
        print('Este produto custa R$2.000,00')
    case 'lavaroupa':
        print('Este produto custa R$3.000,00')
    case 'televisao':
        print('Este produto custa R$2.500,00')
    case 'videogame':
        print('Este produto custa R$7.000,00')
    case _:
        print('Produto não encontrado.')