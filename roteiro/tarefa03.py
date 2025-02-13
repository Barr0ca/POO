with open("meus_dados.txt", "a") as arquivo:
    arquivo.write("\nCidade: Currais Novos")
with open("meus_dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)