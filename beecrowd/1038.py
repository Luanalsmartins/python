codigo, quantidade = input().split()

codigo = int(codigo)
quantidade = int(quantidade)

if codigo == 1:
    codigo = 4.00
elif codigo == 2: 
    codigo = 4.50
elif codigo == 3:
    codigo = 5.00
elif codigo == 4:
    codigo = 2.00
elif codigo == 5:
    codigo = 1.50

valor_total = codigo * quantidade 

print(f'Total: R$ {valor_total:.2f}')