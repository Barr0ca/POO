import datetime

class Usuario:
    nome = str
    senha = str

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        # return print(f'Usuário: {nome}\nSenha: {senha}\n{datetime.datetime.now()}')

    def escrever_arquivo(self, arq):
        arqAberto = open(arq, 'r+')
        arqAberto.write(f'[ {self.nome}, {datetime.datetime.now()} ]')



nomeUsuario = input('Informe o usuário: ')
senhaUsuario = input('Informe a senha do usuario: ')

usuario01 = Usuario(nomeUsuario, senhaUsuario)
Usuario.escrever_arquivo('auditoria_autenticacao.txt')