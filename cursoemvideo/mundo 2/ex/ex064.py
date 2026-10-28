n = int(input('Digite quantos números quiser, o programa só finaliza quando vocẽ digitar 999: '))
qt = 0
soma = 0

while n != 999:
    qt += 1
    soma += n
    n = int(input('Digite quantos números quiser, o programa só finaliza quando vocẽ digitar 999: '))
print(f'A quantidade de números digitados foi: {qt}\nA soma de todos os números digitados é: {soma}')