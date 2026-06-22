# Arquivo: interface.py

def gerar_html(entrada, saida, lucro, estoque):
    # Criamos uma variável de texto gigante contendo o HTML/CSS do site
    # Colocamos as variáveis do Python dentro do HTML usando as chaves {}
    
    html_livros = ""
    # Esse laço cria um bloco de código HTML para cada livro da nossa lista
    for livro in estoque:
        html_livros += f"""
        <div class="livro-card">
            <h4>{livro['titulo']}</h4>
            <p>Qtd: {livro['qtd']} unidades</p>
        </div>
        """

    conteudo_site = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Painel Fidelivros</title>
    <style>
        body {{ font-family: Arial, sans-serif; background-color: #f4f6f9; padding: 20px; }}
        header {{ background-color: #2c3e50; color: white; padding: 20px; text-align: center; border-radius: 8px; }}
        .financeiro-container {{ display: flex; gap: 20px; margin: 20px 0; }}
        .card {{ flex: 1; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }}
        .entrada {{ color: #27ae60; font-weight: bold; font-size: 24px; }}
        .saida {{ color: #c0392b; font-weight: bold; font-size: 24px; }}
        .vendas {{ color: #2980b9; font-weight: bold; font-size: 24px; }}
        .livros-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; }}
        .livro-card {{ background: white; padding: 15px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; border-top: 4px solid #2c3e50; }}
    </style>
</head>
<body>
    <header>
        <h1>Painel de Controle Interno</h1>
        <p>Fidelivros Distribuidora</p>
    </header>

    <h2>Resumo do Dia</h2>
    <div class="financeiro-container">
        <div class="card"><h3>Entradas</h3><p class="entrada">R$ {entrada:.2f}</p></div>
        <div class="card"><h3>Saídas</h3><p class="saida">R$ {saida:.2f}</p></div>
        <div class="card"><h3>Vendido Hoje</h3><p class="vendas">R$ {lucro:.2f}</p></div>
    </div>

    <h2>Livros em Estoque</h2>
    <div class="livros-grid">
        {html_livros}
    </div>
</body>
</html>"""
    
    return conteudo_site