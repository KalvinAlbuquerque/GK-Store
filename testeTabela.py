from algorithms.tabela import TabelaProdutos, TabelaPrincipal
from common.produto import Produto

def printar_tabela_produtos():
    for produtoa in tabelaProdutos.tabela.items():
        print(produtoa)
        print()

tabelaPrincipal = TabelaPrincipal("data/catalogo.json")
tabelaProdutos = tabelaPrincipal.getTabelaProdutos()

""" 
    Teste inserir produto
"""
produto = Produto("Camisa 1", "100", "Amarela")
produto2 = Produto("Camisa 2", "100", "Vermelha")
produto3 = Produto("Camisa 3", "200", "Preto")

produto = tabelaProdutos.insert(produto)
produto2 = tabelaProdutos.insert(produto2)
produto3 = tabelaProdutos.insert(produto3)

printar_tabela_produtos()

""" 
    Teste deletar produto
"""

# tabelaProdutos.delete(produto.idProduto)

# print("DEPOIS DE DELETAR")
# for produtoa in tabelaProdutos.tabela.items():
#     print(produtoa)

""" 
    Teste editar produto
"""

# tabelaProdutos.updateNome(produto.idProduto, "Calça")
# tabelaProdutos.updatePreco(produto.idProduto, "150")

# print("DEPOIS DO UPDATE")
# printar_tabela_produtos()

""" 
    Teste get no produto
"""

# produtoget = tabelaProdutos.getProduto(1)

# produtoget.printProduto()

# print("PRINTANDO ATRIBUTOS INDIVIDUALMENTE")
# print(f"nome -> {tabelaProdutos.getNomeProduto(produtoget.idProduto)}")
# print(f"cor -> {tabelaProdutos.getCorProduto(produtoget.idProduto)}")
# print(f"preco -> {tabelaProdutos.getPrecoProduto(produtoget.idProduto)}")
