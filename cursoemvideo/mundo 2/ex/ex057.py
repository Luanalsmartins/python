sexo = str(input('Digite [M] para masculino ou [F] para feminino: ')).upper()

while sexo != 'M' and sexo != 'F':
    print('Tente novamente!')
    sexo = str(input('Digite [M] para masculino ou [F] para feminino: ')).upper()
if sexo == 'M':
    print('O sexo é masculino.')
else:
    print('O sexo é feminino.')