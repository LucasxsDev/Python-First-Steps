compras = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,  'Estojo', 25.00, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

titulo = '\033[4;32mLISTAGEM DE COMPRAS\033[m'
print('-' * 50)
print(f'{titulo:^60}')
print('-' * 50)

for c in range(0, len(compras), 2):
    print(f'{compras[c]:.<40} R$ {compras[c+1]:>6.2f}')
    
print('-' * 50)
