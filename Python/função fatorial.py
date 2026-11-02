#var
def fatorial(n, show=False):
    """
    -> Serve para calcular o fatorial de um número qualquer.
    n = número que deseja ser calculado.
    show = parâmetro opcional para mostrar o processo de cálculo.
    if n == 0, o fatorial será sempre 1.
    else = o fatorial será calculado através de um for, começando do antecessor do valor até o número 1, multiplicando a cada valor.
    """
    from time import sleep
    if n == 0:
        return 1
    else:
        for c in range(n - 1, 0, -1):
            if show == True:
                print(f'{n} x {c}', end=' => ', flush=True)
                sleep(0.5)
            n *= c
        return n


#program
h = input('Deseja ajuda no programa? [S/N]? ').strip().upper()
if h == 'S':
    help(fatorial)
x = int(input('Digite um número para calcular o fatorial: '))
s = input('Deseja mostrar o processo de cálculo? [S/N]? ').strip().upper()
print('-' * 60)
if s == 'S':
    print(f'O fatorial de {x}! é {fatorial(x, show = True)}')
else: 
    print(f'O fatorial de {x}! é {fatorial(x)}')