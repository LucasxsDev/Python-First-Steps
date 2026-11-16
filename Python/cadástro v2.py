#var
from utils import interface
pessoas = [['Ana Paula', 32], ['Cláudia', 30], ['Vorcaro', 54], ['Jessé', 10]]


#program
while True:
    while True:
        try:
            interface.menu.visual()
            verify = int(input('\033[33mSua opção\033[m: '))
            while verify < 1 or verify > 3:
                print('\033[31mERRO: Digite um valor válido.\033[m')
                interface.menu.visual()
                verify = int(input('\033[33mSua opção\033[m: '))
        except (ValueError, TypeError):
            print('\033[31mERRO: Coloque os valores corretos.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mERRO: Espaço vazio.\033[m')
        else:
            break
    
    if verify == 1:
        interface.menu.titulo('PESSOAS CADASTRADAS')
        for c, v in enumerate(pessoas, start=0):
            print(f'{v[0]:<10} {v[1]:>20}')
        interface.menu.linha()

    if verify == 2:
        interface.menu.linha()
        nome = input('\033[33mDigite o nome\033[m: ')
        while True:
            try:
                idade = int(input('\033[33mDigite a idade\033[m: '))
            except(ValueError, TypeError):
                print('\033[31mERRO: Digite um valor válido.\033[m')
            else:
                break
        pessoas.append([nome, idade])
        interface.menu.linha()

    if verify == 3:
        break

print('\033[35mMuito obrigado por testar!\033[m')
interface.menu.linha()