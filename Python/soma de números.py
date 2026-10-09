n = 1
soma= 0
contador = 0
print('\033[4;35mLEITOR DE NÚMEROS\033[m')
print('Para parar, digite: \033[4;35m999\033[m')
print()
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        contador += 1
        soma += n
    if n == 999:
        break
print()
print('Foram digitados {} valores.'.format(contador))
print('A soma entre todos os valores foi de: {}'.format(soma))