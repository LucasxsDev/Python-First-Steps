escolha = 's'
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão dessa progressão: '))
n = int(input('Quantos termos deseja mostrar? '))
an = a1 + ( n - 1) * r
for c in range(a1, an + 1, r):
    print(c, end=' => ')
print('FIM')
while escolha == 's':
    print()
    escolha = str(input('Você deseja continuar a progressão? [S/N] ')).lower()
    print()
    if escolha == 's':
        continuação = int(input('QUantos termos a mais você deseja mostrar?  '))
        print()
        an = a1 + ( continuação  + n - 1) * r
        for cc in range(c + r, an + 1, r):
            print(cc, end=' => ')
        print('FIM')
        n = n + continuação  
        c = cc  
print('Muito obrigado!')