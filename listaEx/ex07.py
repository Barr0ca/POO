def calcular_media(lista):
    media = sum(lista)/len(lista)
    if lista :
        raise TypeError('A lista contem um elemento que não é número.')
    elif lista == []:
        raise ZeroDivisionError('A lista está vazia.')
    return print(f'A média é {media}')

lista = [10,5,5,10]
try:
    calcular_media(lista)
except (TypeError, ZeroDivisionError, Exception) as exc:
    print(exc)
