class PorcentagemInvalidaError(Exception):
    pass

class Funcionario:
    nome = None
    salario = float

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, porcentagem): 
        if porcentagem <= 0:
            raise PorcentagemInvalidaError('Porcentagem inválida')
        self.salario = (self.salario * (porcentagem/100))+self.salario

    def mostrar_salario(self):
        print(f'Salario de {self.nome}: {self.salario:.2f}')

class Gerente(Funcionario):
    departamento = None

gerente01 = Gerente('Pedro', 5000)

gerente01.mostrar_salario()

try:
    gerente01.aumentar_salario(1)
except PorcentagemInvalidaError as exc:
    print(exc)

gerente01.mostrar_salario()
