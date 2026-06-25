# Arquivo: interface.py

def gerar_html():
    """
    Gera a interface principal baseada no layout moderno de portfólio.
    Removido o f-string do bloco principal para evitar erros de sintaxe com o CSS.
    """
    html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fidelivros - Home</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700;900&display=swap');

        /* Reset total de margens e preenchimentos para controle absoluto do layout */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Montserrat', sans-serif;
        }

        body, html {
            height: 100%;
            background-color: #ffffff;
            color: #333333;
        }

        /* --- BARRA DE NAVEGAÇÃO SUPERIOR (NAVBAR) --- */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 70px;
            background-color: #2A2A2A;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 40px;
            z-index: 1000;
            border-bottom: 2px solid #D6001C;
        }

        .logo-link {
            display: flex;
            align-items: center;
            text-decoration: none;
            height: 100%;
        }

        .logo-nav {
            height: 45px;
            width: auto;
            transition: transform 0.2s ease;
        }

        .logo-link:hover .logo-nav {
            transform: scale(1.05);
        }

        .nav-links {
            display: flex;
            gap: 30px;
            list-style: none;
        }

        .nav-links a {
            color: #FFFFFF;
            text-decoration: none;
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: color 0.3s ease;
        }

        .nav-links a:hover {
            color: #D6001C;
        }

        .btn-area-restrita {
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
        }

        .btn-area-restrita:hover {
            background-color: #FFFFFF;
            color: #D6001C;
            border-color: #D6001C;
        }

        /* --- SEÇÃO PRINCIPAL (HERO SECTION) --- */
        .hero-section {
            position: relative;
            width: 100%;
            height: 100vh;
            background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                             url('static/imagens/fundo_principal_site.png');
            background-size: cover;
            background-position: center;
            display: flex;
            justify-content: center;
            align-items: center;
            padding-top: 70px;
        }

        .hero-conteudo {
            text-align: center;
            color: #FFFFFF;
            max-width: 800px;
            padding: 0 20px;
            z-index: 2;
        }

        .hero-subtitulo {
            font-size: 16px;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: #D6001C;
            margin-bottom: 10px;
        }

        .hero-titulo {
            font-size: 56px;
            font-weight: 900;
            text-transform: uppercase;
            line-height: 1.1;
            margin-bottom: 20px;
            letter-spacing: 1px;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
        }

        .hero-descricao {
            font-size: 18px;
            font-weight: 400;
            margin-bottom: 35px;
            color: #E0E0E0;
            text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
        }

        .btn-saiba-mais {
            display: inline-block;
            background-color: #00B495;
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
        }

        .btn-saiba-mais:hover {
            background-color: #009379;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
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


def gerar_html_adm(lista_usuarios):
    """
    Gera a interface do painel do Administrador de forma segura.
    As variáveis são injetadas fora da string principal para não quebrar com o CSS.
    """
    linhas_tabela = ""
    for usuario, senha in lista_usuarios.items():
        linhas_tabela += f"<tr><td style='padding: 10px; border: 1px solid #dddddd;'>{usuario}</td><td style='padding: 10px; border: 1px solid #dddddd;'>{senha}</td></tr>"

    html_base = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fidelivros - Painel ADM</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght=500;700;900&display=swap');
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Montserrat', sans-serif; }
        body { background-color: #f4f6f9; padding: 40px; color: #333333; }
        .container-adm { max-width: 800px; margin: 0 auto; background: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        h1 { color: #D6001C; margin-bottom: 10px; }
        h2 { margin-top: 30px; margin-bottom: 15px; font-size: 20px; }
        .form-adm { display: flex; gap: 10px; margin-bottom: 30px; }
        .input-adm { padding: 10px; border: 1px solid #cccccc; border-radius: 4px; flex: 1; font-size: 14px; }
        .btn-adm { background-color: #D6001C; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: 700; }
        .btn-adm:hover { background-color: #b50017; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th { background-color: #333333; color: white; padding: 10px; text-align: left; }
    </style>
</head>
<body>
    <div class="container-adm">
        <h1>Painel de Controle - Administrador</h1>
        <p>Gerenciamento interno de acessos ao Sistema Fidelivros.</p>
        
        <h2>Cadastrar Novo Usuário Autorizado</h2>
        <form action="/adm-adicionar-usuario" method="POST" class="form-adm">
            <input type="text" name="novo_usuario" placeholder="Nome do Usuário" class="input-adm" required>
            <input type="text" name="nova_senha" placeholder="Senha Provisória" class="input-adm" required>
            <button type="submit" class="btn-adm">CADASTRAR</button>
        </form>

        <h2>Usuários com Acesso ao Sistema</h2>
        <table>
            <thead>
                <tr>
                    <th style="padding: 10px;">Usuário</th>
                    <th style="padding: 10px;">Senha</th>
                </tr>
            </thead>
            <tbody>
                CHAT_TABELA_CONTEUDO
            </tbody>
        </table>
    </div>
</body>
</html>
"""
    # Substitui a marcação do texto pelas linhas geradas dinamicamente sem quebrar a string
    return html_base.replace("CHAT_TABELA_CONTEUDO", linhas_tabela)