import pickle

with open("dados.pkl", "rb") as arquivo:
    dados_carregados = pickle.load(arquivo)
    print(dados_carregados)