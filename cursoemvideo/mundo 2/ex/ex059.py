v1 = int(input('Digite o valor 1: '))
v2 = int(input('Digite o valor 2: '))

print('---------- MENU ----------')
print('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA')

opcao = int(input('Escolha a opção desejada: '))

while opcao != 5:
    if opcao == 1:
        print(f'{v1} + {v2} = {v1 + v2}')
    elif opcao == 2: 
        print(f'{v1} x {v2} = {v1 * v2}')
    elif opcao == 3:
        if v1 > v2: 
            print(f'Entre {v1} e {v2} o maior é {v1}')
        elif v2 > v1: 
            print(f'Entre {v1} e {v2} o maior é {v2}')
        else: 
            print(f'Os números {v1} e {v2} são iguais!')
    elif opcao == 4:
        v1 = int(input('Digite o valor 1: '))
        v2 = int(input('Digite o valor 2: '))   

    opcao = int(input('Qual será a sua próxima escolha? '))

print('Programa finalizado!')