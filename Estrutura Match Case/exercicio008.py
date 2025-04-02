#------Exercicio 008-----
destino = input('Escolha seu destino: \n São Paulo \n Rio de Janeiro \n Curitiba \n Salvador \n').lower()
match destino:
    case 'sao paulo':
        print('O valor da passagem é de R$150,00')
    case 'rio de janeiro':
        print('O valor da passagem é de R$500,00')
    case 'curitiba':
        print('O valor da passagem é de R$730,00')
    case 'sao paulo':
        print('O valor da passagem é de R$1400,00')
    case _:
        print('Destino inválido.')
