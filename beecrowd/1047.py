h_inicio, m_inicio, h_fim, m_fim = input().split()

h_inicio = int(h_inicio)
m_inicio = int(m_inicio)
h_fim = int(h_fim)
m_fim = int(m_fim)

if h_inicio == m_inicio == h_fim == m_fim:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')

elif h_inicio == h_fim and m_inicio > m_fim:
    duracao_jogo_horas = h_fim - h_inicio + 23
    duracao_jogo_minutos = m_fim - m_inicio + 60
    print(f'O JOGO DUROU {duracao_jogo_horas} HORA(S) E {duracao_jogo_minutos} MINUTO(S)')

elif h_inicio == h_fim and m_inicio < m_fim:
    duracao_jogo_minutos = m_fim - m_inicio 
    print(f'O JOGO DUROU 0 HORA(S) E {duracao_jogo_minutos} MINUTO(S)')

elif h_inicio > h_fim and m_inicio > m_fim:
    duracao_jogo_horas = h_fim - h_inicio + 23
    duracao_jogo_minutos = m_fim - m_inicio + 60
    print(f'O JOGO DUROU {duracao_jogo_horas} HORA(S) E {duracao_jogo_minutos} MINUTO(S)')

elif h_inicio > h_fim and m_inicio < m_fim:
    duracao_jogo_horas = h_fim - h_inicio + 24
    duracao_jogo_minutos = m_fim - m_inicio
    print(f'O JOGO DUROU {duracao_jogo_horas} HORA(S) E {duracao_jogo_minutos} MINUTO(S)')

elif h_inicio < h_fim and m_inicio > m_fim:
    duracao_jogo_horas = h_fim - h_inicio - 1
    duracao_jogo_minutos = m_fim - m_inicio + 60
    print(f'O JOGO DUROU {duracao_jogo_horas} HORA(S) E {duracao_jogo_minutos} MINUTO(S)')

elif h_inicio < h_fim and m_inicio < m_fim:
    duracao_jogo_horas = h_fim - h_inicio
    duracao_jogo_minutos = m_fim - m_inicio
    print(f'O JOGO DUROU {duracao_jogo_horas} HORA(S) E {duracao_jogo_minutos} MINUTO(S)')

'''
def calcular_duracao(hora_inicial, minuto_inicial, hora_final, minuto_final):
    # Converte as horas e minutos de início e fim em minutos totais
    inicio_em_minutos = hora_inicial * 60 + minuto_inicial
    fim_em_minutos = hora_final * 60 + minuto_final
    
    # Calcula a duração em minutos
    if fim_em_minutos >= inicio_em_minutos:
        duracao_em_minutos = fim_em_minutos - inicio_em_minutos
    else:
        duracao_em_minutos = (24 * 60 - inicio_em_minutos) + fim_em_minutos
    
    # Converte a duração de minutos de volta para horas e minutos
    duracao_horas = duracao_em_minutos // 60
    duracao_minutos = duracao_em_minutos % 60
    
    return duracao_horas, duracao_minutos

# Entrada do usuário
hora_inicial = int(input("Hora inicial: "))
minuto_inicial = int(input("Minuto inicial: "))
hora_final = int(input("Hora final: "))
minuto_final = int(input("Minuto final: "))

# Calcula a duração do jogo
duracao_horas, duracao_minutos = calcular_duracao(hora_inicial, minuto_inicial, hora_final, minuto_final)

# Exibe o resultado
print(f"A duração do jogo foi de {duracao_horas} hora(s) e {duracao_minutos} minuto(s).") '''