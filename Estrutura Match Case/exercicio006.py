import time
#-----Exercicio 6-----
print('Discando...')
time.sleep(2)
print('Chamando...')
time.sleep(5)
decisao = input('========SOBRE QUAL ASSUNTO GOSTARIA DE FALAR?======== \n 1 - Suporte Técnico \n 2 - Financeiro \n 3 - Cancelamento \n 4 - Falar com Atendente \n').lower()
match decisao:
    case '1':
        print('Estamos direcioando você para o suporte técnico.')
    case '2':
        print('Departamento Financeiro como podemos ajudar?')
    case '3':
        print('Estamos te direcionando ao departamento escolhido.')
        time.sleep(120)
        print('Obrigado por entrar em contato com EMPRESA, como gostaria de prosseguir?')
    case '4':
        print('Estamos redirecionando você a um atendente')
        time.sleep(500)
        print('Não temos nenhum atendente disponível no momento, tente novamente mais tarde.')
    case _:
        print('Opção inválida.')
