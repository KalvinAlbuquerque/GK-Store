from flask import Flask, url_for, render_template, redirect, jsonify, send_file, make_response
import json
import gzip, os

# Modulos locais
from algorithms.tabela import TabelaPrincipal, TabelaCategorias, TabelaProdutos
from common.produto import Produto
from common.catagoria import Categoria
from algorithms.arvoreb import BTree, Registro

global tabelaPrincipal
tabelaPrincipal = TabelaPrincipal("data/catalogo.json")

global ordemArvore
ordemArvore = 6

global arvore
arvore = BTree(ordemArvore) # arvore b de ordem 6

global arvoreCategoria
arvore = BTree(ordemArvore - 3)

class Main():

    app = Flask(__name__)

    def __init__(self) -> None:
        pass

    @app.route('/')
    def index_page():
        return render_template('index.html')

    @app.route('/catalogo.html')
    def redirect_to_catalog():
        # Redireciona para a página catalogo.html
        return redirect(url_for('static', filename='templates/catalogo.html'))
    
    @app.route('/catalogo.json.gz')
    def baixar_catalogo():
        # Redireciona para a página catalogo.html
        return redirect(url_for('static', filename='compressed/catalogo.json.gz'))
    
    @app.route('/editar-catalogo.html')
    def redirect_to_editar_catalogo():
        # Redireciona para a página catalogo.html
        return redirect(url_for('static', filename='templates/editar-catalogo.html'))

    @app.route('/produtos', methods=['GET'])
    def obter_produtos():
        global tabelaPrincipal
        produtos = tabelaPrincipal.getTabelaProdutos().getTodosProdutos()

        return jsonify(produtos)

    @app.route('/categorias', methods=['GET'])
    def obter_categorias():
        global tabelaPrincipal
        categorias = tabelaPrincipal.getTabelaCategorias().getTodasCategorias()

        return jsonify(categorias)

    @app.route('/atualizarTabela')
    def atualizar_tabela():
        global tabelaPrincipal
        global arvore
        global ordemArvore
        global arvoreCategoria

        tabelaPrincipal = TabelaPrincipal("data/catalogo.json")
        
        #
        # carregando os ids dos produtos pra arvore b
        #
        
        # Faz duas listas com os ids dos produtos e os dicionarios dos produtos
        tabelaProdutos = tabelaPrincipal.getTabelaProdutos()
        todosIdsProdutos = tabelaProdutos.getTodosProdutosIds()
        todosProdutos = tabelaProdutos.getTodosProdutos()

        # Faz uma nova arvore
        arvore = BTree(ordemArvore)

        # Insere na arvore b os registros estruturados como: chave (idProduto) elemento (dicionarioDoProduto)
        arvore.insert_from_list(todosIdsProdutos, todosProdutos)

        #
        # carregando todas as categorias pra arvore b
        #

        # Faz duas listas com os nomes das categorias e os dicionarios de cada uma
        tabelaCategorias = tabelaPrincipal.getTabelaCategorias()
        todasCategorias = tabelaCategorias.getTodasCategorias()
        
        todosNomesCategoria = []
        todosProdutosCadaCategoria = []

        for categoria in todasCategorias:
            todosNomesCategoria.append(categoria[0])
            todosProdutosCadaCategoria.append(categoria[1]["produtos"])

        arvoreCategoria = BTree(ordemArvore - 3)
        
        arvoreCategoria.insert_from_list(todosNomesCategoria, todosProdutosCadaCategoria)
        
        mensagem = "Tabela atualizada com sucesso!"
        response = make_response(json.dumps({'message': mensagem}), 200)
        response.headers['Content-Type'] = 'application/json'
        
        return response
    
    @app.route('/produtosOrdemAlfabetica/<produtos>', methods=['GET'])
    def produtos_ordem_alfabetica(produtos):
        global tabelaPrincipal

        produtos = produtos.split(",")

        produtosOrdemAlf = tabelaPrincipal.getTabelaProdutos().getProdutosOrdemAlfabetica(produtos)

        return jsonify(produtosOrdemAlf)
    
    @app.route('/todosIdsProdutos', methods=['GET'])
    def produtos_todos_ids():
        global tabelaPrincipal

        produtosTodosIds = tabelaPrincipal.getTabelaProdutos().getTodosProdutosIds()

        return jsonify(produtosTodosIds)
    
    @app.route('/produtosMenorPreco/<produtos>', methods=['GET'])
    def produtos_menor_preco(produtos):
        global tabelaPrincipal

        produtos = produtos.split(",")

        produtosMenorPreco = tabelaPrincipal.getTabelaProdutos().getProdutosMenorPreco(produtos)

        return jsonify(produtosMenorPreco)

    @app.route('/produtosMaiorPreco/<produtos>', methods=['GET'])
    def produtos_maior_preco(produtos):
        global tabelaPrincipal

        produtos = produtos.split(",")

        produtosMaiorPreco = tabelaPrincipal.getTabelaProdutos().getProdutosMaiorPreco(produtos)

        return jsonify(produtosMaiorPreco)
    
    @app.route('/produtosPorNome/<nome>', methods=['GET'])
    def produtos_por_nome(nome):
        global tabelaPrincipal

        produtosPorNome = tabelaPrincipal.getTabelaProdutos().getProdutosPorNome(nome)

        return jsonify(produtosPorNome)
    
    @app.route('/produtoPorId/<id>', methods=['GET'])
    def produto_por_id(id):
        global tabelaPrincipal

        produtoPorId = tabelaPrincipal.getTabelaProdutos().__get__(id)

        return jsonify(produtoPorId)
    
    @app.route('/updateProduto/<lista>', methods=['GET'])
    def update_produto(lista):

        global tabelaPrincipal

        lista = lista.split(",")

        print("id do produto -> {}".format(lista[0]))

        produtoID = lista[0]

        tabelaPrincipal.getTabelaProdutos().updateNome(produtoID, lista[1])
        tabelaPrincipal.getTabelaProdutos().updatePreco(produtoID, lista[2])
        tabelaPrincipal.getTabelaProdutos().updateCor(produtoID, lista[3])
        tabelaPrincipal.getTabelaProdutos().updateLinkFoto(produtoID, lista[4])

        categoriaPassada = lista[5]
        currCategoria = tabelaPrincipal.getTabelaProdutos().getCategoriaProduto(produtoID)

        print("curr categoria -> {}".format(currCategoria))

        if (currCategoria != categoriaPassada):
            """ Remove o ID do produto da lista de produtos da antiga categoria """
            tabelaPrincipal.getTabelaCategorias().deleteProduto(currCategoria, produtoID)

            """ Caso a nova categoria exista """
            if (tabelaPrincipal.getTabelaCategorias().checarSeCategoriaExiste(categoriaPassada)):
                """ Insere o ID do produto na lista de produtos da nova categoria """
                tabelaPrincipal.getTabelaCategorias().insertProduto(categoriaPassada, produtoID)
            
            else:
                """ Caso a nova categoria não exista """

                """ Cria nova categoria com o nome indicado e insere o id do produto na lista
                de produtos da nova categoria """
                newCategoria = Categoria(categoriaPassada, [produtoID])
                """ Insere a nova categoria na tabela """
                tabelaPrincipal.getTabelaCategorias().insert(newCategoria)

            """ Insere a nova categoria no dicionário do produto """
            tabelaPrincipal.getTabelaProdutos().updateCategoria(produtoID, categoriaPassada)            

            """ Checa se a antiga categoria ficou sem produtos. Se sim, a categoria é excluída da tabela """
            if (len(tabelaPrincipal.getTabelaCategorias().getProdutos(currCategoria)) == 0):
                tabelaPrincipal.getTabelaCategorias().delete(currCategoria)

        tabelaPrincipal.saveJson("data/catalogo.json")

        mensagem = "Produto atualizado com sucesso!"
        response = make_response(json.dumps({'message': mensagem}), 200)
        response.headers['Content-Type'] = 'application/json'

        return response
    
    @app.route('/excluirProduto/<produtoID>', methods=['GET'])
    def excluir_produto(produtoID):
        global tabelaPrincipal

        """ Primeiro, remove o produto da lista de produtos dentro da sua categoria """
        categoria = tabelaPrincipal.getTabelaProdutos().getCategoriaProduto(produtoID)

        tabelaPrincipal.getTabelaCategorias().deleteProduto(categoria, produtoID)
        tabelaPrincipal.getTabelaProdutos().delete(produtoID)

        """ Checa se a antiga categoria ficou sem produtos. Se sim, a categoria é excluída da tabela """
        if (len(tabelaPrincipal.getTabelaCategorias().getProdutos(categoria)) == 0):
            tabelaPrincipal.getTabelaCategorias().delete(categoria)

        tabelaPrincipal.saveJson("data/catalogo.json")

        mensagem = "Produto excluído com sucesso!"
        response = make_response(json.dumps({'message': mensagem}), 200)
        response.headers['Content-Type'] = 'application/json'

        return response
    
    @app.route('/adicionarProduto/<lista>', methods=['GET'])
    def adicionar_produtoo(lista):
        global tabelaPrincipal

        lista = lista.split(",")

        newProduto = Produto(lista[0], lista[1], lista[2], lista[3], lista[4])

        newProduto = tabelaPrincipal.getTabelaProdutos().insert(newProduto)

        if (tabelaPrincipal.getTabelaCategorias().checarSeCategoriaExiste(lista[4])):
            tabelaPrincipal.getTabelaCategorias().insertProduto(lista[4], newProduto.idProduto)
        else:
            newCategoria = Categoria(lista[4], [newProduto.idProduto])
            tabelaPrincipal.getTabelaCategorias().insert(newCategoria)

        tabelaPrincipal.saveJson("data/catalogo.json")

        mensagem = "Produto excluído com sucesso!"
        response = make_response(json.dumps({'message': mensagem}), 200)
        response.headers['Content-Type'] = 'application/json'

        return response

    @app.route('/compactarArquivo/', methods=['GET'])
    def compactar_arquivo():

        if os.path.exists("static/compressed/catalogo.json.gz"):
            os.remove("static/compressed/catalogo.json.gz")

        with gzip.open('static/compressed/catalogo.json.gz', 'wb') as json_file:
            # Escreva os dados compactados no arquivo usando json.dumps com indent=None
            json_string = json.dumps(tabelaPrincipal.tabela, indent=None)
            json_bytes = json_string.encode('utf-8')
            json_file.write(json_bytes)

        mensagem = "Produto excluído com sucesso!"
        response = make_response(json.dumps({'message': mensagem}), 200)
        response.headers['Content-Type'] = 'application/json'

        return response
    
    """ 

        FUNÇÕES ARVORE B 
    
    """
    @app.route('/produtosOrdenadosArvoreB/<produtosID>', methods=['GET'])
    def ordenacao_arvoreb(produtosID):
        global ordemArvore

        arvoreb = BTree(ordemArvore)

        produtosID = produtosID.split(",")

        arvoreb.insert_from_list(produtosID, produtosID)

        produtos = arvoreb.getListaOrdenada()

        return jsonify(produtos)
    
    @app.route('/localizacaoProdutoNaTabela/<idproduto>', methods=['GET'])
    def localizacao_produto_por_id(idproduto):
        global arvore

        registro = Registro()
        registro.Chave = int(idproduto)

        resposta = arvore.search(registro, arvore.root).posicaoNoArquivo
        print(type(resposta))

        return str(resposta)
    
    @app.route('/buscarIntervalosDePreco/<produtos>/<precoMax>/<precoMin>', methods=['GET'])
    def buscatIntervalosPreco(produtos, precoMax, precoMin):
        global ordemArvore

        arvoreb = BTree(ordemArvore)

        produtos = produtos.split(",")

        # Criando uma nova arvore com a chave sendo o preço do produto

        precosLista = []

        for produto in produtos:
            precosLista.append(float(tabelaPrincipal.getTabelaProdutos().getPrecoProduto(produto)))

        # chave -> preço do produto / elemento -> id do produto
        arvoreb.insert_from_list(produtos, precosLista)

        resultado = []

        registroMax = Registro()
        registroMax.Elemento = float(precoMax)
        
        registroMin = Registro()
        registroMin.Elemento = float(precoMin)

        if (float(precoMax) == 99999999):
            resultado = arvoreb.getListaValoresMaioresElemento(registroMin)
        elif (float(precoMin) == 0):
            resultado = arvoreb.getListaValoresMenoresElemento(registroMax)
        else:
            resultado = arvoreb.getListaLimiteMaxMinElemento(registroMax, registroMin)

        print(resultado)

        return jsonify(resultado)

    @app.route('/categoriasProdutos/<categoria>', methods=['GET'])
    def obter_produtos_categoria(categoria):
        global arvoreCategoria

        registro = Registro()
        registro.Chave = arvoreCategoria.converter_para_numerico(categoria)

        result = arvoreCategoria.search(registro, arvoreCategoria.root).Elemento

        return jsonify(result)
    
    @app.route('/produtosOrdenadosArvoreBNome/<produtosID>', methods=['GET'])
    def ordenacao_arvoreb_por_nome(produtosID):
        global ordemArvore
        global tabelaPrincipal

        arvoreb = BTree(ordemArvore)

        produtosID = produtosID.split(",")

        listaProdutosNome = []

        for produto in produtosID:
            listaProdutosNome.append(tabelaPrincipal.getTabelaProdutos().getNomeProduto(produto))

        arvoreb.insert_from_list(listaProdutosNome, produtosID)

        produtos = arvoreb.getListaOrdenada()

        print(produtos)

        return jsonify(produtos)


catalog = Main()

catalog.app.run(debug = True) 