/* 
    IDs dos produtos atuais
*/
var produtosID = [];

/*
    Categorias selecionadas
*/
var categoriasMarcadas = [];

/* 
    Radios selecionados
*/
var radioSelecionado = "option1";

/* 
    Pesquisar
*/
var pesquisarH = "";

/*
    Limpando a barra de pesquisa
*/
const inputElement = document.querySelector('.search-input');
inputElement.value = "";

/* 
    Checando se está em modo de edição
*/
var editionMode = false;

var currentPath = window.location.pathname;
if (currentPath.includes("editar-catalogo.html"))
{
    console.log("Edition mode enabled.");
    editionMode = true;
}

async function gerenciar_categorias()
{
    var catalogocontainer = document.getElementById("bg-catalogo");
    catalogocontainer.innerHTML = "";

    var novaDiv = document.createElement('div');
    novaDiv.classList.add('editar-categorias');    

    // var response = await fetch('/categorias');
    // var categor = await response.json();

    // const response = await fetch('/categorias');
    // const categorias = await response.json();

    novaDiv.innerHTML = `
    <button class="btn-salvar-produto" id="btn-editar-categoria">EDITAR CATEGORIA</button>
    <button class="btn-salvar-produto" id="btn-criar-categoria">CRIAR CATEGORIA</button>
    `

    catalogocontainer.appendChild(novaDiv);
}

async function fazerDownloadArquivo()
{
    await fetch('/compactarArquivo/');

    const nomeArquivo = '/catalogo.json.gz'; // Caminho relativo ao servidor web

    const linkDownload = document.createElement('a');
    linkDownload.href = nomeArquivo;
    linkDownload.download = 'catalogo.json.gz'; // Nome do arquivo a ser baixado

    linkDownload.style.display = 'none';
    document.body.appendChild(linkDownload);

    linkDownload.click();

    document.body.removeChild(linkDownload);
}

/* 
    Função pra dar update do produto na tabela
*/
async function updateProduto(produtoID)
{
    let produtoAttr = []

    let nome = document.getElementById("product-input");
    let preco = document.getElementById("product-input2");
    let cor = document.getElementById("product-input3");
    let linkFoto = document.getElementById("product-input4");
    let categoria = document.getElementById("product-input5");

    produtoAttr.push(produtoID);
    produtoAttr.push(nome.value);
    produtoAttr.push(preco.value);
    produtoAttr.push(cor.value);
    produtoAttr.push(linkFoto.value);
    produtoAttr.push(categoria.value)

    await fetch(`/updateProduto/${produtoAttr}`);

    window.location.reload();
}

async function add_produto()
{
    console.log("clicked 2")

    let inputName = document.getElementById("product-input").value;
    let inputName2 = document.getElementById("product-input2").value;
    let inputName3 = document.getElementById("product-input3").value;
    let inputName4 = document.getElementById("product-input4").value;
    let inputName5 = document.getElementById("product-input5").value;

    let produtoAttrbut = []

    produtoAttrbut.push(inputName);
    produtoAttrbut.push(inputName2);
    produtoAttrbut.push(inputName3);
    produtoAttrbut.push(inputName4);
    produtoAttrbut.push(inputName5);

    let repsostaAddProduto = await fetch(`/adicionarProduto/${produtoAttrbut}`);

    window.location.reload();
}

async function adicionar_produto()
{
    var catalogocontainer = document.getElementById("bg-catalogo");
    catalogocontainer.innerHTML = "";

    var novaDiv = document.createElement('div');
    novaDiv.classList.add('adicionar-produto');

    console.log("aqui!!!!!")

    novaDiv.innerHTML = `
    <p class=title-above>Nome:</p>
    <input type="text" class="product-input" id="product-input" placeholder="Nome do produto">
    <p class=title-above>Preco:</p>
    <input type="text" class="product-input" id="product-input2" placeholder="Preco do produto">
    <p class=title-above>Cor:</p>
    <input type="text" class="product-input" id="product-input3" placeholder="Cor do produto">
    <p class=title-above>Link imagem:</p>
    <input type="text" class="product-input" id="product-input4" placeholder="Link do produto">
    <p class=title-above>Categoria</p>
    <input type="text" class="product-input" id="product-input5" placeholder="Categoria do produto">
    <button class="btn-salvar-produto" id="btn-salvar-produto2">SALVAR</button>
    `

    catalogocontainer.appendChild(novaDiv)

    let button_salvar2 = document.getElementById("btn-salvar-produto2");

    button_salvar2.addEventListener('click', () => {
        console.log("clicked")
        add_produto();
    });
}

