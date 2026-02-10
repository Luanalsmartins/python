# Receba F para feminino e M para masculino e exiba o sexo da pessoa.

sexo = input('Digite seu sexo, sendo F para feminino e M para masculino: ')


if sexo == 'F' or sexo == 'f': 
    print('Você é do sexo feminino')
elif sexo == 'M'or sexo == 'm':
    print('Você é do sexo masculino')
else:
    print('Valor inválido!')