#Exercicio 14
list = []
for i in range(5):
    num = float(input(f'Digite o {i + 1}° número: '))
    list.append(num)
print(f'O maior número é {max(list)}.')
print(f'O menor número é {min(list)}.')
