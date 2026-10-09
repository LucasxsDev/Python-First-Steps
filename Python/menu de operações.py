resposta = 0 
maior = 0
menor = 9999

print('\033[4;35mOPERAÇÕES\033[m')
print('[ 1 ] somar')
print('[ 2 ] multiplicar')
print('[ 3 ] maior')
print('[ 4 ] novos números')
print('[ 5 ] sair')

while resposta != 5:
    
    print()
    if resposta != 5 and resposta != 4:
        number1 = float(input('digite um número: '))
        print()
        number2 = float(input('Digite outro número: '))      
    print()
    
    resposta = int(input('Oq deseja fazer com esses números? '))
    print()
    
    if resposta == 1:
        soma = number1 + number2
        print('A soma entre {} e {} é igual a: {}'.format(number1, number2, soma))
        
    elif resposta == 2:
        multi = number1 * number2
        print('A multiplicação entre {} e {} é igual a: {}'.format(number1, number2, multi))
        
    elif resposta == 3:
        if number1 > maior:
            maior = number1
            menor = number2
        elif number2 > maior:
            maior = number2
            menor = number2
        else:
            print('Eles são iguais!')
        print('O maior número é o {} e o menor é o {}'.format(maior, menor))
    
    elif resposta == 4:
       number1 = float(input('digite um número: '))
       print()
       number2 = float(input('Digite outro número: '))
       print() 
        
    elif resposta == 5:
        print('Muito obrigado, volte sempre!' )
    else:
        print('Opção invalida, digite um número de 1 a 5.')





        