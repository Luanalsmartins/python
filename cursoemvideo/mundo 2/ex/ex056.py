media = 0
hmv = 0
nomehmv = ''
mvinte = 0

for c in range (1, 5):
    print(f'-----{c}ª PESSOA-----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    # Média da idade do grupo
    media += idade/4

    # Verifica qual é o homem mais velho
    if sexo in 'Mm' and idade > hmv:
        hmv = idade
        nomehmv = nome

    # Verifica quantas mulheres tem menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        mvinte += 1


print(f'A média de idade do grupo é {media}.')
print(f'O homem mais velho se chama {nomehmv} e tem {hmv} anos.')
print(f'Ao todo, {mvinte} mulheres tem menos de 20 anos')