from algorithms.tabela import TabelaProdutos, TabelaPrincipal
from common.produto import Produto

tabelaPrincipal = TabelaPrincipal("data/catalogo.json")
tabelaProdutos = tabelaPrincipal.getTabelaProdutos()

produto = Produto("Camisa", "100", "Amarela")
produto2 = Produto("Camisa", "100", "Vermelha")

produto = tabelaProdutos.insert(produto)
produto2 = tabelaProdutos.insert(produto2)

print(tabelaProdutos.tabela)

tabelaProdutos.delete(produto.idProduto)

print(tabelaProdutos.tabela)