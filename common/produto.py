class Produto():

    def __init__(self, nome, preco, cor, idProduto = None) -> None:
        self.idProduto = idProduto
        self.nome = nome
        self.preco = preco
        self.cor = cor

    def printProduto(self) -> None:

        print(f"Nome -> {self.nome}\nPreco -> {self.preco}\nCor -> {self.cor}\nID -> {self.idProduto}")
    
    