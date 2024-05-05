from common.produto import Produto
from common.catagoria import Categoria
import json
from unidecode import unidecode

class TabelaProdutos():

    def __init__(self, tabela: dict) -> None:
        self.tabela = tabela

    def insert(self, value: Produto) -> Produto:

        novo_produto = {
            "nome" : value.nome,
            "preco" : value.preco,
            "cor" : value.cor,
            "linkFoto" : value.linkFoto,
            "categoria" : value.categoria
        }

        novo_id = 0

        if (len(self.tabela) > 0):

            novo_id = int(list(self.tabela.keys())[-1]) + 1

        self.tabela[novo_id] = novo_produto

        return Produto(nome=value.nome, preco=value.preco, cor=value.cor, linkFoto= value.linkFoto, categoria=value.categoria, idProduto=str(novo_id))

    def delete(self, produtoID) -> None:
        
        if produtoID not in self.tabela.keys():

            raise ValueError("TabelaProdutos -> função delete retornou um erro: ID DO PRODUTO NÃO ENCOTNRADO NA TABELA. ID RECEBIDO -> {}".format(produtoID))
        
        del self.tabela[produtoID]

    def updateCor(self, produtoID: int, cor: str) -> None:
        self.__update__(produtoID, "cor", cor)

    def updateNome(self, produtoID, nome: str) -> None:
        self.__update__(produtoID, "nome", nome)

    def updatePreco(self, produtoID, preco: str) -> None:
        self.__update__(produtoID, "preco", preco)

    def updateLinkFoto(self, produtoID, linkFoto: str) -> None:
        self.__update__(produtoID, "linkFoto", linkFoto)
    
    def updateCategoria(self, produtoID, categoria: str) -> None:
        self.__update__(produtoID, "categoria", categoria)

    def getProduto(self, produtoID) -> Produto:
        produtoDict = self.__get__(produtoID)
        
        return Produto(nome=produtoDict["nome"], preco=produtoDict["preco"], cor=produtoDict["cor"], idProduto=produtoID, linkFoto=produtoDict["linkFoto"], categoria=produtoDict["categoria"])

    def getNomeProduto(self, produtoID) -> str:
        produtoDict = self.__get__(produtoID)

        return produtoDict["nome"]
    
    def getCategoriaProduto(self, produtoID) -> str:

        produtoDict = self.__get__(produtoID)

        return produtoDict["categoria"]
    
    def getProdutosPorNome(self, nome) -> list:

        produtosID = []

        nome = unidecode(nome)

        for produtoID in self.tabela.keys():

            produto = self.tabela[produtoID]

            if nome.lower() in unidecode(produto["nome"].lower()):
                produtosID.append(produtoID)
        
        return produtosID

    def getPrecoProduto(self, produtoID) -> str:
        produtoDict = self.__get__(produtoID)

        return produtoDict["preco"]

    def getCorProduto(self, produtoID) -> str:
        produtoDict = self.__get__(produtoID)

        return produtoDict["cor"]
    
    def getTodosProdutos(self) -> list:

        result = []

        for produto in self.tabela.items():
            result.append(produto)

        return result
    
    def getTodosProdutosIds(self) -> list:

        result = []

        for produtoID in self.tabela.keys():

            result.append(produtoID)

        return result
    
    def getProdutosOrdemAlfabetica(self, produtos):

        produtosObj = []

        for produto in produtos:
            produtosObj.append(self.getProduto(produto))
        
        produtosOrdenados = sorted(produtosObj, key=lambda produto: unidecode(produto.nome))

        produtosIDs = []

        for produtoObj in produtosOrdenados:
            produtosIDs.append(produtoObj.idProduto)

        return produtosIDs
    
    def getProdutosMenorPreco(self, produtos):
        
        produtosObj = []

        for produto in produtos:
            produtosObj.append(self.getProduto(produto))
        
        produtosOrdenados = sorted(produtosObj, key=lambda produto: float(produto.preco))

        produtosIDs = []

        for produtoObj in produtosOrdenados:
            produtosIDs.append(produtoObj.idProduto)

        return produtosIDs
    
    def getProdutosMaiorPreco(self, produtos):
        
        produtosObj = []

        for produto in produtos:
            produtosObj.append(self.getProduto(produto))
        
        produtosOrdenados = sorted(produtosObj, key=lambda produto: float(produto.preco), reverse = True)

        produtosIDs = []

        for produtoObj in produtosOrdenados:
            produtosIDs.append(produtoObj.idProduto)

        return produtosIDs

    def __update__(self, produtoID: int, keyTable: str, newValue: str) -> None:
        
        if produtoID not in self.tabela.keys():

            raise ValueError("TabelaProdutos -> função update retornou um erro: ID DO PRODUTO NÃO ENCOTNRADO NA TABELA. ID RECEBIDO -> {}".format(produtoID))
        
        self.tabela[produtoID][keyTable] = newValue

    def __get__(self, produtoID) -> dict:

        if produtoID not in self.tabela.keys():

            raise ValueError("TabelaProdutos -> função get retornou um erro: ID DO PRODUTO NÃO ENCOTNRADO NA TABELA. ID RECEBIDO -> {}".format(produtoID))
        
        in_table = self.tabela[produtoID]

        return in_table

