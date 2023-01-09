#Exercício - Quiz

perguntas = [
    {
        'Pergunta': 'Quanto é 2 x 2 ?',
        'Alternativas': ['A) 2', 'B) 3', 'C) 4', 'D) 6'],
        'Resposta': 'C',
    },
    {
        'Pergunta': 'Quanto é 55 + 71 ?',
        'Alternativas': ['A) 133', 'B) 123', 'C) 136', 'D) 126'],
        'Resposta': 'D',
    },
    {
        'Pergunta': 'Quem descobriu o Brasil?',
        'Alternativas': ['A) Santos Dumont', 'B) Tiradentes', 'C) Pedro Álvares Cabral', 'D) Dom Pedro I'],
        'Resposta': 'C',
    },
]

qtd_acertos = 0

for pergunta in perguntas:
    
    print('Pergunta:', pergunta['Pergunta'])
    print()

    for alternativa in pergunta['Alternativas']:
        print(alternativa)
    print()

    escolha = input('Escolha uma alternativa: ').upper()
    
    if escolha == pergunta['Resposta']:
        print('✔️ Acerto Mizeravi!')
        qtd_acertos += 1
    else:
        print('❌ Erroouuu!')
    print()

if qtd_acertos > 0:
    print('⭐ Parabéns você acertou', qtd_acertos, 'de', len(perguntas), 'perguntas! ⭐')
    print()
else:
    print('❌❌ Nãão, cê é burro cara que loucura! ❌❌')
    print()

