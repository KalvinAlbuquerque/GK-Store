from common.produto import Produto

class Categoria():

    def __init__(self, nome: str, produtos: list[Produto] = None) -> None:
        self.nome = nome
        self.produtos = produtos