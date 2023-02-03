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
        for Pecas.id, Pecas.marca, Pecas.modelo, Pecas.cor, Pecas.grau_de_importancia, Pecas.quantidade in dados:
            lista = lista + " " + str(Pecas.id) + " " + str(Pecas.marca) + " " + str(Pecas.modelo) + " " + str(Pecas.cor) + " " + str(Pecas.grau_de_importancia) + " " + str(Pecas.quantidade) + "\n"
        return lista
        