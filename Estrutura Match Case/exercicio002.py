#-----Exercicio 2-----
#-----Entrada decisão-----
decisao = input('O que deseja calcular? \n Retângulo \n Quadrado \n Triângulo \n').lower()
match decisao:
    case 'retangulo':
        altura = float(input('Digite a altura: '))
        comprimento = float(input('Digite o comprimento: '))
        print(f'A area desse retâgulo é de {altura*comprimento:.2f}')
    case 'quadrado':
        altura = float(input('Digite a altura: '))
        comprimento = float(input('Digite o comprimento: '))
        print(f'A area desse quadrado é de {altura * comprimento:.2f}')
    case 'triangulo':
        altura = float(input('Digite a altura: '))
        comprimento = float(input('Digite o comprimento: '))
        print(f'A area desse triângulo é de {(altura * comprimento)/2:.2f}')
    case _:
        print('Opção inválida.')