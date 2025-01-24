class ArquivoTexto:
    nome_arquivo = None

    def __init__(self, nome_arquivo:str):
        self.nome_arquivo = nome_arquivo

    def ler_arquivo(self):
        arq = open(self.nome_arquivo, 'r+')
        conteudo = arq.read()
        print('Conteúdo do arquivo:')
        print(conteudo)


    def gravar_conteudo(self, escrito):
        arq = open(self.nome_arquivo, 'r+')
        arq.write(escrito) 

arquivo01 = ArquivoTexto('arquivo.txt')

try: 
    arquivo01.ler_arquivo()
except Exception:
    raise

try: 
    arquivo01.gravar_conteudo('BATATA')
except Exception:
    raise

arquivo01.ler_arquivo()