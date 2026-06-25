# Arquivo: interface.py

def gerar_html_login():
    """
    1. TELA DE LOGIN PRINCIPAL (Restrita)
    A primeira tela que qualquer um vê ao acessar o site.
    """
    html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fidelivros - Login Restrito</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;900&display=swap');
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Montserrat', sans-serif; }
        body, html { height: 100%; overflow: hidden; }
        .background-container {
            position: relative; width: 100%; height: 100%;
            background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url('static/imagens/fundo_principal_site.png');
            background-size: cover; background-position: center;
            display: flex; justify-content: center; align-items: center;
        }
        .conteudo-central { display: flex; flex-direction: column; align-items: center; text-align: center; z-index: 2; width: 100%; max-width: 400px; padding: 20px; }
        .logo-principal { width: auto; height: 150px; margin-bottom: 10px; }
        .letras-principal {
            color: #FFFFFF; font-size: 42px; font-weight: 900; text-transform: uppercase; margin-bottom: 30px;
            text-shadow: -2px -2px 0 #D6001C, 1px -1px 0 #D6001C, -2px 1px 0 #D6001C, 1px 1px 0 #D6001C, 0px 2px 0 #FFFFFF, 0px -2px 0 #FFFFFF, 2px 0px 0 #FFFFFF, -2px 0px 0 #FFFFFF;
        }
        .form-container { width: 100%; display: flex; flex-direction: column; gap: 15px; margin-bottom: 20px; }
        .input-fidelivros { width: 100%; padding: 14px 20px; font-size: 16px; font-weight: 500; border: 2px solid #FFFFFF; border-radius: 50px; background-color: rgba(255, 255, 255, 0.9); color: #333333; outline: none; transition: all 0.3s ease; }
        .input-fidelivros:focus { border-color: #D6001C; box-shadow: 0 0 10px rgba(214, 0, 28, 0.5); }
        .botao-entrar { width: 100%; background-color: #D6001C; color: #FFFFFF; font-size: 18px; font-weight: 700; text-transform: uppercase; border: 3px solid #FFFFFF; border-radius: 50px; padding: 14px; cursor: pointer; box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3); transition: all 0.3s ease; }
        .botao-entrar:hover { background-color: #b50017; transform: scale(1.03); }
    </style>
</head>
<body>
    <div class="background-container">
        <div class="conteudo-central">
            <img src="static/imagens/fidelivros_logo_principal.png" alt="Logo Fidelivros" class="logo-principal">
            <h1 class="letras-principal">fidelivros</h1>
            <form action="/login" method="POST" class="form-container">
                <input type="text" name="txt_usuario" placeholder="Usuário" class="input-fidelivros" required>
                <input type="password" name="txt_senha" placeholder="Senha" class="input-fidelivros" required>
                <button type="submit" class="botao-entrar">ENTRAR</button>
            </form>
        </div>
    </div>
</body>
</html>"""
    return html


def gerar_html_menu(nome_usuario):
    """
    2. TELA DE MENU PRINCIPAL (ESTILO IMOBILIÁRIA FORMA)
    Só aparece depois que o login é feito com sucesso.
    """
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fidelivros - Menu Principal</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700;900&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Montserrat', sans-serif; }}
        body, html {{ height: 100%; background-color: #ffffff; color: #333333; }}
        
        /* Navbar Superior */
        .navbar {{
            position: fixed; top: 0; left: 0; width: 100%; height: 70px;
            background-color: #2A2A2A; display: flex; justify-content: space-between; align-items: center; padding: 0 40px; z-index: 1000;
            border-bottom: 2px solid #D6001C;
        }}
        .logo-link {{ display: flex; align-items: center; text-decoration: none; height: 100%; }}
        .logo-nav {{ height: 45px; width: auto; transition: transform 0.2s ease; }}
        .logo-link:hover .logo-nav {{ transform: scale(1.05); }}
        
        .nav-links {{ display: flex; gap: 30px; list-style: none; }}
        .nav-links a {{ color: #FFFFFF; text-decoration: none; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; transition: color 0.3s ease; }}
        .nav-links a:hover {{ color: #D6001C; }}
        
        /* Botão de Logout no canto direito */
        .btn-logout {{ background-color: #D6001C; color: #FFFFFF; text-decoration: none; font-size: 12px; font-weight: 700; text-transform: uppercase; padding: 10px 20px; border: 2px solid #FFFFFF; border-radius: 4px; transition: all 0.3s ease; }}
        .btn-logout:hover {{ background-color: #FFFFFF; color: #D6001C; border-color: #D6001C; }}
        
        /* Hero Section */
        .hero-section {{
            position: relative; width: 100%; height: 100vh;
            background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('static/imagens/fundo_principal_site.png');
            background-size: cover; background-position: center;
            display: flex; justify-content: center; align-items: center; padding-top: 70px;
        }}
        .hero-conteudo {{ text-align: center; color: #FFFFFF; max-width: 800px; padding: 0 20px; z-index: 2; }}
        .hero-subtitulo {{ font-size: 16px; font-weight: 500; text-transform: uppercase; letter-spacing: 3px; color: #D6001C; margin-bottom: 10px; }}
        .hero-titulo {{ font-size: 56px; font-weight: 900; text-transform: uppercase; line-height: 1.1; margin-bottom: 20px; letter-spacing: 1px; text-shadow: 2px 2px 8px rgba(0,0,0,0.7); }}
        .hero-descricao {{ font-size: 18px; font-weight: 400; margin-bottom: 35px; color: #E0E0E0; text-shadow: 1px 1px 4px rgba(0,0,0,0.5); }}
        
        .btn-saiba-mais {{ display: inline-block; background-color: #00B495; color: #FFFFFF; font-size: 14px; font-weight: 700; text-transform: uppercase; text-decoration: none; padding: 15px 40px; border-radius: 4px; letter-spacing: 1px; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }}
        .btn-saiba-mais:hover {{ background-color: #009379; transform: translateY(-2px); }}
    </style>
</head>
<body>
    <nav class="navbar">
        <a href="/menu" class="logo-link">
            <img src="static/imagens/fidelivros_logo_principal.png" alt="Logo Fidelivros" class="logo-nav">
        </a>
        <ul class="nav-links">
            <li><a href="/menu">Dashboard</a></li>
            <li><a href="#">Relatórios</a></li>
            <li><a href="#">Estoque</a></li>
            <li><a href="#">Faturamento</a></li>
        </ul>
        <a href="/logout" class="btn-logout">Sair (Logoff) ➔</a>
    </nav>

    <section class="hero-section">
        <div class="hero-conteudo">
            <p class="hero-subtitulo">Olá, {nome_usuario} • Painel Corporativo</p>
            <h1 class="hero-titulo">Fidelivros<br>Corporativo</h1>
            <p class="hero-descricao">Gerenciamento inteligente de relatórios, monitoramento de estoque e análise de margens de lucro de forma totalmente automatizada.</p>
            <a href="#" class="btn-saiba-mais">Abrir Relatórios &rarr;</a>
        </div>
    </section>
</body>
</html>"""
    return html


def gerar_html_adm(lista_usuarios):
    """
    3. TELA DO ADMINISTRADOR SECRETO
    Mantida intacta e protegida para o seu controle de senhas.
    """
    linhas_tabela = ""
    for usuario, senha in lista_usuarios.items():
        linhas_tabela += f"<tr><td style='padding: 10px; border: 1px solid #dddddd;'>{usuario}</td><td style='padding: 10px; border: 1px solid #dddddd;'>{senha}</td></tr>"

    html_base = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
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
        <form action="/adm-adicionar-usuario" method="POST" class="form-adm">
            <input type="text" name="novo_usuario" placeholder="Nome do Usuário" class="input-adm" required>
            <input type="text" name="nova_senha" placeholder="Senha Provisória" class="input-adm" required>
            <button type="submit" class="btn-adm">CADASTRAR</button>
        </form>
        <h2>Usuários com Acesso ao Sistema</h2>
        <table>
            <thead><tr><th style="padding: 10px;">Usuário</th><th style="padding: 10px;">Senha</th></tr></thead>
            <tbody>CHAT_TABELA_CONTEUDO</tbody>
        </table>
    </div>
</body>
</html>"""
    return html_base.replace("CHAT_TABELA_CONTEUDO", linhas_tabela)