class Produto():

    def __init__(self, nome, preco, cor, idProduto = None) -> None:
        self.idProduto = idProduto
        self.nome = nome
        self.preco = preco
        self.cor = cor
    
    