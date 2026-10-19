casa = float(input('Valor do imóvel R$'))
salario = float(input('Salário do comprador R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa/(anos*12)
maximo = salario*0.3

if prestacao <= maximo:
    print(f'O valor da prestação mensal seria de R${prestacao:.2f}')
    print('Empréstimo APROVADO!')
else: 
    print(f'O valor da prestação mensal seria de R${prestacao:.2f}')
    print('Empréstimo NEGADO!')