from algorithms.tabela import TabelaProdutos, TabelaPrincipal
from common.produto import Produto
from common.catagoria import Categoria

def printar_tabela_produtos():
    for produtoa in tabelaProdutos.tabela.items():
        print(produtoa)
        print()

tabelaPrincipal = TabelaPrincipal("data/catalogo.json")
tabelaProdutos = tabelaPrincipal.getTabelaProdutos()
tabelaCategorias = tabelaPrincipal.getTabelaCategorias()

""" 

    TESTE TABELA PRODUTOS

"""

# """ 
#     Teste inserir produto
# """
# produto = Produto("Camisa 1", "100", "Amarela")
# produto2 = Produto("Camisa 2", "100", "Vermelha")
produto3 = Produto(nome="Camisa 3", preco="200", cor="Preto", linkFoto="1.png", categoria="Teste")

# produto = tabelaProdutos.insert(produto)
# produto2 = tabelaProdutos.insert(produto2)
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

""" 
    Teste salvar alterações na tabela
"""
# tabelaPrincipal.saveJson("data/catalogo.json")

""" 

    Teste printar produtos em ordem alfabetica

"""

# produtosReordenados = tabelaProdutos.getProdutosOrdemAlfabetica(["1", "2", "0"])

# print(produtosReordenados)

""" 

    Pegar lista de IDs de produtos que contenha no nome certa ordem de caracteres

"""

# produtosIds = tabelaProdutos.getProdutosPorNome("sneaker")

# print(produtosIds)

# Excluir a chave específica ('4' no seu exemplo)
# tabelaProdutos.delete("4")

# print(tabelaProdutos.tabela)



""" 

    TESTE TABELA CATEGORIAS

"""

""" 
    Inserir categoria
"""
# novaCategoria = Categoria("Esportivo", [produto.idProduto, produto2.idProduto, produto3.idProduto])

# tabelaCategorias.insert(novaCategoria)

# for categoria in tabelaCategorias.tabela.items():
#     print(categoria)

""" 
    Deletar produto na categoria
"""
# tabelaCategorias.deleteProduto(novaCategoria.nome, produto.idProduto)

# print("DEPOIS DE DELETAR")
# for categoria in tabelaCategorias.tabela.items():
#     print(categoria)

""" 
    Inserir produto na categoria
"""
# tabelaCategorias.insertProduto(novaCategoria.nome, produto.idProduto)

# print("DEPOIS DE ADICIONAR NOVO PRODUTO")
# for categoria in tabelaCategorias.tabela.items():
#     print(categoria)

""" 
    Mudar o nome da categoria
"""
# tabelaCategorias.updateNome(novaCategoria.nome, "Sport")

# print("DEPOIS DE ATUALIZAR O NOME")
# for categoria in tabelaCategorias.tabela.items():
#     print(categoria)

""" 
    Get produtos categoria
"""

# nomeCategoria = "Sport"
# produtos = tabelaCategorias.getProdutos(nomeCategoria)

# print("PRODUTOS DA CATEGORIA")

# for produtoa in produtos:

#     print(produtoa)


""" 
    Get todas as categorias
"""

# nomeCategoria = "Sport"
all_categorias = tabelaCategorias.getTodasCategorias()

for categoria in all_categorias:

    print(categoria[1]['produtos'])