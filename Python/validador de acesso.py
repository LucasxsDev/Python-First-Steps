#var
from urllib.request import urlopen



#program
try:
    urlopen('https://www.python.org/', timeout=5)
except Exception as erro:
    print()
    print('\033[31mO site não está acessível no momento\033[m.')
    print(f'\033[31mERRO\033[m: {erro.__class__}')
    print()
else:
    print()
    print('\033[33mConsegui acessar o site com sucesso\033[m!')
    print()
finally:
    print('\033[33mObrigado pelo teste\033[m!')
