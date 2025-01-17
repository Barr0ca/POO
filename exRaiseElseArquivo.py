import io

def abrirArquivo(nomeArquivo: str):
    try:
        arquivo = open(nomeArquivo, 'r+')  

        imprimirConteudo(arquivo)

        escreverNoArquivo(arquivo)
    except FileNotFoundError:
        print('Não consegui abrir o arquivo')
    except io.UnsupportedOperation:
        print('Não consegui abrir para escrita')
        raise
    except PermissionError:
        print('Não tenho permissão para manipular o arquivo')
    else: #É executado se nenhum except for acionado
        print('Fechando arquivo...')
        arquivo.close()

def imprimirConteudo(arquivo):
    conteudo = arquivo.read()

    print('Conteúdo do arquivo:')
    print(conteudo)

def escreverNoArquivo(arquivo):
    arquivo.write('Conteúdo escrito\n')

try:
    abrirArquivo('arquivo.txt')
except:
    print('Chegou alguma exceção.')
