import time
import random
jogos = []

print('-' * 30)
print(f'\033[35m{'JOGO DA MEGA SENA':^30}\033[m')
print('-' * 30)

qnt = int(input('Quantos jogos você quer que eu sorteie? '))
print()
print(f'-=-=-= SORTEANDO \033[35m{qnt}\033[m JOGOS -=-=-=')
print()

for c in range(1, qnt+1):
    for cont in range(1, 7):
        jogos.append(random.randint(1, 60))
    print(f'jogo \033[35m{c}\033[m: {jogos}')
    time.sleep(1)
    jogos = []
    
print()
print(f'-=-=-=-=\033[35m < BOA SORTE! >\033[m-=-=-=-=')
print()