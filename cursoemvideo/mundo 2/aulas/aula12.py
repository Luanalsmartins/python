nome = str(input('Qual é seu nome? '))
if nome == 'Luana':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Ana':
    print('Seu nome é popular no Brasil.')
elif nome in 'Aurora Diana Helena':
    print('Belo nome feminino!')
else: 
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}!')