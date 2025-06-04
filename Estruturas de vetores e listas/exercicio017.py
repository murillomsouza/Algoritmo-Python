# Faça uma função que recebe uma lista de números e retorna uma nova lista com o fatorial de cada número.
import math
lista_num = [3, 2, 4, 5]
factorial = 1
for i in lista_num[::]:
   factorial = math.factorial(i)
   print(factorial)