/* 
    Função pra excluir produto na tabela
*/
async function excluirProduto(produtoID)
{
    let responseExcluir = await fetch(`/excluirProduto/${produtoID}`);

    window.location.reload();
}

/* 
    Função pra redirecionar a página para catalogo.html
*/
function redirectCatalog() 
{
    window.location.href = 'catalogo.html'
}

function redirectPaginaInicial()
{
    window.location.href = 'index.html'
}

/* 
    Função pra redirecionar a página para editar-catalogo.html
*/
function redirectEditCatalog() 
{
    window.location.href = 'editar-catalogo.html'
}

async function editarProduto(produtoID)
{
    var catalogocontainer = document.getElementById("bg-catalogo");
    catalogocontainer.innerHTML = "";

    var novaDiv = document.createElement('div');
    novaDiv.classList.add('editar-produto');

    var novaDiv2 = document.createElement('div');
    novaDiv2.classList.add("produto-antigo");

    var novaDiv3 = document.createElement('div');
    novaDiv3.classList.add("produto-novo");

    
    var responseProdutoUnico = await fetch(`/produtoPorId/${produtoID}`);
    var resposta = await responseProdutoUnico.json();
    
    let imagemProduto = resposta.linkFoto ? `/static/img/produtos/${resposta.linkFoto}` : `/static/img/produtos/0.jpg`
    
    novaDiv3.innerHTML = `
        <p class=title-above>Nome:</p>
        <input type="text" class="product-input" id="product-input" placeholder="${resposta.nome}">
        <p class=title-above>Preco:</p>
        <input type="text" class="product-input" id="product-input2" placeholder="${resposta.preco}">
        <p class=title-above>Cor:</p>
        <input type="text" class="product-input" id="product-input3" placeholder="${resposta.cor}">
        <p class=title-above>Link imagem:</p>
        <input type="text" class="product-input" id="product-input4" placeholder="${resposta.linkFoto}">
        <p class=title-above>Categoria:</p>
        <input type="text" class="product-input" id="product-input5" placeholder="${resposta.categoria}">
        <button class="btn-salvar-produto" id="btn-salvar-produto">SALVAR</button>
        <button class="btn-salvar-produto" id="btn-excluir-produto">EXCLUIR</button>
    `

    novaDiv2.innerHTML = `
    <img src="${imagemProduto}" class="pic-produto">
    <p class="title-produto" id="title-produto">${resposta.nome}</p>
    <p class="preco-produto" id="preco-produto">R$ ${resposta.preco}</p>
    <p class="cor-produto" id="cor-produto">${resposta.cor}</p>
    `;

    
    novaDiv.appendChild(novaDiv2);
    novaDiv.appendChild(novaDiv3)
    catalogocontainer.appendChild(novaDiv);

    let inputName = document.getElementById("product-input");
    inputName.value = resposta.nome;

    let inputName2 = document.getElementById("product-input2");
    inputName2.value = resposta.preco;

    let inputName3 = document.getElementById("product-input3");
    inputName3.value = resposta.cor;

    let inputName4 = document.getElementById("product-input4");
    inputName4.value = resposta.linkFoto;

    let inputName5 = document.getElementById("product-input5");
    inputName5.value = resposta.categoria;

    let button_salvar = document.getElementById("btn-salvar-produto");
    let button_excluir = document.getElementById("btn-excluir-produto");

    button_salvar.addEventListener('click', () => {
        console.log(`clicado pra editar o produto ${produtoID}`)
        updateProduto(produtoID);
    });


    button_excluir.addEventListener('click', () => {
        excluirProduto(produtoID);
    });
}

async function pesquisar() 
{
    const inputElement = document.querySelector('.search-input');

    const textoDigitado = inputElement.value;

    pesquisarH = textoDigitado;

    /* 
        Reseta as opções de ordenar de volta para o padrão
    */
    const option1 = document.getElementById('option1');
    option1.checked = true;
    radioSelecionado = "option1";

    limparDivProdutos();
    carregarProdutos();
}

/* 
    Função pra atualizar a tabela de acordo com o conteúdo do arquivo json.

    Essa função irá chamar o método /atualizarTabela do main.py, que cria uma nova instância
    da tabela com o caminho do arquivo json. Dessa forma, o conteúdo do módulo Tabela é lido
    novamente.
*/
async function atualizarTabela() 
{
    try 
    {   
        const response = await fetch('/atualizarTabela');
        
        if (response.ok) 
        {
            console.log('Tabela atualizada com sucesso!');
        } 
        else 
        {
            console.error('Erro ao atualizar tabela:', response.statusText);
        }
    } 
    catch (error) 
    {
        console.error('Erro ao fazer requisição para atualizar tabela:', error);
    }
}

