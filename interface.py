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
    Gera a interface do Menu Principal com uma barra de navegação vertical (Sidebar).
    O logotipo e o nome 'Fidelivros' expandem juntos ao passar o mouse.
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
        
        body, html {{ height: 100%; width: 100%; background-color: #ffffff; overflow: hidden; }}
        
        /* SIDEBAR CONFIGURAÇÃO */
        .sidebar {{
            position: fixed; top: 0; left: 0; height: 100vh;
            width: 85px; background-color: #1A1A1A;
            border-right: 4px solid #D6001C; display: flex; flex-direction: column;
            z-index: 1000; transition: width 0.4s cubic-bezier(0.25, 1, 0.5, 1);
            overflow: hidden;
        }}
        
        .sidebar:hover {{
            width: 260px;
        }}
        
        /* CONTAINER DO LOGO E TEXTO DO TOPO */
        .sidebar-logo {{
            width: 100%; height: 100px; display: flex; align-items: center;
            padding-left: 20px; border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            text-decoration: none; /* Garante que se virar link, não mude a cor do texto */
        }}
        
        .sidebar-logo img {{
            height: 45px; width: auto; flex-shrink: 0;
        }}
        
        /* TEXTO 'FIDELIVROS' DO TOPO */
        .logo-text {{
            color: #FFFFFF; font-size: 18px; font-weight: 900; text-transform: uppercase;
            letter-spacing: 2px; margin-left: 15px; opacity: 0; transform: translateX(-10px);
            transition: opacity 0.3s ease, transform 0.3s ease; white-space: nowrap;
        }}
        
        /* EFEITO PARA MOSTRAR O NOME DA LOGO NO HOVER */
        .sidebar:hover .logo-text {{
            opacity: 1; transform: translateX(0);
            transition-delay: 0.15s; /* Delay idêntico ao dos outros textos para abrir em sincronia */
        }}
        
        /* LINKS DE NAVEGAÇÃO */
        .nav-links {{
            list-style: none; display: flex; flex-direction: column; gap: 10px; padding-top: 20px; flex-grow: 1;
        }}
        
        .nav-links a {{
            display: flex; align-items: center; text-decoration: none;
            height: 60px; padding-left: 25px; position: relative;
            transition: background 0.3s ease;
        }}
        
        .nav-links a:hover {{
            background-color: rgba(214, 0, 28, 0.15);
        }}
        
        .nav-icon {{
            width: 32px; height: 32px; fill: none; stroke: #D6001C;
            stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round;
            flex-shrink: 0; transition: transform 0.3s ease;
        }}
        
        .nav-links a:hover .nav-icon {{
            transform: scale(1.15);
        }}
        
        .nav-text {{
            color: #FFFFFF; font-size: 14px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 1px; margin-left: 25px; opacity: 0; transform: translateX(-10px);
            transition: opacity 0.3s ease, transform 0.3s ease; white-space: nowrap;
        }}
        
        .sidebar:hover .nav-text {{
            opacity: 1; transform: translateX(0);
            transition-delay: 0.15s;
        }}
        
        /* LOGOUT */
        .btn-logout {{
            border-top: 1px solid rgba(255, 255, 255, 0.05); margin-top: auto; margin-bottom: 20px;
        }}
        
        .btn-logout .nav-icon {{ stroke: #A0A0A0; }}
        .btn-logout:hover .nav-icon {{ stroke: #D6001C; }}
        
        /* HERO SECTION */
        .hero-section {{
            position: relative; width: 100%; height: 100vh;
            background-image: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.45)), url('static/imagens/fundo_menu_site.png');
            background-size: cover; background-position: center;
            display: flex; justify-content: center; align-items: center; padding-left: 85px;
        }}
        
        .hero-conteudo {{ text-align: center; color: #FFFFFF; max-width: 850px; padding: 0 20px; }}
        .hero-subtitulo {{ font-size: 20px; font-weight: 700; color: #D6001C; margin-bottom: 12px; letter-spacing: 1px; }}
        .hero-titulo {{ font-size: 64px; font-weight: 900; text-transform: uppercase; line-height: 1.1; margin-bottom: 20px; letter-spacing: 2px; text-shadow: 3px 3px 10px rgba(0,0,0,0.8); }}
        .hero-descricao {{ font-size: 18px; font-weight: 400; margin-bottom: 35px; color: #E5E5E5; text-shadow: 2px 2px 6px rgba(0,0,0,0.6); }}
        
        .btn-saiba-mais {{ display: inline-block; background-color: #00B495; color: #FFFFFF; font-size: 14px; font-weight: 700; text-transform: uppercase; text-decoration: none; padding: 15px 40px; border-radius: 4px; letter-spacing: 1px; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }}
        .btn-saiba-mais:hover {{ background-color: #009379; transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.4); }}
    </style>
</head>
<body>

    <nav class="sidebar">
        <!-- O bloco do topo agora abriga a imagem e a tag span com a classe logo-text -->
        <a href="/menu" class="sidebar-logo">
            <img src="static/imagens/fidelivros_logo_principal.png" alt="Logo">
            <span class="logo-text">Fidelivros</span>
        </a>
        
        <ul class="nav-links">
            <li>
                <a href="/menu">
                    <svg class="nav-icon" viewBox="0 0 24 24">
                        <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
                    </svg>
                    <span class="nav-text">Dashboard</span>
                </a>
            </li>
            <li>
                <a href="/relatorio">
                    <svg class="nav-icon" viewBox="0 0 24 24"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
                    <span class="nav-text">Relatórios</span>
                </a>
            </li>
            <li>
                <a href="#">
                    <svg class="nav-icon" viewBox="0 0 24 24">
                        <rect x="2" y="3" width="20" height="14" rx="2"/>
                        <path d="M12 17v4M8 21h8M12 7v6M10 9h4"/>
                    </svg>
                    <span class="nav-text">Faturamento</span>
                </a>
            </li>
            
            <li class="btn-logout">
                <a href="/logout">
                    <svg class="nav-icon" viewBox="0 0 24 24">
                        <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/>
                    </svg>
                    <span class="nav-text">Sair (Logoff)</span>
                </a>
            </li>
        </ul>
    </nav>

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

def gerar_html_relatorio(lista_relatorios, usuario_atual, filtro_dia="", filtro_mes="", filtro_ano=""):
    """
    TELA DO USUÁRIO COMUM
    Contém filtros de data (Dia, Mês, Ano), botão de Relatório Geral e exportação para Excel.
    """
    # 1. CONSTRUÇÃO DAS LINHAS DA TABELA (Conforme colunas da imagem image_9b2b3b.png)
    linhas_tabela = ""
    for r in lista_relatorios:
        # Formatamos a data que vem do banco (YYYY-MM-DD) para o padrão brasileiro (DD/MM/YYYY)
        ano_r, mes_r, dia_r = r['data'].split('-')
        data_formatada = f"{dia_r}/{mes_r}/{ano_r}"
        
        linhas_tabela += f"""
        <tr>
            <td>{data_formatada}</td>
            <td>{r['nfe']}</td>
            <td>{r['canal']}</td>
            <td>{r['cliente']}</td>
            <td>{r['destino']}</td>
            <td>{r['livro']}</td>
            <td>{r['quantidade']}</td>
            <td>R$ {r['valor_nf']:.2f}</td>
            <td>R$ {r['preco_livro']:.2f}</td>
            <td>R$ {r['tarifa_venda']:.2f}</td>
            <td>R$ {r['custo_fixo_ml']:.2f}</td>
            <td>R$ {r['envios']:.2f}</td>
            <td style="color: {'#00B495' if r['valor_lucro'] >= 0 else '#D6001C'}; font-weight: 700;">R$ {r['valor_lucro']:.2f}</td>
            <td>{r['rentabilidade']}%</td>
        </tr>
        """

    # Retorna o HTML estruturado com a Sidebar dinâmica
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fidelivros - Relatórios de Vendas</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700;900&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Montserrat', sans-serif; }}
        body, html {{ height: 100%; width: 100%; background-color: #f4f6f9; overflow: hidden; }}
        
        /* SIDEBAR ESTILIZADA (Z-INDEX CORRIGIDO) */
        .sidebar {{
            position: fixed; top: 0; left: 0; height: 100vh; width: 85px; background-color: #1A1A1A;
            border-right: 4px solid #D6001C; display: flex; flex-direction: column; z-index: 9999;
            transition: width 0.4s cubic-bezier(0.25, 1, 0.5, 1); overflow: hidden;
        }}
        .sidebar:hover {{ width: 260px; }}
        .sidebar-logo {{ width: 100%; height: 100px; display: flex; align-items: center; padding-left: 20px; border-bottom: 1px solid rgba(255, 255, 255, 0.05); text-decoration: none; }}
        .sidebar-logo img {{ height: 45px; width: auto; flex-shrink: 0; }}
        .logo-text {{ color: #FFFFFF; font-size: 18px; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; margin-left: 15px; opacity: 0; transform: translateX(-10px); transition: opacity 0.3s ease, transform 0.3s ease; white-space: nowrap; }}
        .sidebar:hover .logo-text {{ opacity: 1; transform: translateX(0); transition-delay: 0.15s; }}
        
        .nav-links {{ list-style: none; display: flex; flex-direction: column; gap: 10px; padding-top: 20px; flex-grow: 1; }}
        .nav-links a {{ display: flex; align-items: center; text-decoration: none; height: 60px; padding-left: 25px; transition: background 0.3s ease; }}
        .nav-links a:hover {{ background-color: rgba(214, 0, 28, 0.15); }}
        .nav-icon {{ width: 32px; height: 32px; fill: none; stroke: #D6001C; stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round; flex-shrink: 0; transition: transform 0.3s ease; }}
        .nav-text {{ color: #FFFFFF; font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-left: 25px; opacity: 0; transform: translateX(-10px); transition: opacity 0.3s ease, transform 0.3s ease; white-space: nowrap; }}
        .sidebar:hover .nav-text {{ opacity: 1; transform: translateX(0); transition-delay: 0.15s; }}
        .btn-logout {{ border-top: 1px solid rgba(255, 255, 255, 0.05); margin-top: auto; margin-bottom: 20px; }}
        
        /* CONTEÚDO PRINCIPAL COM SCROLL LATERAL SE PRECISAR */
        .main-content {{ margin-left: 85px; padding: 40px; height: 100vh; overflow-y: auto; background-color: #f8f9fa; }}
        .titulo-pagina {{ font-size: 28px; font-weight: 900; color: #1A1A1A; text-transform: uppercase; }}
        
        /* BARRA DE FILTROS SUPERIOR */
        .filter-container {{ background: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin: 25px 0; display: flex; gap: 15px; align-items: flex-end; }}
        .form-filtro {{ display: flex; gap: 15px; flex-grow: 1; align-items: flex-end; }}
        .input-group {{ display: flex; flex-direction: column; gap: 5px; }}
        .input-group label {{ font-size: 11px; font-weight: 700; color: #666666; text-transform: uppercase; }}
        .input-field {{ padding: 10px; border: 1px solid #cccccc; border-radius: 4px; font-size: 14px; background: #fdfdfd; width: 100px; }}
        
        /* BOTÕES */
        .btn-filtrar {{ background-color: #1A1A1A; color: white; border: none; padding: 11px 20px; border-radius: 4px; font-weight: 700; cursor: pointer; text-transform: uppercase; font-size: 12px; }}
        .btn-geral {{ background-color: #A0A0A0; color: white; border: none; padding: 11px 20px; border-radius: 4px; font-weight: 700; cursor: pointer; text-transform: uppercase; text-decoration: none; font-size: 12px; }}
        .btn-excel {{ background-color: #00B495; color: white; border: none; padding: 11px 20px; border-radius: 4px; font-weight: 700; cursor: pointer; text-transform: uppercase; text-decoration: none; font-size: 12px; margin-left: auto; }}
        
        /* TABELA SCROLL HORIZONTAL COMPATÍVEL COM PLANILHAS */
        .table-container {{ background: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); overflow-x: auto; }}
        table {{ width: 100%; border-collapse: collapse; text-align: left; min-width: 1300px; }}
        th {{ background-color: #0080FF; color: white; padding: 12px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; border: 1px solid #0066cc; text-align: center; }}
        td {{ padding: 12px; border: 1px solid #eeeeee; color: #333333; font-size: 13px; font-weight: 500; text-align: center; }}
        tr:hover {{ background-color: #f2f7ff; }}
    </style>
</head>
<body>

    <nav class="sidebar">
        <a href="/menu" class="sidebar-logo">
            <img src="static/imagens/fidelivros_logo_principal.png" alt="Logo">
            <span class="logo-text">Fidelivros</span>
        </a>
        <ul class="nav-links">
            <li><a href="/menu"><svg class="nav-icon" viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg><span class="nav-text">Dashboard</span></a></li>
            <li><a href="/relatorio"><svg class="nav-icon" viewBox="0 0 24 24"><path d="M18 20V10M12 20V4M6 20v-6"/></svg><span class="nav-text">Relatórios</span></a></li>
            <li class="btn-logout"><a href="/logout"><svg class="nav-icon" viewBox="0 0 24 24"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/></svg><span class="nav-text">Sair</span></a></li>
        </ul>
    </nav>

    <div class="main-content">
        <h1 class="titulo-pagina">Consulta de Vendas e Rentabilidade</h1>
        
        <!-- SEÇÃO DE FILTROS SUPERIORES -->
        <div class="filter-container">
            <form action="/relatorio" method="GET" class="form-filtro">
                <div class="input-group">
                    <label>Dia</label>
                    <input type="number" name="dia" value="{filtro_dia}" min="1" max="31" placeholder="Ex: 25" class="input-field">
                </div>
                <div class="input-group">
                    <label>Mês</label>
                    <input type="number" name="mes" value="{filtro_mes}" min="1" max="12" placeholder="Ex: 06" class="input-field">
                </div>
                <div class="input-group">
                    <label>Ano</label>
                    <input type="number" name="ano" value="{filtro_ano}" min="2020" max="2030" placeholder="Ex: 2026" class="input-field">
                </div>
                <button type="submit" class="btn-filtrar">Filtrar</button>
                <a href="/relatorio" class="btn-geral">Relatório Geral</a>
            </form>
            
            <!-- BOTÃO DOWNLOAD EXCEL -->
            <a href="/baixar-excel" class="btn-excel">Baixar Planilha Formatada (.xlsx)</a>
        </div>
        
        <!-- TABELA CORPORATIVA -->
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>DATA</th>
                        <th>NFE</th>
                        <th>CANAL DE VENDA</th>
                        <th>CLIENTE</th>
                        <th>DESTINO</th>
                        <th>LIVRO</th>
                        <th>QNTIDADE</th>
                        <th>VALOR DA NF</th>
                        <th>PREÇO DO LIVRO</th>
                        <th>TARIFA DE VENDA</th>
                        <th>CUSTO FIXO ML</th>
                        <th>ENVIOS</th>
                        <th>VALOR DO LUCRO</th>
                        <th>RENTABILIDADE</th>
                    </tr>
                </thead>
                <tbody>
                    {linhas_tabela}
                </tbody>
            </table>
        </div>
    </div>

</body>
</html>"""

def gerar_html_relatorio_adm(lista_relatorios, usuario_atual, filtro_dia="", filtro_mes="", filtro_ano=""):
    """
    TELA DO ADMINISTRADOR
    Contém todos os campos manuais da imagem image_9b2b3b.png em grid para lançamento de faturamento.
    """
    linhas_tabela = ""
    for r in lista_relatorios:
        ano_r, mes_r, dia_r = r['data'].split('-')
        data_formatada = f"{dia_r}/{mes_r}/{ano_r}"
        
        linhas_tabela += f"""
        <tr>
            <td>{data_formatada}</td>
            <td>{r['nfe']}</td>
            <td>{r['canal']}</td>
            <td>{r['cliente']}</td>
            <td>{r['destino']}</td>
            <td>{r['livro']}</td>
            <td>{r['quantidade']}</td>
            <td>R$ {r['valor_nf']:.2f}</td>
            <td>R$ {r['preco_livro']:.2f}</td>
            <td>R$ {r['tarifa_venda']:.2f}</td>
            <td>R$ {r['custo_fixo_ml']:.2f}</td>
            <td>R$ {r['envios']:.2f}</td>
            <td style="color: {'#00B495' if r['valor_lucro'] >= 0 else '#D6001C'}; font-weight: 700;">R$ {r['valor_lucro']:.2f}</td>
            <td>{r['rentabilidade']}%</td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fidelivros - Gerenciamento Administrativo</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700;900&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Montserrat', sans-serif; }}
        body, html {{ height: 100%; width: 100%; background-color: #f4f6f9; overflow: hidden; }}
        
        /* SIDEBAR */
        .sidebar {{
            position: fixed; top: 0; left: 0; height: 100vh; width: 85px; background-color: #1A1A1A;
            border-right: 4px solid #D6001C; display: flex; flex-direction: column; z-index: 9999;
            transition: width 0.4s cubic-bezier(0.25, 1, 0.5, 1); overflow: hidden;
        }}
        .sidebar:hover {{ width: 260px; }}
        .sidebar-logo {{ width: 100%; height: 100px; display: flex; align-items: center; padding-left: 20px; border-bottom: 1px solid rgba(255, 255, 255, 0.05); text-decoration: none; }}
        .sidebar-logo img {{ height: 45px; width: auto; flex-shrink: 0; }}
        .logo-text {{ color: #FFFFFF; font-size: 18px; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; margin-left: 15px; opacity: 0; transform: translateX(-10px); transition: opacity 0.3s ease, transform 0.3s ease; white-space: nowrap; }}
        .sidebar:hover .logo-text {{ opacity: 1; transform: translateX(0); transition-delay: 0.15s; }}
        
        .nav-links {{ list-style: none; display: flex; flex-direction: column; gap: 10px; padding-top: 20px; flex-grow: 1; }}
        .nav-links a {{ display: flex; align-items: center; text-decoration: none; height: 60px; padding-left: 25px; transition: background 0.3s ease; }}
        .nav-links a:hover {{ background-color: rgba(214, 0, 28, 0.15); }}
        .nav-icon {{ width: 32px; height: 32px; fill: none; stroke: #D6001C; stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round; flex-shrink: 0; }}
        .nav-text {{ color: #FFFFFF; font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-left: 25px; opacity: 0; transform: translateX(-10px); transition: opacity 0.3s ease, transform 0.3s ease; white-space: nowrap; }}
        .sidebar:hover .nav-text {{ opacity: 1; transform: translateX(0); transition-delay: 0.15s; }}
        .btn-logout {{ border-top: 1px solid rgba(255, 255, 255, 0.05); margin-top: auto; margin-bottom: 20px; }}
        
        /* CONTEÚDO */
        .main-content {{ margin-left: 85px; padding: 40px; height: 100vh; overflow-y: auto; background-color: #f8f9fa; }}
        .titulo-pagina {{ font-size: 28px; font-weight: 900; color: #D6001C; text-transform: uppercase; }}
        
        /* FILTROS */
        .filter-container {{ background: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin: 20px 0; display: flex; gap: 15px; align-items: flex-end; }}
        .form-filtro {{ display: flex; gap: 15px; flex-grow: 1; align-items: flex-end; }}
        .input-field-filter {{ padding: 10px; border: 1px solid #cccccc; border-radius: 4px; font-size: 14px; width: 100px; }}
        
        /* FORMULÁRIO GRID DE ENTRADA ADM */
        .form-container {{ background: #ffffff; padding: 25px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 30px; border-top: 4px solid #D6001C; }}
        .form-titulo {{ font-size: 16px; font-weight: 700; color: #1A1A1A; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.5px; }}
        .form-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; }}
        .input-group {{ display: flex; flex-direction: column; gap: 5px; }}
        .input-group label {{ font-size: 11px; font-weight: 700; color: #555555; text-transform: uppercase; }}
        .input-field {{ padding: 11px; border: 1px solid #cccccc; border-radius: 4px; font-size: 13px; outline: none; background: #fdfdfd; width: 100%; }}
        .input-field:focus {{ border-color: #D6001C; }}
        
        .btn-filtrar {{ background-color: #1A1A1A; color: white; border: none; padding: 11px 20px; border-radius: 4px; font-weight: 700; cursor: pointer; text-transform: uppercase; font-size: 12px; }}
        .btn-geral {{ background-color: #A0A0A0; color: white; border: none; padding: 11px 20px; border-radius: 4px; font-weight: 700; cursor: pointer; text-transform: uppercase; text-decoration: none; font-size: 12px; }}
        .btn-excel {{ background-color: #00B495; color: white; border: none; padding: 11px 20px; border-radius: 4px; font-weight: 700; text-decoration: none; text-transform: uppercase; font-size: 12px; margin-left: auto; }}
        .btn-submit {{ grid-column: span 4; background-color: #D6001C; color: white; border: none; padding: 14px; border-radius: 4px; font-weight: 700; text-transform: uppercase; cursor: pointer; margin-top: 10px; font-size: 14px; transition: background 0.2s; }}
        .btn-submit:hover {{ background-color: #b50017; }}
        
        /* TABELA */
        .table-container {{ background: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); overflow-x: auto; }}
        table {{ width: 100%; border-collapse: collapse; text-align: left; min-width: 1300px; }}
        th {{ background-color: #0080FF; color: white; padding: 12px; font-size: 11px; text-transform: uppercase; border: 1px solid #0066cc; text-align: center; }}
        td {{ padding: 12px; border: 1px solid #eeeeee; color: #333333; font-size: 13px; font-weight: 500; text-align: center; }}
    </style>
</head>
<body>

    <nav class="sidebar">
        <a href="/menu" class="sidebar-logo">
            <img src="static/imagens/fidelivros_logo_principal.png" alt="Logo">
            <span class="logo-text">Fidelivros</span>
        </a>
        <ul class="nav-links">
            <li><a href="/menu"><svg class="nav-icon" viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg><span class="nav-text">Dashboard</span></a></li>
            <li><a href="/relatorio-adm"><svg class="nav-icon" viewBox="0 0 24 24"><path d="M18 20V10M12 20V4M6 20v-6"/></svg><span class="nav-text">Relatórios</span></a></li>
            <li class="btn-logout"><a href="/logout"><svg class="nav-icon" viewBox="0 0 24 24"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/></svg><span class="nav-text">Sair</span></a></li>
        </ul>
    </nav>

    <div class="main-content">
        <h1 class="titulo-pagina">Painel de Controle - Admin</h1>
        
        <!-- LANÇAMENTO FINANCEIRO -->
        <div class="form-container">
            <h2 class="form-titulo">Lançar Registro de Venda (Campos Planilha)</h2>
            <form action="/add-relatorio" method="POST" class="form-grid">
                <div class="input-group">
                    <label>Data da Venda</label>
                    <input type="date" name="txt_data" class="input-field" required>
                </div>
                <div class="input-group">
                    <label>NFE</label>
                    <input type="text" name="txt_nfe" placeholder="Nº Nota Fiscal" class="input-field" required>
                </div>
                <div class="input-group">
                    <label>Canal de Venda</label>
                    <input type="text" name="txt_canal" placeholder="Ex: Mercado Livre" class="input-field" required>
                </div>
                <div class="input-group">
                    <label>Cliente</label>
                    <input type="text" name="txt_cliente" placeholder="Nome Completo" class="input-field" required>
                </div>
                <div class="input-group">
                    <label>Destino (UF)</label>
                    <input type="text" name="txt_destino" placeholder="Ex: AM, SP" maxlength="2" class="input-field" required>
                </div>
                <div class="input-group">
                    <label>Livro Objeto</label>
                    <input type="text" name="txt_livro" placeholder="Título do Livro" class="input-field" required>
                </div>
                <div class="input-group">
                    <label>Quantidade</label>
                    <input type="number" name="txt_quantidade" min="1" value="1" class="input-field" required>
                </div>
                <div class="input-group">
                    <label>Valor da NF (R$)</label>
                    <input type="number" step="0.01" name="txt_valor_nf" placeholder="0.00" class="input-field" required>
                </div>
                <div class="input-group">
                    <label>Preço do Livro (Custo R$)</label>
                    <input type="number" step="0.01" name="txt_preco_livro" placeholder="0.00" class="input-field" required>
                </div>
                <div class="input-group">
                    <label>Tarifa de Venda (R$)</label>
                    <input type="number" step="0.01" name="txt_tarifa_venda" placeholder="0.00" class="input-field" required>
                </div>
                <div class="input-group">
                    <label>Custo Fixo ML (R$)</label>
                    <input type="number" step="0.01" name="txt_custo_fixo_ml" placeholder="0.00" class="input-field" required>
                </div>
                <div class="input-group">
                    <label>Envios (Frete R$)</label>
                    <input type="number" step="0.01" name="txt_envios" placeholder="0.00" class="input-field" required>
                </div>
                <button type="submit" class="btn-submit">Calcular e Adicionar na Planilha</button>
            </form>
        </div>

        <!-- SEÇÃO DE FILTROS DO ADM -->
        <div class="filter-container">
            <form action="/relatorio-adm" method="GET" class="form-filtro">
                <input type="number" name="dia" value="{filtro_dia}" min="1" max="31" placeholder="Dia" class="input-field-filter">
                <input type="number" name="mes" value="{filtro_mes}" min="1" max="12" placeholder="Mês" class="input-field-filter">
                <input type="number" name="ano" value="{filtro_ano}" min="2020" max="2030" placeholder="Ano" class="input-field-filter">
                <button type="submit" class="btn-filtrar">Filtrar</button>
                <a href="/relatorio-adm" class="btn-geral">Relatório Geral</a>
            </form>
            <a href="/baixar-excel" class="btn-excel">Baixar Planilha (.xlsx)</a>
        </div>

        <!-- TABELA DE EXIBIÇÃO -->
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>DATA</th>
                        <th>NFE</th>
                        <th>CANAL DE VENDA</th>
                        <th>CLIENTE</th>
                        <th>DESTINO</th>
                        <th>LIVRO</th>
                        <th>QNTIDADE</th>
                        <th>VALOR DA NF</th>
                        <th>PREÇO DO LIVRO</th>
                        <th>TARIFA DE VENDA</th>
                        <th>CUSTO FIXO ML</th>
                        <th>ENVIOS</th>
                        <th>VALOR DO LUCRO</th>
                        <th>RENTABILIDADE</th>
                    </tr>
                </thead>
                <tbody>
                    {linhas_tabela}
                </tbody>
            </table>
        </div>
    </div>

</body>
</html>"""