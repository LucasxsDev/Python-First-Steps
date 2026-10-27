import time
from random import randint
dados = {}
ranking = []

input('Toque para iniciar...')
print()

for c in range (1, 5):
    dados[str(c)] = randint(1, 6)
for k, v in dados.items():
    print(f'O jogador {k} tirou {v} no dado.')
    ranking.append([k, v])
    time.sleep(1)

print('=-' * 30)
print('==== RANKING ====')
ranking.sort(key=lambda item: item[1], reverse=True)
for c, v in enumerate(ranking,start=1):
   print(f'    {c}° lugar: Jogador {v[0]} com {v[1]}')
   