#var
notas = []
verify = 's'
def analisar_notas(lst, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    Maior = maior nota do aluno.
    Menor = menor nota do aluno.
    Total = total de notas do aluno.
    Média = soma das notas do aluno / total de notas do aluno.
    situação = opcional, mostra a situação do aluno de acordo com a média das notas.
    """
    result = {'Total':len(lst),
           'Maior':max(lst),
           'Menor':min(lst),
           'Média': sum(lst) / len(lst)}
    
    if sit == True:
        if result['Média'] >= 5 and result['Média'] < 7:
            result['Situação'] = 'Razoável'
        elif result['Média'] >= 7:
            result['Situação'] = 'Muito boa'
        else:
            result['Situação'] = 'Ruim'

    return result


#program
print('-' * 40)
while verify == 's':
    notas.append(float(input('Digite a nota do aluno: ')))
    verify = input('Deseja continuar? [S/N] ').strip().lower()
    if verify != 's' and verify != 'n':
        while verify != 's' and verify != 'n':
            verify = input('Tente novamente. Deseja continuar? [S/N] ').strip().lower()

s = input('Deseja mostrar a situação do aluno? [S/N] ').strip().lower()
if s == 's':
    print(analisar_notas(notas, sit=True))
else:
    print(analisar_notas(notas))
