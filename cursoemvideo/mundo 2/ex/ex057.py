sexo = str(input('Digite [M] para masculino ou [F] para feminino: ')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    print('Tente novamente!')
    sexo = str(input('Digite [M] para masculino ou [F] para feminino: ')).strip().upper()[0]
if sexo == 'M':
    print('O sexo é masculino.')
else:
    print('O sexo é feminino.')
print('Sexo registrado com sucesso.')