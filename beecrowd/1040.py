N1, N2, N3, N4 = input().split()

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

media = ((N1*2) + (N2*3) + (N3*4) + (N4*1)) / 10

if media >= 5.0 and media <= 6.9:
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    exame = float(input())
    recalculo_media = (media + exame) / 2 
    if recalculo_media >= 5.0: 
        print(f'Nota do exame: {exame:.1f}')
        print('Aluno aprovado.')
        print(f'Media final: {recalculo_media:.1f}')
    else: 
        print(f'Nota do exame: {exame:.1f}')
        print('aluno reprovado.')
        print(f'Media final: {recalculo_media:.1f}')

elif media >= 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif media < 5.0:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
