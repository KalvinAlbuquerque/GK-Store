from algorithms.tabela import TabelaProdutos, TabelaPrincipal
from common.produto import Produto

tabelaPrincipal = TabelaPrincipal("data/catalogo.json")
tabelaProdutos = tabelaPrincipal.getTabelaProdutos()

produto = Produto("Camisa", "100", "Amarela")
produto2 = Produto("Camisa", "100", "Vermelha")
produto3 = Produto("Camisa", "200", "Preto")

produto = tabelaProdutos.insert(produto)
produto2 = tabelaProdutos.insert(produto2)
produto3 = tabelaProdutos.insert(produto3)

for produtoa in tabelaProdutos.tabela.items():
    print(produtoa)

tabelaProdutos.delete(produto.idProduto)

print("DEPOIS DE DELETAR")
for produtoa in tabelaProdutos.tabela.items():
    print(produtoa)
