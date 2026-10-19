from datetime import date
an = int(input('Informe o ano de nascimento: '))
ano = date.today().year
idade = ano-an

print(f'Quem nasceu em {an} tem {idade} anos em {ano}.')

if idade < 18:
    saldo = 18 - idade
    print(f'Você vai se alistar em {saldo} anos.')
    print(f'Seu alistamento será em {ano + (saldo)}')
elif idade == 18:
    print('Já é hora de se alistar!')
else:
    saldo = idade - 18
    print(f'Você deveria ter se alistado à {saldo} anos.')
    print(f'Seu alistamento foi em {ano - (saldo)}')