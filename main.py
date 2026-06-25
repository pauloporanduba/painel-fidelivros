# Arquivo: main.py

# Importamos o 'session' para gerenciar o crachá de acesso e o 'abort' para segurança
from flask import Flask, request, render_template_string, redirect, session
from interface import gerar_html_login, gerar_html_menu, gerar_html_adm

app = Flask(__name__)

# ATENÇÃO: Definimos uma chave secreta para criptografar os dados da sessão do usuário.
# Isso impede que o usuário consiga falsificar o crachá digital.
app.secret_key = 'chave_ultra_secreta_fidelivros_998877'

USUARIOS_PERMITIDOS = {
    "admin": "fidelivros123",
    "paulo": "fidelivros2026",
    "nenem": "fidelivros99"
}

# --- 1. TELA DE LOGIN ---
@app.route('/')
def pagina_inicial_login():
    conteudo_html = gerar_html_login()
    return render_template_string(conteudo_html)


# --- 2. VALIDAÇÃO DO LOGIN ---
@app.route('/login', methods=['POST'])
def processar_login():
    usuario_digitado = request.form.get('txt_usuario')
    senha_digitada = request.form.get('txt_senha')
    
    if usuario_digitado in USUARIOS_PERMITIDOS and USUARIOS_PERMITIDOS[usuario_digitado] == senha_digitada:
        # SUCESSO: Gravamos o usuário na sessão. O crachá digital foi entregue!
        session['usuario_logado'] = usuario_digitado
        return redirect('/menu')
    
    return redirect('/')


# --- 3. ROTA DO MENU PRINCIPAL PROTEGIDA ---
@app.route('/menu')
def pagina_menu_principal():
    """
    Agora o menu está blindado. O Flask confere se o crachá digital existe.
    """
    # 1. Verifica se a variável 'usuario_logado' existe dentro da sessão do navegador
    if 'usuario_logado' not in session:
        print("[SEGURANÇA] Tentativa de invasão detectada! Redirecionando para login.")
        # Se não tiver o crachá, joga de volta para a tela de login imediatamente
        return redirect('/')
        
    # 2. Se o crachá existir, puxamos o nome direto da sessão segura e abrimos o menu
    nome_usuario = session['usuario_logado']
    conteudo_menu = gerar_html_menu(nome_usuario)
    return render_template_string(conteudo_menu)


# --- ROTA DE LOGOUT (SAIR DO SISTEMA) ---
@app.route('/logout')
def realizar_logout():
    """
    Rota que destrói o crachá digital quando o usuário clica em Sair.
    """
    session.pop('usuario_logado', None) # Remove o usuário da sessão
    return redirect('/')


# --- 4. ÁREA ADMINISTRATIVA OCULTA ---
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