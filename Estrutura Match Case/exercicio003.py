#-----Exercicio 3-----
#-----Usuário-----
login = input('Seja bem-vindo! \n Deseja logar com qual usuário? \n Admin \n Professor \n Aluno \n').lower()
#-----decisão de acesso-----
match login:
    case 'admin':
        print('Você tem acesso total ao sitema!')
    case 'professor':
        print('Você tem acesso ao ambiente acadêmico!')
    case 'aluno':
        print('Você tem acesso ao ambiente de estudos!')
    case _:
        print('Opção inválida.')