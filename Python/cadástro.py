pessoas_velhas = 0 
mulheres_novas = 0
homens = 0
while True:
    idade = int(input('digite a sua idade: '))
    sexo = input('Digite o seu sexo: [M/F] ').lower()
    flag = input('Quer continuar? [S/N] ').lower()
    if idade > 18:
        pessoas_velhas += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade <= 20:
        mulheres_novas += 1
    if flag == 'n':
        break
print(f'Maiores de idade cadastrados: {pessoas_velhas}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos cadastradas: {mulheres_novas}')
print('Obrigado! Volte sempre!')