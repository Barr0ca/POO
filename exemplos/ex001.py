from random import randint
from time import sleep
from typing import List

class Pneu:
    vida_util = 1
    aderencia = 1

    def __init__(self, aderencia):
        self.aderencia = aderencia

    def calcular(self, velocidade):
        nova_velocidade = (self.aderencia * velocidade) * self.vida_util

        self.vida_util -=  randint(1,10)/100

        if (self.vida_util <= 0):
            raise Exception('Pneu estourou.')

        return nova_velocidade

class Carro:
    # Atributos privados
    __identificacao = None
    __velocidade = None

    # Atributos protegidos
    _quebrado = False
    _pneu = Pneu(1)

    def __init__(self, identificacao, velocidade = 1):
        self.__identificacao = identificacao
        self.__velocidade = velocidade

    def iniciar(self):
        print(f'{self.__identificacao} iniciou a corrida.')

    def acelerar(self, quantidade):
        if not self._quebrado:
            try:
                self.__velocidade += self._pneu.calcular(quantidade)
            except Exception:
                print(f'{self.__identificacao} entrou no pit-stop.')
                self._pneu = Pneu(1)

    def parar(self):
        self.__velocidade = 0
        self._quebrado = True

    # Permite apenas a leitura do atributo velocidade
    # Metodo Getter
    def velocidade(self):
        return self.__velocidade
    
    # Permite apenas a leitura do atributo identificação
    # Metodo Getter
    def identificacao(self):
        return self.__identificacao
    
    # Permite apenas a leitura do atributo quebrado
    # Metodo Getter
    def quebrado(self):
        return self._quebrado

class Ferrari(Carro):
    def acelerar(self, quantidade):
        # O super permite modificar um método da calsse ancestral
        super().acelerar(quantidade*1.5)

class Corrida:
    carros = None
    velocidades = []
    rodadas = None

    def __init__(self, carros:List[Carro], rodadas):
        self.carros = carros
        self.rodadas = rodadas
        for i in range(len(self.carros)):
            self.velocidades.append(0)

    def largada(self):
        for carro in self.carros:
            carro.iniciar()

    def calcular_turno(self):
        for idx, carro in enumerate(self.carros):
            # Sorteio de acidente
            if (randint(0,100) <= 1) and (not carro.quebrado()):
                print(f'Grave acidente na pista, {carro.identificacao()} bateu na curva')
                carro.parar()
            
            # Sortei de aceleração
            if (randint(0, 100) <= 50):
                carro.acelerar(randint(2, 7))

            self.velocidades[idx] += carro.velocidade()

    def ranking(self):
        # Lista de tuplas do tipo: [ (0, 25), (1, 10) ]
        nova_lista = enumerate(self.velocidades)
        ordenado = sorted(nova_lista, key=lambda carro: carro[1], reverse=True)
        print('Ranking:')

        posicao = 1
        for idx, velocidade in ordenado:
            print(f'{posicao}: {self.carros[idx].identificacao()} ({velocidade:.2f})')
            posicao += 1

    def corrida(self):
        for i in range(self.rodadas):
            self.calcular_turno()

            sleep(1.5)
            print('')
            self.ranking()

        # for idx, carro in enumerate(self.carros):
        #     print(f'Velocidade total de {carro.identificacao} foi {self.velocidades[idx]}')
        
        # self.ranking()
    
    def executar(self):
        self.largada()
        self.corrida()

carros = [
    Carro('Senna'),
    Ferrari('Shummacher'),
    Carro('Hamilton'),
    Carro('Verstappen'),
    Carro('Massa'),
    Carro('Bottas')
]


corrida = Corrida(carros, 16)
# corrida.largada()
# corrida.corrida()
corrida.executar()