class TabelaCategorias():

    def __init__(self, tabela: dict) -> None:
        self.tabela = tabela

    def insert(self, value: Categoria) -> None:

        nova_categoria = {
            "produtos" : value.produtos
        }

        self.tabela[value.nome] = nova_categoria

    def checarSeCategoriaExiste(self, value : str) -> bool:

        result = False

        if (value in self.tabela.keys()):
            result = True

        return result
    
    def insertProduto(self, categoriaNome: str, produtoID: int) -> None:
        
        if categoriaNome in self.tabela:
            produtos = self.tabela[categoriaNome]["produtos"]

            if produtoID not in produtos:
                produtos.append(produtoID)
            else:
                raise ValueError("TabelaCategorias -> função insertProduto retornou um erro: Produto já cadastrado na categoria.")
        
        else:
            raise ValueError("TabelaCategorias -> função insertProduto retornou um erro: Categoria não existe na tabela.")

    def deleteProduto(self, nomeCategoria: str, idProduto: int) -> None:
        if nomeCategoria not in self.tabela.keys():

            raise ValueError("TabelaCategorias -> função deleteProduto retornou um erro: CATEGORIA NÃO ENCOTNRADA NA TABELA. NOME RECEBIDO -> {}".format(nomeCategoria))

        produtos = self.tabela[nomeCategoria]["produtos"]

        print("produtos na categoria -> {}".format(produtos))

        produtos.remove(idProduto)

    def delete(self, categorianome: int) -> None:
        if categorianome not in self.tabela.keys():

            raise ValueError("TabelaCategorias -> função delete retornou um erro: CATEGORIA NÃO ENCOTNRADA NA TABELA. NOME RECEBIDO -> {}".format(categorianome))
        
        self.tabela.pop(categorianome)

    def updateNome(self, nomeCategoria: str, novoNomeCategoria: str) -> None:

        print("nome categoria -> {}".format(nomeCategoria))

        if nomeCategoria not in self.tabela.keys():

            raise ValueError("TabelaCategorias -> função updateNome retornou um erro: CATEGORIA NÃO ENCOTNRADA NA TABELA. NOME RECEBIDO -> {}".format(nomeCategoria))
        
        chaveAntiga = self.tabela[nomeCategoria]

        self.tabela[novoNomeCategoria] = chaveAntiga

        self.delete(nomeCategoria)
    
    def getProdutos(self, nomeCategoria: str) -> list:

        if nomeCategoria not in self.tabela.keys():

            raise ValueError("TabelaCategorias -> função updateNome retornou um erro: CATEGORIA NÃO ENCOTNRADA NA TABELA. NOME RECEBIDO -> {}".format(nomeCategoria))

        return self.tabela[nomeCategoria]["produtos"]
    
    def getTodasCategorias(self) -> list:

        categorias = []

        for categoria in self.tabela.items():
            categorias.append(categoria)

        return categorias



class TabelaPrincipal():

    def __init__(self, jsonPath) -> None:
        self.tabela = self.loadJson(jsonPath)
        self.produtos = TabelaProdutos(self.tabela["catalogo"]["produtos"])
        self.categorias = TabelaCategorias(self.tabela["catalogo"]["categorias"])

    def getTabelaProdutos(self) -> TabelaProdutos:
        
        return self.produtos
    
    def getTabelaCategorias(self) -> TabelaCategorias:
        
        return self.categorias

    def loadJson(self, jsonPath) -> dict:

        with open(jsonPath, "r") as file:
            tabela = json.load(file)

        return tabela
    
    def saveJson(self, jsonPath) -> None:
        with open(jsonPath, "w") as file:
            json.dump(self.tabela, file, indent=4)

