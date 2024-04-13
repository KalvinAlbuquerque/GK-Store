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

    def updateCor(self, produtoID: int, cor: str) -> None:
        self.__update__(produtoID, "cor", cor)

    def updateNome(self, produtoID, nome: str) -> None:
        self.__update__(produtoID, "nome", nome)

    def updatePreco(self, produtoID, preco: str) -> None:
        self.__update__(produtoID, "preco", preco)

    def getProduto(self, produtoID) -> Produto:
        produtoDict = self.__get__(produtoID)
        
        return Produto(produtoDict["nome"], produtoDict["preco"], produtoDict["cor"], produtoID)

    def getNomeProduto(self, produtoID) -> str:
        produtoDict = self.__get__(produtoID)

        return produtoDict["nome"]

    def getPrecoProduto(self, produtoID) -> str:
        produtoDict = self.__get__(produtoID)

        return produtoDict["preco"]

    def getCorProduto(self, produtoID) -> str:
        produtoDict = self.__get__(produtoID)

        return produtoDict["cor"]

    def __update__(self, produtoID: int, keyTable: str, newValue: str) -> None:
        
        if produtoID not in self.tabela.keys():

            raise ValueError("TabelaProdutos -> função update retornou um erro: ID DO PRODUTO NÃO ENCOTNRADO NA TABELA. ID RECEBIDO -> {}".format(produtoID))
        
        self.tabela[produtoID][keyTable] = newValue

    def __get__(self, produtoID) -> dict:

        if produtoID not in self.tabela.keys():

            raise ValueError("TabelaProdutos -> função update retornou um erro: ID DO PRODUTO NÃO ENCOTNRADO NA TABELA. ID RECEBIDO -> {}".format(produtoID))
        
        in_table = self.tabela[produtoID]

        return in_table

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

