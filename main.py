from calculo import *

nome = input('Qual seu nome?:  \n')
print('Seja Bem vindo,', nome,'!\n')
usar = input('Digite sim se você deseja usar a calculadora\n')
usar.title()

if usar == 'sim':
    print('\t   Calculadora de C e F   \n')

    print('1. Para Celsius')
    print('2. Para Fah')

    a = int(input('Qual você deseja fazer? \n Escreva aqui: '))

    if a == 1:
        print('De Fah para Celsius\n')
        c = int(input('Coloque o valor: '))
        print('\nDe Fah para Celsius = {}'.format(Fah(c)))

    if a == 2:
        print('De Celsius para Fah\n')
        c = int(input('Coloque o valor: '))
        print('\nDe Celsius para Fah = {}'.format(celsius(c)))

    if a == 3:
        print('Até logo, b')

elif usar != 'sim':
    print('Até logo,', nome)
