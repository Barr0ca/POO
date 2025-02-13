import pickle

class Contato:
    nome: str
    telefone: str
    email: str

    def __init__(self, nome, telefone, email):
        self.nome: nome
        self.telefone: telefone
        self.email: email

listaContatos = []

while True:
    print('Adicionar um novo contato - 1')
    print('Visualizar lista de contatos - 2')
    print('Sair - 0')
    opcao = int(input('\nSelecione uma opcão: '))

    if opcao == 1:
        nome = input('Nome: ')
        telefone = input('Telfone: ')
        email = input('Email: ')
        contato = Contato(nome, telefone, email)

        with open('contatos.pkl', 'wb') as arquivo:
            pickle.dump(contato, arquivo)
    elif opcao == 2:
        with open('contatos.pkl', 'rb') as arquivo:
            dados_carregados = pickle.load(arquivo)
            print(dados_carregados)
    elif opcao == 0:
        break