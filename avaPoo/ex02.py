class NotaInvalidaError(Exception):
    pass
class SemNotasError(Exception):
    pass

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    def adicionar_nota(self, nota):
        if 0 < nota > 10:
            raise NotaInvalidaError('Nota inserida é inválida.')
        else:
            self.notas.append(nota)
    def calcular_media(self):
        if self.notas == []:
            raise SemNotasError('Não há notas registradas desse aluno.')
        else:
            return sum(self.notas)/len(self.notas)

def main():
    nome_aluno = input("Digite o nome do aluno: ")
    aluno = Aluno(nome_aluno)
    while True:
        print("\n### Sistema de Gestão de Notas ###")
        print("1 - Adicionar nota")
        print("2 - Calcular média")
        print("3 - Mostrar todas as notas")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nota = int(input("Digite a nota (0 a 10): "))
            aluno.adicionar_nota(nota)
        elif opcao == "2":
            try:
                media = aluno.calcular_media()
                print(f"Média do aluno {aluno.nome}: {media:.2f}")
            except SemNotasError as e:
                print(f"{e}")
        elif opcao == "3":
            print(f"Notas do aluno {aluno.nome}: {aluno.notas}")
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
        except(SemNotasError, NotaInvalidaError) as exc:
            print(exc)