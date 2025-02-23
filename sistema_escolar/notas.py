from alunos import listaAlunos
from utilitarios import formatacao

def atribuirNota(nome, nota):
  if nome in listaAlunos:
    listaAlunos[nome].append(nota)
    print(f'Nota atribuída ao aluno {nome}.')
  else:
    print(f'Aluno {nome} não encontrado.')

def calcularMedia(nome):
  if nome in listaAlunos and listaAlunos[nome]:
    media = sum(listaAlunos[nome]) / len(listaAlunos[nome])
    return formatacao.formatarMedia(media)
  else:
    print(f'Aluno {nome} não tem notas cadastradas.')
    return None