listaAlunos = {}

def cadastrarAluno(nome):
  if nome in listaAlunos:
    print(f'Aluno {nome} já está cadastrado.')
  else:
    listaAlunos[nome] = []
    print(f'Aluno {nome} cadastrado.')
  
def listarAlunos():
  if not listaAlunos:
    print('\nNenhum aluno cadastrado.')
  else:
    print('\nAlunos cadastrados no sistema:')
    for aluno in listaAlunos:
      print(f'{aluno}')