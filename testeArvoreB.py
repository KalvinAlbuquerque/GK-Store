from algorithms.arvoreb import BTree, Registro
from algorithms.tabela import TabelaPrincipal

arvore = BTree(4)

tabelaProdutos = TabelaPrincipal("data/catalogo.json").getTabelaProdutos()

todosIdsProdutos = tabelaProdutos.getTodosProdutosIds()
todosProdutos = tabelaProdutos.getTodosProdutos()

arvore.insert_from_list(todosIdsProdutos, todosProdutos)
# arvore.Imprime(arvore.root)

# arvore.ImprimeEmOrdemDaArvore(arvore.root)

# reg = Registro()
# reg.Chave = 11

# reg2 = Registro()
# reg2.Chave = 2
# print(arvore.search(reg, arvore.root).posicaoNoArquivo)
# a = arvore.getListaLimiteMaxMin(11, 2)



# for elemento in a:
#     print(elemento)
# lista = arvore.getListaOrdenada()

# for elemento in lista:
#     print(elemento)

# arvore.Imprime(arvore.root)

tabelaCategorias = TabelaPrincipal("data/catalogo.json").getTabelaCategorias()
todasCategorias = tabelaCategorias.getTodasCategorias()

todosNomesCategoria = []
todosProdutosCadaCategoria = []

for categoria in todasCategorias:
    todosNomesCategoria.append(categoria[0])
    todosProdutosCadaCategoria.append(categoria[1]["produtos"])

arvoreCategoria = BTree(3)

arvoreCategoria.insert_from_list(todosNomesCategoria, todosProdutosCadaCategoria)

arvoreCategoria.Imprime(arvoreCategoria.root)

categoria ="Esportivo"
registro = Registro()
registro.Chave = arvoreCategoria.converter_para_numerico(categoria)

result = arvoreCategoria.search(registro, arvoreCategoria.root)
print(result.Elemento)