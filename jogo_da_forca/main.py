import os

palavra_secreta = 'esqueleto'
letras_acertadas = ''
numero_tentativas = 0
historico_letras = ''
palavra_formada = ''

while True:
    
    os.system('cls')
    print('Histórico de Letras:', historico_letras)
    print('Palavra Secreta:', palavra_formada)
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    

    if len(letra_digitada) > 1:
        if letra_digitada == palavra_secreta:
            palavra_formada = letra_digitada
        else:
            continue
    else:
        historico_letras += letra_digitada

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada    
    
    palavra_formada = ''

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'


    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('PARABÉNS, VOCÊ ACERTOU!')
        print('A palavra era:', palavra_secreta)
        print('Número de tentativas:', numero_tentativas)
        input('Pessione "Enter" para jogar novamente.')
        
        palavra_formada = ''
        letras_acertadas = ''
        numero_tentativas = 0
        historico_letras = ''

        for letra in palavra_secreta:
            palavra_formada += '*'