/* 
    Função pra limpar a div que ficam os produtos
*/
async function limparDivProdutos()
{
    console.log("limpando div")
    const catalogoContainer = document.getElementById('catalogo-container');
    catalogoContainer.innerHTML = '';
}

/* 
    Função para obter um array com os ids dos produtos de uma categoria
*/
async function obterProdutosPorCategoria(categoria) 
{
    try 
    {
        const response = await fetch(`/categoriasProdutos/${categoria}`)
        const produtos = await response.json();

        return produtos
    } 
    catch (error) 
    {
        console.error('Erro ao obter produtos por categoria:', error);
    }
}

/* 
    Função pra carregar os produtos da tabela para a div de produtos
*/
async function carregarProdutos() 
{
    try 
    {
        console.log("carregando produtos");
        /* 
            Acessa todos os produtos
        */
        const response = await fetch('/produtos');
        var produtos = await response.json();
        
        /* 
            Checa os checkbox das categorias
        */
        if (categoriasMarcadas.length > 0) 
        {
            produtosID = [];

            for (const categoria of categoriasMarcadas) 
            {
                const produtosCategoria = await obterProdutosPorCategoria(categoria);

                produtosID = produtosID.concat(produtosCategoria);
            }
        }
        else
        {
            const responseProdutosID = await fetch('/todosIdsProdutos');
            var listProdutosID = await responseProdutosID.json();
            produtosID = listProdutosID;
        }
        
        if (pesquisarH.length > 0)
        {
            var responsePesquisar = await fetch(`/produtosPorNome/${pesquisarH}`);
            var produtosIDPesquisa = await responsePesquisar.json();

            if (categoriasMarcadas.length > 0)
            {
                produtosIDCatetorias = produtosID
                produtosID = []

                produtosIDPesquisa.forEach(idProduto => {
                    if (produtosIDCatetorias.includes(idProduto))
                    {
                        produtosID.push(idProduto);
                    }
                });
            }       
            else
            {
                produtosID = produtosIDPesquisa
            }
        }

        /* 
            Checa os radios de ordenação
        */
        if (radioSelecionado != "option1")
        {
            if (radioSelecionado == "option2")
            {
                var responseOrdemAlf = await fetch(`/produtosOrdemAlfabetica/${produtosID}`);
                produtosID = await responseOrdemAlf.json();
            }
            else if (radioSelecionado == "option3")
            {
                var responseMenorPreco = await fetch(`/produtosMenorPreco/${produtosID}`);
                produtosID = await responseMenorPreco.json();
            }
            else if (radioSelecionado == "option4")
            {
                var responseMaiorPreco = await fetch(`/produtosMaiorPreco/${produtosID}`);
                produtosID = await responseMaiorPreco.json();
            }
        }

        const catalogoContainer = document.getElementById('catalogo-container');
        

        // console.log(produtosID)
        /* 

        */
        for (let i = 0; i < produtosID.length; i++)
        {
            let produtoID = produtosID[i]
            const divProduto = document.createElement('div');
            divProduto.classList.add('produto-catalogo');
            var objetoProduto = produtos[produtoID][1];
            let imagemProduto = objetoProduto.linkFoto ? `/static/img/produtos/${objetoProduto.linkFoto}` : `/static/img/produtos/0.jpg`
    
            divProduto.innerHTML = `
                <img src="${imagemProduto}" class="pic-produto">
                <p class="title-produto" id="title-produto">${objetoProduto.nome}</p>
                <p class="preco-produto" id="preco-produto">R$ ${objetoProduto.preco}</p>
                <p class="cor-produto" id="cor-produto">${objetoProduto.cor}</p>
            `;
                
            divProduto.addEventListener('click', () => {
                editarProduto(produtoID);
            });
                // if (editionMode == true) 
                // {
                // const checkboxElement = document.createElement('input');
                // checkboxElement.type = 'checkbox';
                // checkboxElement.classList.add('edit-checkbox');
                // checkboxElement.name = String(produtoID);
        
                // checkboxElement.addEventListener('change', (event) => 
                // {
                //     const isChecked = event.target.checked;
                //     console.log(`Checkbox estado alterado: ${isChecked}`);
                // });

                // divProduto.insertBefore(checkboxElement, divProduto.firstChild);
                // }
    
            catalogoContainer.appendChild(divProduto);
        }
        
        const divEspacoFinal = document.createElement('div');
        divEspacoFinal.classList.add("div-branco");
        catalogoContainer.appendChild(divEspacoFinal);
    } 
    catch (error) 
    {
        console.error('Erro ao carregar os produtos:', error);
    }
}

