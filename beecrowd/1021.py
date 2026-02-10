# lê a entrada do usuário, sendo dividida em duas partes, a parte inteira (reais) e a parte decimal (centavos) usando split
#map(int, ...) converte essas duas partes em inteiros
reais, centavos = map(int, input().split('.'))

# Converte o valor total para centavos
total_centavos = reais * 100 + centavos

# Lista de valores das notas e moedas em centavos
notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

# Itera (percorre) sobre cada valor de nota
print("NOTAS:")
for nota in notas:
    count = total_centavos // nota # calcula quantas notas daquele valor são necessárias
    total_centavos %= nota # atualiza total_centavos com o valor restante após subtrair o valor das notas contadas
    print(f"{count} nota(s) de R$ {nota / 100:.2f}")

# Itera (percorre) sobre cada valor de moeda
print("MOEDAS:")
for moeda in moedas:
    count = total_centavos // moeda
    total_centavos %= moeda
    print(f"{count} moeda(s) de R$ {moeda / 100:.2f}")