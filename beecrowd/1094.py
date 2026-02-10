N = int(input()) # quantidade de casos de teste 

C = 0
R = 0
S = 0

for i in range(N):
    quantia, tipo = input().split()
    quantia = int(quantia) # quantidade de cobaias
    tipo = (tipo) # tipo de cobaia
    if tipo == 'C':
        C += quantia
    elif tipo == 'R':
        R += quantia
    elif tipo == 'S':
        S += quantia

total = C + R + S
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {C}')
print(f'Total de ratos: {R}')
print(f'Total de sapos: {S}')
print(f'Percentual de coelhos: {C*100/total:.2f} %')
print(f'Percentual de ratos: {R*100/total:.2f} %')
print(f'Percentual de sapos: {S*100/total:.2f} %')