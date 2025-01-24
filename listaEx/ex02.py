class ValorInvalideError(Exception):
    pass

class Produto:
    nome = None
    preco = float
    estoque = int

    def __init__(self, nome, preco, estoque):
        if preco <= 0 or estoque <= 0:
            raise ValorInvalideError('Valores como preço e estoque devem ser positivos')
        return print(f'{nome}\nR$ {preco:.2f}\n{estoque} em estoque')
    
try:
    produto01 = Produto('Calça Jeans', 4, -3)
except  ValorInvalideError as exc:
    print(exc)