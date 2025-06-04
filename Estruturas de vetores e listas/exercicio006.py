# Verifique se um nome digitado pelo usuário está em uma lista de nomes.
nomes = ['murillo', 'caua', 'matheus', 'raul']
busca = str(input('Digite o nome para verificar se está na lista: ')).lower()
if busca in nomes:
    print('Este nome está na lista!')
else:
    print('Este nome não esta na lista.')