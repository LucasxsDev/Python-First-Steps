import random
print("Bem-vindo ao jogo de \033[32mPedra\033[m, \033[31mPapel\033[m e \033[34mTesoura\033[m!")
print('\033[35mescolhendo\033[m...')
p = 'pedra'
pa = 'papel'
t = 'tesoura'
pc = random.choice([p, pa, t])
input('aperte \033[35mENTER\033[m para continuar!')
print()
esc = input('Escolha entre \033[32mPedra\033[m, \033[31mPapel\033[m e \033[34mTesoura\033[m: ').lower()
print()
print('O computador escolheu \033[35m{}\033[m'.format(pc))
print()
if esc == pc:
    print('\033[4;33mEmpate!\033[m')
elif (esc == p and pc == t) or (esc == pa and pc == p) or (esc == t and pc == pa):
     print('\033[4;32mVocê venceu!\033[m')
else:
    print('\033[4;31mVocê perdeu!\033[m')