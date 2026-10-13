velocidade = float(input('Velocidade atual do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi MULTADO, a velocidade limite é de 80Km/h e a sua multa é de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')