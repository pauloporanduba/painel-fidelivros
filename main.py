# Arquivo: main.py

from flask import Flask, request, render_template_string, redirect
# Importamos as duas funções do interface.py agora
from interface import gerar_html, gerar_html_adm

app = Flask(__name__)

# O nosso dicionário agora funciona como o banco de dados temporário do sistema
USUARIOS_PERMITIDOS = {
    "admin": "fidelivros123",
    "paulo": "fidelivros2026",
    "nenem": "fidelivros99"
}

# --- ROTA DA TELA DE LOGIN COMUM ---
@app.route('/')
def pagina_inicial():
    conteudo_html = gerar_html()
    return render_template_string(conteudo_html)


# --- ROTA QUE PROCESSA O LOGIN ---
@app.route('/login', methods=['POST'])
def processar_login():
    usuario_digitado = request.form.get('txt_usuario')
    senha_digitada = request.form.get('txt_senha')
    
    if usuario_digitado in USUARIOS_PERMITIDOS and USUARIOS_PERMITIDOS[usuario_digitado] == senha_digitada:
        return f"<h1>Acesso Permitido! Bem-vindo ao Menu do Fidelivros, {usuario_digitado}.</h1>"
    
    return redirect('/')


# =====================================================================
# --- ÁREA ADMINISTRATIVA OCULTA (SÓ VOCÊ SABE O CAMINHO) ---
# =====================================================================

@app.route('/painel-adm-secreto-paulo')
def pagina_adm():
    """
    Sua rota secreta. Digitando esse endereço direto no navegador,
    o Flask chama a tela de ADM passando a lista de usuários atuais.
    """
    # Passamos o dicionário de usuários para a função gerar a tabela dinamicamente
    conteudo_html_adm = gerar_html_adm(USUARIOS_PERMITIDOS)
    return render_template_string(conteudo_html_adm)


@app.route('/adm-adicionar-usuario', methods=['POST'])
def adm_adicionar_usuario():
    """
    Rota que o formulário do painel ADM chama para adicionar um novo 
    funcionário dentro do dicionário de permissões.
    """
    novo_user = request.form.get('novo_usuario')
    nova_pass = request.form.get('nova_senha')
    
    if novo_user and nova_pass:
        # Adiciona o novo par de usuário e senha direto no dicionário da memória
        USUARIOS_PERMITIDOS[novo_user] = nova_pass
        print(f"[ADM] Novo usuário cadastrado com sucesso: {novo_user}")
        
    # Após cadastrar, recarrega a página do painel ADM para exibir o novo usuário na tabela
    return redirect('/painel-adm-secreto-paulo')


if __name__ == '__main__':
    app.run(debug=True, port=5000)