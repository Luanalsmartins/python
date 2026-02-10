"""
Escreva um algoritmo para calcular e escrever o 
valor de S, sendo S dado pela fórmula:
S = 1 + 1/2 + 1/3 + … + 1/100

Entrada
Não há nenhuma entrada neste problema.

Saída
A saída contém um valor correspondente ao 
valor de S.
O valor deve ser impresso com dois dígitos 
após o ponto decimal.
"""
count = [100]
S = 1
i = 2

while i <= 100:
    S = S + 1/i
    i += 1

print(f'{S:.2f}')