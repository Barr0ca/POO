import alunos
from notas import atribuirNota, calcularMedia

while True:
  print('\nSistema Escolar')
  print('1 - Cadastrar aluno')
  print('2 - Listar alunos')
  print('3 - Atribuir nota')
  print('4 - Calcular média')
  print('0 - Sair')

  opcao = int(input('Seleciona uma opção: '))

  if opcao == 0:
    print('Saindo do sistema...')
    break
  elif opcao == 1:  
    nome = input('\nNome do aluno: ')
    alunos.cadastrarAluno(nome)
  elif opcao == 2:
    alunos.listarAlunos()
  elif opcao == 3:
    nome = input('\nNome do aluno: ')
    nota = float(input('Nota: '))
    atribuirNota(nome, nota)
  elif opcao == 4:
    nome = input('\nNome do aluno: ')
    media = calcularMedia(nome)
    if media is not None:
      print(f'\nA média do aluno {nome} é {media}')
  else:
    print('Opção inválida.')