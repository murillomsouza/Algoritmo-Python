#------Exercicio 10-----
payment = input('==========Selecione a forma de pagamento========== \n 1 - Dinheiro \n 2 - Débito \n 3 - Crédito \n 4 - Pix').lower()
match payment:
    case'1':
        print('Você vai recebe um desconto de 10%!')
    case '2':
        print('Pagamento do valor integral.')
    case '3':
        print('Você vai recebe um acréscimo de 5%.')
    case '4':
        print('Você vai recebe um desconto de 15%!')
    case _:
        print('Opção inválida.')
        