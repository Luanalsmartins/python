# Minha resolução: 
'''print('========== BANCO BANCO ==========')
valor = int(input('Qual valor você quer sacar? R$'))
cedcinquenta = cedvinte = ceddez = cedum = 0

while True:
    while valor >= 50:
        cedcinquenta += 1
        valor -= 50
    if cedcinquenta >= 1:
        print(f'Total de {cedcinquenta} cédulas de R$50')
    while valor >= 20:
        cedvinte += 1
        valor -= 20
    if cedvinte >= 1:
        print(f'Total de {cedvinte} cédulas de R$20')
    while valor >= 10:
        ceddez += 1
        valor -= 10
    if ceddez >= 1:
        print(f'Total de {ceddez} cédulas de R$10')
    while valor >= 1:
        cedum += 1
        valor -= 1
    if cedum >= 1:
        print(f'Total de {cedum} cédulas de R$1')
    if valor == 0:
        break
'''
# Resolução do prof Guanabara
print('==================== BANCO CEV ====================')
valor = int(input('Qual valor você quer sacar? R$'))
total = valor 
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced 
        totalced += 1 
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break