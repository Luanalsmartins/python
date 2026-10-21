from datetime import date
ano_atual = date.today().year
s = 0

for c in range (1, 8):
    an = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = ano_atual - an
    if idade >= 21:
        s += 1
print(f'{s} pessoas tem mais de 18 anos.')
print(f'{7-s} pessoas tem menos de 18 anos.')