class Pecas():
    def __init__(self,id,marca,modelo,cor,grau_importancia,quantidade):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.grau_importancia =  grau_importancia
        self.quantidade = quantidade

    def buscar_pecas(dados):
        lista = ""
        for Pecas.id, Pecas.marca, Pecas.modelo, Pecas.cor, Pecas.quantidade , Pecas.grau_de_importancia, Pecas.caixa in dados:
            lista = lista + " " + str(Pecas.id) + " " + str(Pecas.marca) + " " + str(Pecas.modelo) + " " + str(Pecas.quantidade) + " " + str(Pecas.cor) + " " + str(Pecas.grau_de_importancia) + " " + str(Pecas.caixa) + "\n"
        return lista
        