class AssentosInsuficientesError(Exception):
    pass

class CancelamentoInvalidoError(Exception):
    pass

class ReservaVoo:
    def __init__(self, voo_numero, lugares_disponiveis):
        self.voo_numero = voo_numero
        self.lugares_disponiveis = lugares_disponiveis
    def reservar_lugar(self, quantidade):
        if self.lugares_disponiveis < quantidade:
            raise AssentosInsuficientesError('Quantidade de assentos insuficientes.')
        else:
            self.lugares_disponiveis -= quantidade
    def cancelar_reserva(self, quantidade):
        if quantidade > self.lugares_disponiveis:
            raise CancelamentoInvalidoError('Quantidade maior do que antes reservada.')
        else:
            self.lugares_disponiveis += quantidade

def main():
    voo = ReservaVoo("AB123", 10) # Criando uma reserva com 10 lugares disponíveis
    while True:
        print("\n### Sistema de Reserva de Passagens ###")
        print("1 - Reservar um lugar")
        print("2 - Cancelar uma reserva")
        print("3 - Mostrar assentos disponíveis")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            try:
                quantidade = int(input("Quantos lugares deseja reservar?"))
                voo.reservar_lugar(quantidade)
            except ValueError:
                print("Erro: Insira um número inteiro válido.")

        elif opcao == "2":
            try:
                quantidade = int(input("Quantos lugares deseja cancelar?"))
                voo.cancelar_reserva(quantidade)
            except ValueError:
                print("Erro: Insira um número inteiro válido.")
        elif opcao == "3":
            print(f"Assentos disponíveis: {voo.lugares_disponiveis}")
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    while True: 
        try:
            main()
            break
        except (AssentosInsuficientesError, CancelamentoInvalidoError) as exc:
            print(exc)