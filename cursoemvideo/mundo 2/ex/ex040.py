nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')

if media < 5:
    print('O aluno está REPROVADO!')
elif media >= 5 and media <= 7:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO!')