# Arquivo: main.py

from flask import Flask, request, render_template_string, redirect
# Importamos a estrutura da home e da administração
from interface import gerar_html, gerar_html_adm

app = Flask(__name__)

USUARIOS_PERMITIDOS = {
    "admin": "fidelivros123",
    "paulo": "fidelivros2026",
    "lara": "fidelivros99"
}

# --- 1. ROTA DA NOVA HOME ESTILO IMOBILIÁRIA FORMA ---
@app.route('/')
def pagina_inicial():
    """
    Carrega a nova Landing Page elegante do Fidelivros com a navbar superior,
    logo clicável e botão verde 'Saiba Mais'.
    """
    conteudo_html = gerar_html()
    return render_template_string(conteudo_html)


# --- 2. ROTA DA TELA DE LOGIN (QUANDO CLICA EM ÁREA INTERNA) ---
@app.route('/login-tela')
def tela_login_formulario():
    """
    Exibe um formulário limpo para o funcionário digitar Usuário e Senha.
    Separado da home para manter o visual limpo da marca.
    """
    html_formulario = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Fidelivros - Login Restrito</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;900&display=swap');
            * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Montserrat', sans-serif; }
            body { 
                background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('static/imagens/fundo_principal_site.png');
                background-size: cover; background-position: center; height: 100vh;
                display: flex; justify-content: center; align-items: center;
            }
            .box-login { background: rgba(255, 255, 255, 0.95); padding: 40px; border-radius: 8px; width: 100%; max-width: 360px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
            h2 { color: #D6001C; margin-bottom: 20px; text-transform: uppercase; font-size: 20px; letter-spacing: 1px; }
            .input-field { width: 100%; padding: 12px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px; font-size: 14px; }
            .btn-submit { width: 100%; background: #D6001C; color: white; border: none; padding: 12px; border-radius: 4px; font-weight: bold; cursor: pointer; text-transform: uppercase; }
            .btn-submit:hover { background: #b50017; }
            .back-home { display: inline-block; margin-top: 15px; color: #666; text-decoration: none; font-size: 12px; }
        </style>
    </head>
    <body>
        <div class="box-login">
            <h2>Acesso Restrito</h2>
            <form action="/login" method="POST">
                <input type="text" name="txt_usuario" placeholder="Digite seu Usuário" class="input-field" required>
                <input type="password" name="txt_senha" placeholder="Digite sua Senha" class="input-field" required>
                <button type="submit" class="btn-submit">Entrar no Sistema</button>
            </form>
            <a href="/" class="back-home">&larr; Voltar para o Início</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_formulario)


# --- 3. PROCESSAMENTO DA VALIDAÇÃO DO LOGIN ---
@app.route('/login', methods=['POST'])
def processar_login():
    usuario_digitado = request.form.get('txt_usuario')
    senha_digitada = request.form.get('txt_senha')
    
    if usuario_digitado in USUARIOS_PERMITIDOS and USUARIOS_PERMITIDOS[usuario_digitado] == senha_digitada:
        return f"<h1>Acesso Autorizado! Bem-vindo ao painel operacional, {usuario_digitado}.</h1>"
    
    return redirect('/login-tela')


# --- 4. ÁREA ADMINISTRATIVA SECRETA ---
@app.route('/painel-adm-secreto-paulo')
def pagina_adm():
    conteudo_html_adm = gerar_html_adm(USUARIOS_PERMITIDOS)
    return render_template_string(conteudo_html_adm)


@app.route('/adm-adicionar-usuario', methods=['POST'])
def adm_adicionar_usuario():
    novo_user = request.form.get('novo_usuario')
    nova_pass = request.form.get('nova_senha')
    if novo_user and nova_pass:
        USUARIOS_PERMITIDOS[novo_user] = nova_pass
    return redirect('/painel-adm-secreto-paulo')


if __name__ == '__main__':
    app.run(debug=True, port=5000)