distancia = int(input('Digite a distância da viagem em Km: '))

if distancia <= 200:
    preco = distancia*0.50
    print(f'O preço da passagem é {preco:.2f}')
else:
    preco = distancia*0.45
    print(f'O preço da passagem é {preco:.2f}')