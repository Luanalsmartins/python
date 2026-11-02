total = prodmd1000 = c = 0

while True:
    print('========== LOJA DA LUANA ==========')
    nomeprod = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))

    total += preco
    c += 1

    if preco > 1000:
        prodmd1000 += 1

    if (c == 1) or (preco < precomb) :
        precomb = preco
        prodmb = nomeprod

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('========== FIM DO PROGRAMA ==========')
print(f'O total da compra foi {total:.2f}')
print(f'Temos {prodmd1000} custando mais de R$1000,00')
print(f'O produto mais barato foi {prodmb} que custa {precomb:.2f}')