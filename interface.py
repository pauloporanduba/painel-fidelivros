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
    Gera a interface do Menu Principal com uma barra de navegação vertical (Sidebar)
    que expande automaticamente ao passar o mouse por cima (efeito Hover).
    """
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fidelivros - Menu Principal</title>
    <style>
        /* Importação da fonte Montserrat para manter a identidade moderna do Fidelivros */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700;900&display=swap');
        
        /* Reset global para remover as margens nativas dos navegadores e fixar a fonte */
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Montserrat', sans-serif; }}
        
        /* O corpo do site ocupa toda a tela e esconde barras de rolagem desnecessárias */
        body, html {{ height: 100%; width: 100%; background-color: #ffffff; overflow: hidden; }}
        
        /* 
           BARRA LATERAL (SIDEBAR) - CONFIGURAÇÃO INICIAL (FECHADA)
           - Definimos uma largura inicial estreita (85px) para caber apenas os ícones.
           - 'transition: width 0.4s' faz com que a abertura e o fechamento sejam suaves e elegantes.
        */
        .sidebar {{
            position: fixed; top: 0; left: 0; height: 100vh;
            width: 85px; background-color: #1A1A1A;
            border-right: 4px solid #D6001C; display: flex; flex-direction: column;
            z-index: 1000; transition: width 0.4s cubic-bezier(0.25, 1, 0.5, 1);
            overflow: hidden;
        }}
        
        /* 
           EFEITO DE EXPANSÃO DA BARRA
           Quando o mouse passa por cima da área da sidebar, a largura dela muda de 85px para 260px.
        */
        .sidebar:hover {{
            width: 260px;
        }}
        
        /* Container do Logotipo no topo da barra */
        .sidebar-logo {{
            width: 100%; height: 100px; display: flex; align-items: center;
            padding-left: 20px; border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }}
        
        /* Imagem do logotipo dimensionada para se ajustar perfeitamente no modo fechado */
        .sidebar-logo img {{
            height: 45px; width: auto; transition: transform 0.3s ease;
        }}
        
        /* Lista que agrupa os itens do menu dispostos verticalmente */
        .nav-links {{
            list-style: none; display: flex; flex-direction: column; gap: 10px; padding-top: 20px; flex-grow: 1;
        }}
        
        /* Links de navegação internos da Sidebar */
        .nav-links a {{
            display: flex; align-items: center; text-decoration: none;
            height: 60px; padding-left: 25px; position: relative;
            transition: background 0.3s ease;
        }}
        
        /* Efeito visual de destaque no fundo do link ao passar o mouse */
        .nav-links a:hover {{
            background-color: rgba(214, 0, 28, 0.15);
        }}
        
        /* 
           ESTILIZAÇÃO DOS ÍCONES (SVG)
           - Fixamos uma largura de 32px para que fiquem alinhados no centro quando fechado.
           - O 'transition: transform 0.3s' cria aquele leve crescimento (zoom) pedido.
        */
        .nav-icon {{
            width: 32px; height: 32px; fill: none; stroke: #D6001C;
            stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round;
            flex-shrink: 0; transition: transform 0.3s ease;
        }}
        
        /* EFEITO DE CRESCIMENTO DO ÍCONE: Quando passa o mouse no link, o ícone ganha escala */
        .nav-links a:hover .nav-icon {{
            transform: scale(1.15);
        }}
        
        /* 
           ESTILIZAÇÃO DO TEXTO DOS LINKS
           - Inicialmente eles ficam transparentes (opacity: 0) e deslocados para a esquerda.
           - 'white-space: nowrap' impede que o texto quebre linha enquanto a barra expande.
        */
        .nav-text {{
            color: #FFFFFF; font-size: 14px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 1px; margin-left: 25px; opacity: 0; transform: translateX(-10px);
            transition: opacity 0.3s ease, transform 0.3s ease; white-space: nowrap;
        }}
        
        /* TORNA OS TEXTOS VISÍVEIS: Quando a barra estiver em modo expandido (:hover), mostra as letras */
        .sidebar:hover .nav-text {{
            opacity: 1; transform: translateX(0);
            /* Adiciona um pequeno atraso (delay) para a letra aparecer harmoniosamente após a barra abrir */
            transition-delay: 0.15s;
        }}
        
        /* Botão Especial de Logout posicionado no rodapé da Sidebar */
        .btn-logout {{
            border-top: 1px solid rgba(255, 255, 255, 0.05); margin-top: auto; margin-bottom: 20px;
        }}
        
        /* Altera a cor do ícone de sair para cinza claro por padrão */
        .btn-logout .nav-icon {{ stroke: #A0A0A0; }}
        
        /* Se passar o mouse no botão de sair, ele brilha em vermelho */
        .btn-logout:hover .nav-icon {{ stroke: #D6001C; }}
        
        /* 
           CONTEÚDO PRINCIPAL (HERO SECTION)
           Como a barra lateral está fixa na esquerda, adicionamos um 'padding-left: 85px' 
           para que o texto centralizado compense a largura da barra fechada sem sobreposição.
        */
        .hero-section {{
            position: relative; width: 100%; height: 100vh;
            background-image: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.45)), url('static/imagens/fundo_menu_site.png');
            background-size: cover; background-position: center;
            display: flex; justify-content: center; align-items: center; padding-left: 85px;
        }}
        
        /* Alinhamento dos textos centrais */
        .hero-conteudo {{ text-align: center; color: #FFFFFF; max-width: 850px; padding: 0 20px; }}
        .hero-subtitulo {{ font-size: 20px; font-weight: 700; color: #D6001C; margin-bottom: 12px; letter-spacing: 1px; }}
        .hero-titulo {{ font-size: 64px; font-weight: 900; text-transform: uppercase; line-height: 1.1; margin-bottom: 20px; letter-spacing: 2px; text-shadow: 3px 3px 10px rgba(0,0,0,0.8); }}
        .hero-descricao {{ font-size: 18px; font-weight: 400; margin-bottom: 35px; color: #E5E5E5; text-shadow: 2px 2px 6px rgba(0,0,0,0.6); }}
        
        /* Botão verde central clássico */
        .btn-saiba-mais {{ display: inline-block; background-color: #00B495; color: #FFFFFF; font-size: 14px; font-weight: 700; text-transform: uppercase; text-decoration: none; padding: 15px 40px; border-radius: 4px; letter-spacing: 1px; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }}
        .btn-saiba-mais:hover {{ background-color: #009379; transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.4); }}
    </style>
</head>
<body>

    <!-- ESTRUTURA COMPLETA DA SIDEBAR DINÂMICA -->
    <nav class="sidebar">
        <!-- Logo Corporativa Superior -->
        <div class="sidebar-logo">
            <img src="static/imagens/fidelivros_logo_principal.png" alt="Logo">
        </div>
        
        <!-- Links com Ícones Vetoriais puros (SVG), dispensando arquivos externos de imagem -->
        <ul class="nav-links">
            <li>
                <a href="/menu">
                    <!-- Ícone Vetorial de Gráfico de Linhas (Dashboard) -->
                    <svg class="nav-icon" viewBox="0 0 24 24">
                        <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
                    </svg>
                    <span class="nav-text">Dashboard</span>
                </a>
            </li>
            <li>
                <a href="#">
                    <!-- Ícone Vetorial de Gráfico de Barras (Relatório) -->
                    <svg class="nav-icon" viewBox="0 0 24 24">
                        <path d="M18 20V10M12 20V4M6 20v-6"/>
                    </svg>
                    <span class="nav-text">Relatórios</span>
                </a>
            </li>
            <li>
                <a href="#">
                    <!-- Ícone Vetorial de Monitor com Cifrão de Dinheiro (Faturamento) -->
                    <svg class="nav-icon" viewBox="0 0 24 24">
                        <rect x="2" y="3" width="20" height="14" rx="2"/>
                        <path d="M12 17v4M8 21h8M12 7v6M10 9h4"/>
                    </svg>
                    <span class="nav-text">Faturamento</span>
                </a>
            </li>
            
            <!-- Botão de Desconexão (Sair) ancorado no final -->
            <li class="btn-logout">
                <a href="/logout">
                    <!-- Ícone Vetorial de Porta de Saída -->
                    <svg class="nav-icon" viewBox="0 0 24 24">
                        <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/>
                    </svg>
                    <span class="nav-text">Sair (Logoff)</span>
                </a>
            </li>
        </ul>
    </nav>

    <!-- PAINEL CENTRAL DE CONTEÚDO -->
    <section class="hero-section">
        <div class="hero-conteudo">
            <p class="hero-subtitulo">Olá, {nome_usuario}</p>
            <h1 class="hero-titulo">FIDELIVROS<br>CORPORATIVA</h1>
            <p class="hero-descricao">Análise inteligente de faturamento, emissão de relatórios consolidados e monitoramento gerencial através de painéis automatizados.</p>
            <a href="#" class="btn-saiba-mais">Visualizar Dashboard &rarr;</a>
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