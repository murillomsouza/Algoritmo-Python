# Crie uma lista com 5 notas de alunos, calcule a média e diga quais alunos ficaram acima da média.
notas = [5, 7, 8, 10, 4]
media = sum(notas) / 5
print(f'A media das notas foram: {media}')
for i in notas:
    if i >= 5: print(f'O aluno que tirou {i} passou')
    else: print(f'O aluno que tirou {i} reprovou')