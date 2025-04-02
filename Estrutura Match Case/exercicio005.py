#-----Exercicio 5-----
cor = input('Qual cor deseja traduzir? \n Vermelho \n Azul \n Verde \n Amarelo \n').lower()
match cor:
    case 'vermelho':
        print('A tradução de vermelho para o inglês é Red')
    case 'azul':
        print('A tradução de vermelho para o inglês é Blue')
    case 'verde':
        print('A tradução de vermelho para o inglês é Green')
    case 'amarelo':
        print('A tradução de vermelho para o inglês é Yellow')
    case _:
        print('Opção inválida.')
