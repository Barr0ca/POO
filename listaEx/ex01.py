class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    titular = 1
    saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError('Saldo insuficiente')
        self.saldo -= valor

    def extrato(self):
        print(f'O saldo é R$ {self.saldo:.2f}')

conta = ContaBancaria()

conta.depositar(500)

try:
    conta.sacar(501)
except SaldoInsuficienteError as exc:
    print('Saldo insuficiente')

conta.extrato()    