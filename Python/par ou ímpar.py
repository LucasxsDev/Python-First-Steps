import random
import time
win = True
vitorias_seguidas = 0
print('-=' * 20)
print('\033[35m{:^35}\033[m'.format('PAR OU ÍMPAR'))
print('-=' * 20)

while True:
    
    print()
    valor = int(input('Digite um valor: [1 - 10] '))
    escolha = input('Par ou Ímpar? [P/I] ').lower()
    
    valorpc = random.randint(1, 10)
    if escolha == 'p':
        escolhapc = 'i'
    else:
        escolhapc = 'p'
        
    if (valor + valorpc) % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
        
    print()
    print(f'Você jogou \033[35m{valor}\033[m e o computador \033[35m{valorpc}\033[m. A soma deu \033[35m{valor + valorpc}\033[m, que é um número \033[35m{resultado}\033[m.')
    print('-=' * 33)
    print()
    print('Calculando resultado...')
    print()
    time.sleep(2)
    
    if (valor + valorpc) % 2 == 0 and escolha == 'p':
        win = True
        vitorias_seguidas += 1
     
        print('\033[32mVOCÊ GANHOU\033[m! -> CONTINUE O JOGO')
        print('-=' * 20)
    elif (valor + valorpc) % 2 == 1 and escolha == 'i':
        win = True
        vitorias_seguidas += 1
       
        print('\033[32mVOCÊ GANHOU\033[m! -> CONTINUE O JOGO')
        print('-=' * 20)
    else:
     
        print(f'\033[31mVOCÊ PERDEU\033[m! -> A QUANTIDADE DE VITÓRIAS SEGUIDAS FOI: \033[35m{vitorias_seguidas}\033[m')
        print('-=' * 30)
        win = False
        
    if win == False:
        break
print()
print('Muito obrigado por jogar! Volte sempre!')
print('-=' * 20)
