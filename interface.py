# Arquivo: interface.py

def gerar_html():
    """
    Gera a interface principal baseada no layout moderno de portfólio.
    Contém barra de navegação superior fixa com logo clicável e seção de destaque centralizada.
    """
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fidelivros - Home</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700;900&display=swap');

        /* Reset total de margens e preenchimentos para controle absoluto do layout */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Montserrat', sans-serif;
        }}

        body, html {{
            height: 100%;
            background-color: #ffffff;
            color: #333333;
        }}

        /* --- BARRA DE NAVEGAÇÃO SUPERIOR (NAVBAR) --- */
        .navbar {{
            position: fixed; /* Fixa a barra no topo da tela mesmo se houver rolagem */
            top: 0;
            left: 0;
            width: 100%;
            height: 70px;
            background-color: #2A2A2A; /* Cinza escuro premium baseado na referência */
            display: flex;
            justify-content: space-between; /* Separa a logo dos links de navegação */
            align-items: center;
            padding: 0 40px;
            z-index: 1000; /* Garante que a barra fique sempre por cima de qualquer elemento */
            border-bottom: 2px solid #D6001C; /* Linha sutil vermelha para identidade da marca */
        }}

        /* Link invisível em volta da logo para torná-la clicável */
        .logo-link {{
            display: flex;
            align-items: center;
            text-decoration: none;
            height: 100%;
        }}

        /* Mini logo ajustada para caber perfeitamente na barra superior */
        .logo-nav {{
            height: 45px;
            width: auto;
            transition: transform 0.2s ease;
        }}

        .logo-link:hover .logo-nav {{
            transform: scale(1.05); /* Leve efeito de crescimento ao passar o mouse */
        }}

        /* Menu de links centrais na barra */
        .nav-links {{
            display: flex;
            gap: 30px;
            list-style: none;
        }}

        .nav-links a {{
            color: #FFFFFF;
            text-decoration: none;
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: color 0.3s ease;
        }}

        .nav-links a:hover {{
            color: #D6001C; /* Links mudam para vermelho Fidelivros no hover */
        }}

        /* Botão destacado no canto direito da Navbar (Área Restrita) */
        .btn-area-restrita {{
            background-color: #D6001C;
            color: #FFFFFF;
            text-decoration: none;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            padding: 10px 20px;
            border: 2px solid #FFFFFF;
            border-radius: 4px;
            transition: all 0.3s ease;
        }}

        .btn-area-restrita:hover {{
            background-color: #FFFFFF;
            color: #D6001C;
            border-color: #D6001C;
        }}

        /* --- SEÇÃO PRINCIPAL (HERO SECTION) --- */
        .hero-section {{
            position: relative;
            width: 100%;
            height: 100vh; /* Ocupa 100% da altura da janela visível */
            background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                             url('static/imagens/fundo_principal_site.png');
            background-size: cover;
            background-position: center;
            display: flex;
            justify-content: center;
            align-items: center;
            padding-top: 70px; /* Compensa a altura da barra fixa para não cobrir o conteúdo */
        }}

        /* Bloco de conteúdo de texto centralizado sobre a imagem */
        .hero-conteudo {{
            text-align: center;
            color: #FFFFFF;
            max-width: 800px;
            padding: 0 20px;
            z-index: 2;
        }}

        /* Subtítulo menor acima do título principal */
        .hero-subtitulo {{
            font-size: 16px;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: #D6001C; /* Destacado em vermelho */
            margin-bottom: 10px;
        }}

        /* Título Principal Gigante no estilo VIVERONE GARDEN */
        .hero-titulo {{
            font-size: 56px;
            font-weight: 900;
            text-transform: uppercase;
            line-height: 1.1;
            margin-bottom: 20px;
            letter-spacing: 1px;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
        }}

        /* Descrição do que é a empresa */
        .hero-descricao {{
            font-size: 18px;
            font-weight: 400;
            margin-bottom: 35px;
            color: #E0E0E0;
            text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
        }}

        /* Botão de Ação Principal (Estilo SAIBA MAIS da imagem) */
        .btn-saiba-mais {{
            display: inline-block;
            background-color: #00B495; /* Verde moderno idêntico ao da imagem de referência */
            color: #FFFFFF;
            font-size: 14px;
            font-weight: 700;
            text-transform: uppercase;
            text-decoration: none;
            padding: 15px 40px;
            border-radius: 4px;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }}

        .btn-saiba-mais:hover {{
            background-color: #009379;
            transform: translateY(-2px); /* Efeito de flutuar levemente ao passar o mouse */
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }}
    </style>
</head>
<body>

    <nav class="navbar">
        <a href="/" class="logo-link">
            <img src="static/imagens/fidelivros_logo_principal.png" alt="Logo Fidelivros" class="logo-nav">
        </a>

        <ul class="nav-links">
            <li><a href="/">Inicial</a></li>
            <li><a href="#">Quem Somos</a></li>
            <li><a href="#">Livros</a></li>
            <li><a href="#">Fale Conosco</a></li>
        </ul>

        <a href="/login-tela" class="btn-area-restrita">Área Interna 🔒</a>
    </nav>

    <section class="hero-section">
        <div class="hero-conteudo">
            <p class="hero-subtitulo">Sistema de Gestão Integrada</p>
            <h1 class="hero-titulo">Fidelivros<br>Corporativo</h1>
            <p class="hero-descricao">Gerenciamento inteligente de relatórios, monitoramento de estoque e análise de margens de lucro de forma totalmente automatizada.</p>
            <a href="#" class="btn-saiba-mais">Saiba Mais &rarr;</a>
        </div>
    </section>

</body>
</html>
"""
    return html