def calcular_notas(valor): # def é usada para definir uma nova função chamada calcular_notas que aceita um parâmetro valor
    notas = [100, 50, 20, 10, 5, 2, 1] # lista das notas disponíveis 
    quantidade_notas = {} # dicionário vazio para armazenar a quantidade de cada nota necessária 
    # notas.append(0.25)
    # notas = [100, 50, 20, 10, 5, 2, 1, 0.25] # lista das notas disponíveis 
    # del notas[7] ou notas.pop(7)
    for nota in notas: 
        quantidade_notas[nota] = valor // nota
        valor = valor % nota # para cada nota na lista notas, a quantidade de notas necessárias é calculada usando a divisão inteira //. O valor restante é atualizado usando o operador de módulo %

    return quantidade_notas

valor = int(input())

resultado = calcular_notas(valor)

print(f'{valor}')
for nota, quantidade in resultado.items():
    print(f'{quantidade} nota(s) de R$ {nota},00')

"""N = int(input())

print(N)

print(f"{N//100} nota(s) de R$ 100,00")
N %= 100
print(f"{N//50} nota(s) de R$ 50,00")
N %= 50
print(f"{N//20} nota(s) de R$ 20,00")
N %= 20
print(f"{N//10} nota(s) de R$ 10,00")
N %= 10
print(f"{N//5} nota(s) de R$ 5,00")
N %= 5
print(f"{N//2} nota(s) de R$ 2,00")
N %= 2
print(f"{N} nota(s) de R$ 1,00")"""