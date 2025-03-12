"""Exercicio 7"""
user = input('Nome de usuário: ')
password = input('Digite sua senha: ')
type(user)
type(password)
if user.islower() and user.isalnum() and password.isalnum():
    print(f'Sejá bem-vindo {user}.')
else:
    print('Usuário ou senha incorreto')