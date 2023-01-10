import pandas as pd

tabela = pd.read_excel("ListaPecas.xlsx")

for n in range(150):
    numero_de_linhas = 0
    marca = tabela.loc[n,"Marca"]
    if (marca == "Fim"):
        numero_de_linhas = n
        break

for n in range(numero_de_linhas):
    marca = tabela.loc[n,"Marca"]
    modelo = tabela.loc[n,"Modelo"]
    cor = tabela.loc[n,"Cor"]
    grau_importancia = tabela.loc[n,"Grau de Importancia"]
    grau_importancia.strip()
    if (grau_importancia=="Exceção"):
        grau_importancia="E"
    elif (grau_importancia=="Baixo"):
        grau_importancia="B"
    elif (grau_importancia=="Médio Baixo"):
        grau_importancia="MB"
    elif (grau_importancia=="Médio"):
        grau_importancia="M"
    elif (grau_importancia=="Alto"):
        grau_importancia="A"
    quantidade = int(tabela.loc[n,"Numero"])
    print('("{}" , "{}" , "{}" , {} , "{}"),'.format(marca,modelo,cor,quantidade,grau_importancia))
    