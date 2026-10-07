import random
import pygame
print('Escolhendo...')

list = [0, 1, 2, 3, 4, 5]
e = random.choice(list)

pygame.time.wait
input()

print('Tente descobrir qual número eu escolhi entre 0 e 5.')
n = int(input())
if n < 0 and n > 5:
    print('Não valeu :(')
if n == e:
    print('Você acertou, parabéns!')
else:
    print('Você errou :( tente na próxima!')
