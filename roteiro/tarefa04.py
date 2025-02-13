import pickle

dados = {"nome": "Ian", "idade": 19, "cidade": "Currais Novos", "profissão": "Estudante"}

with open("dados.pkl", "wb") as arquivo:
    pickle.dump(dados, arquivo)