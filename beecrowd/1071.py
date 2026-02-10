x = int(input())
y = int(input())

# Garantir que x seja menor que y
if x > y:
    x, y = y, x

# Calcular a soma dos números entre x e y 
soma_impares = 0
for num in range(x + 1, y): # range é usado para gerar uma sequência de números começando em x + 1 e terminando em y - 1 
    if num % 2 != 0:
        soma_impares += num

print(soma_impares)