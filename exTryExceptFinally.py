def function01():
    print('INÍCIO DA FUNÇÃO 01')
    print('Calculadora de divisão.')
    num1 = float(input('Informe a o primeiro número: '))
    num2 = float(input('Informe a o segundo número: '))
    try:
        function02(num1, num2)
    except ZeroDivisionError:
        print('NÃO PODE DIVIDIR POR ZERO.')
    finally:
        print('FINALLY DA FUNÇÃO 01.')
    print('FIM DA FUNÇÃO 01')


def function02(num1, num2):
    divisao = float(num1 / num2)
    print(f'Divisão: {divisao}')
    print('FIM DA FUNÇÃO 02')

try:
    function01()
except ValueError:
    print('INFORME UM NÚMERO.')
except:
    print('Ocorreu uma exceção na função 01.')