/* 
    Função pra carregar as categorias da tabela para a div de categorias
*/
async function carregarCategorias() 
{
    try 
    {
        const response = await fetch('/categorias');
        const categorias = await response.json();

        const categoriasContainer = document.getElementById('categorias');

        var counter = 0;
        
        /* 
            Carrega as categorias para o bloco de categorias
        */
        categorias.forEach(
            categoria => 
            {
                const divCategoria = document.createElement('div');
                divCategoria.classList.add('checkbox-container');

                let nomeCategoria = categoria[0]

                divCategoria.innerHTML = `
                    <input type="checkbox" id="checkbox${counter}" name="${nomeCategoria}">
                    <label for="${nomeCategoria}" class="checkbox-label">${nomeCategoria}</label>
                `;

                categoriasContainer.appendChild(divCategoria);

                counter++;
            }
        );
        
        /*
            Adiciona um event listener pra ficar esperando que um dos checkbox de categorias
            sejam acionados.
        */
        const checkboxes = document.querySelectorAll('.checkbox-container input[type="checkbox"]');

        var checkBoxChecked = [];

        checkboxes.forEach(
            checkbox => 
            {
                checkbox.addEventListener('change', () => 
                {
                    if (checkbox.checked) 
                    {
                        checkBoxChecked.push(checkbox.name);
                    } 
                    else 
                    {
                        checkBoxChecked = checkBoxChecked.filter(item => item !== checkbox.name);
                    }
                    
                    if (inputElement.value.length == 0)
                    {
                        /* 
                            Limpa todos os protudos da div
                        */
                        limparDivProdutos();

                        /* 
                            Checa se há checkbox marcadas, se sim, carrega os produtos da checkbox. Se não, carrega todos os produtos.
                        */
                        carregarProdutos();  
                    }
                    
                    /* 
                        Reseta as opções de ordenar de volta para o padrão
                    */
                    const option1 = document.getElementById('option1');
                    option1.checked = true;
                    radioSelecionado = "option1";

                    /* 
                        Atualizando o array de categorias selecionadas
                    */
                    categoriasMarcadas = checkBoxChecked;
                });

            }
        );
    } 
    catch (error) 
    {
        console.error('Erro ao carregar os produtos:', error);
    }
}

/* 
    Exibir produtos em ordem alfabética
*/

function adicionarListenerRadiosOrdenacao()
{
    document.addEventListener('DOMContentLoaded', () => 
    {
        /* 
            Inicia as opções de ordenar com o Padrão marcado
        */
        const option1 = document.getElementById('option1');
    
        option1.checked = true;

        radioSelecionado = "option1";

        const radioButtons = document.querySelectorAll('input[type="radio"]');
        
        radioButtons.forEach(radioButton => 
        {
            radioButton.addEventListener('change', () => 
            {
                if (radioButton.checked) 
                {
                    const groupName = radioButton.getAttribute('name');
                    const otherRadioButtons = document.querySelectorAll(`input[name="${groupName}"]`);
                    
                    otherRadioButtons.forEach(otherRadioButton => 
                    {
                        if (otherRadioButton !== radioButton) 
                        {
                            otherRadioButton.checked = false;
                        }
                    });

                    const optionValue = radioButton.id;

                    switch (optionValue)
                    {
                        case 'option1':
                            radioSelecionado = "option1";
                            break;
                        case 'option2':
                            radioSelecionado = "option2";
                            break;
                        case 'option3':
                            radioSelecionado = "option3";
                            break;
                        case 'option4':
                            radioSelecionado = "option4";
                            break;
                    }

                    limparDivProdutos();
                    carregarProdutos();
                }
            });
        });
    });
}


/* 
    Atualiza a tabela (caso novos dados sejam adicionados durante a execução do programa)
*/
atualizarTabela();

/* 
    Carrega todas as categorias e exibe na tela
*/
carregarCategorias();

/* 
    Carrega todos os produtos e exibe na tela (o null é pra indicar que não existe uma
    categoria específica pra exibição, simplesmente vai exibr todos os produtos)
*/
carregarProdutos();

/* 

*/
adicionarListenerRadiosOrdenacao();

/* 
    Listener do input de pesquisa
*/
inputElement.addEventListener('input', function(event) 
{
    const textoDigitado = event.target.value; 
    if (textoDigitado.length == 0)
    {
        pesquisarH = "";
    }
});

// Selecione a imagem pela classe 'shoes-pic'
const imagem = document.querySelector('.shoes-pic');

// Adicione um event listener para o clique na imagem
imagem.addEventListener('click', function() {
    // Redirecione para a página index.html
    window.location.href = '/';
});
