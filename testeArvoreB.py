from algorithms.arvoreb import BTree, Registro
from algorithms.tabela import TabelaPrincipal

arvore = BTree(4)

tabelaProdutos = TabelaPrincipal("data/catalogo.json").getTabelaProdutos()

todosIdsProdutos = tabelaProdutos.getTodosProdutosIds()
todosProdutos = tabelaProdutos.getTodosProdutos()

arvore.insert_from_list(todosIdsProdutos, todosProdutos)

# arvore.ImprimeEmOrdemDaArvore(arvore.root)

reg = Registro()
reg.Chave = 11

reg2 = Registro()
reg2.Chave = 2
# print(arvore.search(reg, arvore.root).posicaoNoArquivo)
a = arvore.getListaLimiteMaxMin(11, 2)



for elemento in a:
    print(elemento)
# lista = arvore.getListaOrdenada()

# for elemento in lista:
#     print(elemento)

# arvore.Imprime(arvore.root)