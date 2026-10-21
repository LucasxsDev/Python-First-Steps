pessoas = []
maioridade = menoridade =  0

for c in range(5):
    nome = input('Qual o seu nome? ')
    print()
    idade = int(input('Qual a sua idade? '))
    print()
    pessoas.append([nome, idade])

print('=-'* 15)
for c, p in enumerate(pessoas, start=1):
    print(f'{c}. {p[0]} - {p[1]} anos de idade')
print('=-'* 15)

print('=-'* 30)
for p in pessoas:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        maioridade += 1
    else:
        print(f'{p[0]} é menor de idade')
        menoridade += 1
print()
print(f'{maioridade} são maiores de idade e {menoridade} são menores de idade.')
print('=-'* 30)
