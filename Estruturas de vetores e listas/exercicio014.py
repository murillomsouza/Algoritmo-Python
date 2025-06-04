# Crie uma lista com 5 strings e conte quantas começam com a letra 'A'.
args = ['Ana', 'Banana', 'Anatomia', 'Antes', 'Python']
cont = 0
for i in args:
    if i.lower().startswith('a'): cont += 1
print(f'{cont} começam com "A" nessa lista')