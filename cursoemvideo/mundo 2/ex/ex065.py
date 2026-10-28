continuar = 'S'
c = soma = maior = menor = 0

while continuar in 'Ss':
    n = int(input('Digite um número: '))
    c += 1
    soma += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
media = soma/c
print(f'Você digitou {c} números e a média foi {media:.2f}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')