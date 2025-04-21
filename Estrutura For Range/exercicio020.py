#Exercicio 20
num = int(input("Digite um número: "))
if num < 2:
    print(f"{num} não é um número primo.")
else:
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")
