from algorithms.arvoreb import BTree
from algorithms.tabela import TabelaPrincipal

arvore = BTree(4)

tabelaProdutos = TabelaPrincipal("data/catalogo.json").getTabelaProdutos()

todosIdsProdutos = tabelaProdutos.getTodosProdutosIds()
todosProdutos = tabelaProdutos.getTodosProdutosObjetoProduto()

arvore.insert_from_list(todosIdsProdutos, todosProdutos)
arvore.Imprime(arvore.root)