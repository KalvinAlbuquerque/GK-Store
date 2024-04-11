from common.produto import Produto
from common.catagoria import Categoria
import json

class TabelaProdutos():

    def __init__(self, tabela: dict) -> None:
        self.tabela = tabela

    def insert(self, value: Produto) -> Produto:

        novo_produto = {
            "nome" : value.nome,
            "preco" : value.preco,
            "cor" : value.cor
        }

        novo_id = 0

        if (len(self.tabela) > 0):

            novo_id = int(list(self.tabela.keys())[-1]) + 1

        self.tabela[novo_id] = novo_produto

        return Produto(value.nome, value.preco, value.cor, novo_id)

    def delete(self, id) -> None:

        self.tabela.pop(id)

    def update(self, value: Produto) -> None:
        pass

    def get(self, id) -> Produto:
        pass

class TabelaCategorias():

    def __init__(self, tabela: dict) -> None:
        self.tabela = tabela

    def insert(self, value: Categoria) -> None:
        pass

    def delete(self, id) -> None:
        pass

    def update(self, value: Categoria) -> None:
        pass

    def get(self, id) -> Categoria:
        pass

class TabelaPrincipal():

    def __init__(self, jsonPath) -> None:
        self.tabela = self.loadJson(jsonPath)
        self.produtos = TabelaProdutos(self.tabela["catalogo"]["produtos"])
        self.categorias = TabelaProdutos(self.tabela["catalogo"]["categorias"])

    def getTabelaProdutos(self) -> TabelaProdutos:
        
        return self.produtos
    
    def getTabelaCategorias(self) -> TabelaCategorias:
        
        return self.categorias

    def loadJson(self, jsonPath) -> dict:

        with open(jsonPath, "r") as file:
            tabela = json.load(file)

        return tabela

