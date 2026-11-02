pessoasmais18 = homenscadastrados = mulheresmenos20 = 0

while True:
    print('========== CADASTRE UMA PESSOA ==========')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        pessoasmais18 += 1
    if sexo in 'M':
        homenscadastrados += 1
    if (sexo in 'F') and (idade < 20):
        mulheresmenos20 += 1
    if continuar in 'N':
        break
print(f'Total de pessoas com mais de 18 anos {pessoasmais18}.')
print(f'Ao todo temos {homenscadastrados} homens cadastrados.')
print(f'E temos {mulheresmenos20} mulheres com menos de 20 anos.')
