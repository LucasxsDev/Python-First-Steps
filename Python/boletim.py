dados_aluno = []
notas_aluno = []
verify = 's'
verify2 = 0

while verify == 's':
    nome = input('Nome: ')
    print()
    nota1 = float(input('Nota 1: '))
    print()
    nota2 = float(input('Nota 2: '))
    print()
    notas_aluno.append([nota1, nota2])
    media = (nota1 + nota2) / 2
    if media > 7:
        resultado = 'APROVADO'
    elif media >= 5 and media <= 7:
        resultado = 'EM RECUPERAÇÃO'
    else:
        resultado = 'REPROVADO'
    dados_aluno.append([nome, media, resultado])
    verify = input('Deseja continuar? [S/N] ').lower()
    print()
    if verify != 's' and verify != 'n':
        while verify != 's' and verify != 'n':
            verify = input('ERRO. Tente novamente: [S/N] ').lower()
            print()
            
print('=-' * 20)
print(f'No. {'\033[35mNOME\033[m'}         {'\033[35mMÉDIA\033[m'}    {'\033[35mRESULTADO\033[m'}')
print('-' * 40)
for c, v in enumerate(dados_aluno, start=1):
    print(f'{c}. \033[35m{v[0]:<10}\033[m \033[35m{v[1]:^10}\033[m \033[35m{v[2]:>10}\033[m')
print('-' * 40)

while verify2 != 999:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print()
    if aluno == 999:
        break
    if aluno == c:
        print(f'As notas de \033[35m{dados_aluno[aluno-1][0]}\033[m são: \033[35m{notas_aluno[aluno-1]}\033[m')
        print()
    else:
        print()
        print('Aluno não encontrado...')
        print()
print('Muito obrigado! Volte sempre!')