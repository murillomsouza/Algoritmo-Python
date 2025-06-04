# Desenvolva um menu de opções para gerenciar uma lista de tarefas: adicionar, remover, exibir e sair.
tarefas = []
while True:
    decisao = input('==========SELECIONE A OPÇÃO========== \n'
                        '1 - Adicionar \n'
                        '2 - Remover \n'
                        '3 - Exibir \n'
                        '4 - Sair \n')
    if decisao == '1':
        add = str(input('Digite a tarefa que deseja adicionar: '))
        tarefas.append(add)
    elif decisao == '2':
        delete = str(input(f'Digite  item que deseja deletar {tarefas}: '))
        tarefas.remove(delete)
        print('Item deletado!')
    elif decisao == '3':
        print(f'A lista atualizada de tarefas {tarefas}.')
    elif decisao == '4':
        print('Obrigado por usar!')
        break
    else:
        print('Valor inválido tente novamente')