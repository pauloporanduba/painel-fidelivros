# Arquivo: main.py
from flask import Flask, request, render_template_string, redirect, session, send_file
import os
import io
import pandas as pd
from interface import gerar_html_menu, gerar_html_relatorio, gerar_html_relatorio_adm

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'fidelivros_super_secret_998877')

# --- DICIONÁRIO DE USUÁRIOS ---
USUARIOS_PERMITIDOS = {
    "admin": "fidelivros123",
    "paulo": "123456"
}

# --- BANCO DE DADOS ALINHADO COM A IMAGEM image_9b2b3b.png ---
RELATORIOS_DB = [
    {
        "id": 1, "data": "2026-06-25", "nfe": "000123", "canal": "Mercado Livre", 
        "cliente": "João Silva", "destino": "SP", "livro": "Algoritmos e Estruturas de Dados", 
        "quantidade": 2, "valor_nf": 150.00, "preco_livro": 75.00, "tarifa_venda": 18.00, 
        "custo_fixo_ml": 6.50, "envios": 19.90, "valor_lucro": 49.60, "rentabilidade": 33.07
    }
]

# --- ROTA RAIZ (TELA DE LOGIN) ---
# --- ROTA RAIZ (TELA DE LOGIN COM IMAGEM DE FUNDO CORRETA) ---
# --- ROTA RAIZ (TELA DE LOGIN - FUNDO PADRÃO CLARO) ---
@app.route('/')
def pagina_inicial():
    if 'usuario_logado' in session:
        return redirect('/menu')
        
    html_login = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Fidelivros - Login</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');
            * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Montserrat', sans-serif; }
            
            body { 
                display: flex; 
                justify-content: center; 
                align-items: center; 
                height: 100vh; 
                background-color: #f4f6f9; /* Fundo claro padrão do sistema */
            }
            
            .login-container { 
                background: white; 
                padding: 40px; 
                border-radius: 8px; 
                width: 100%; 
                max-width: 400px; 
                border-top: 4px solid #D6001C; 
                box-shadow: 0 10px 25px rgba(0,0,0,0.05); 
            }
            h2 { font-weight: 900; text-transform: uppercase; margin-bottom: 20px; color: #1A1A1A; text-align: center; }
            .input-group { margin-bottom: 15px; display: flex; flex-direction: column; gap: 5px; }
            label { font-size: 11px; font-weight: 700; text-transform: uppercase; color: #666; }
            input { padding: 12px; border: 1px solid #ccc; border-radius: 4px; font-size: 14px; }
            input:focus { border-color: #D6001C; outline: none; }
            .btn-login { background: #D6001C; color: white; border: none; padding: 14px; width: 100%; border-radius: 4px; font-weight: 700; text-transform: uppercase; cursor: pointer; margin-top: 10px; font-size: 14px; }
            .btn-login:hover { background: #b50017; }
            .error-msg { color: #D6001C; font-size: 12px; font-weight: 700; text-align: center; margin-bottom: 15px; }
        </style>
    </head>
    <body>
        <div class="login-container">
            <h2>Fidelivros</h2>
            {% if erro %} <p class="error-msg">{{ erro }}</p> {% endif %}
            <form action="/login-autenticar" method="POST">
                <div class="input-group">
                    <label>Usuário</label>
                    <input type="text" name="usuario" required autocomplete="off">
                </div>
                <div class="input-group">
                    <label>Senha</label>
                    <input type="password" name="senha" required>
                </div>
                <button type="submit" class="btn-login">Entrar no Sistema</button>
            </form>
        </div>
    </body>
    </html>
    """
    erro = request.args.get('erro', '')
    return render_template_string(html_login, erro=erro)

@app.route('/login-autenticar', methods=['POST'])
def autenticar_login():
    usuario_digitado = request.form.get('usuario')
    senha_digitada = request.form.get('senha')
    
    if usuario_digitado in USUARIOS_PERMITIDOS and USUARIOS_PERMITIDOS[usuario_digitado] == senha_digitada:
        session['usuario_logado'] = usuario_digitado
        return redirect('/menu')
    else:
        return redirect('/?erro=Usuario+ou+senha+invalidos')

@app.route('/menu')
def pagina_menu_principal():
    if 'usuario_logado' not in session:
        return redirect('/')
    nome_usuario = session['usuario_logado']
    return render_template_string(gerar_html_menu(nome_usuario))

@app.route('/relatorio')
def pagina_relatorio_usuario():
    if 'usuario_logado' not in session:
        return redirect('/')
        
    usuario_atual = session['usuario_logado']
    filtro_dia = request.args.get('dia', '')
    filtro_mes = request.args.get('mes', '')
    filtro_ano = request.args.get('ano', '')
    
    dados_filtrados = RELATORIOS_DB
    
    if filtro_dia or filtro_mes or filtro_ano:
        dados_filtrados = []
        for r in RELATORIOS_DB:
            ano_r, mes_r, dia_r = r['data'].split('-')
            cond_dia = (filtro_dia == dia_r) if filtro_dia else True
            cond_mes = (filtro_mes == mes_r) if filtro_mes else True
            cond_ano = (filtro_ano == ano_r) if filtro_ano else True
            
            if cond_dia and cond_mes and cond_ano:
                dados_filtrados.append(r)

    conteudo_html = gerar_html_relatorio(dados_filtrados, usuario_atual, filtro_dia, filtro_mes, filtro_ano)
    return render_template_string(conteudo_html)

@app.route('/relatorio-adm')
def pagina_relatorio_adm():
    if 'usuario_logado' not in session or session['usuario_logado'] != 'admin':
        return redirect('/menu')
        
    usuario_atual = session['usuario_logado']
    filtro_dia = request.args.get('dia', '')
    filtro_mes = request.args.get('mes', '')
    filtro_ano = request.args.get('ano', '')
    
    dados_filtrados = RELATORIOS_DB
    if filtro_dia or filtro_mes or filtro_ano:
        dados_filtrados = []
        for r in RELATORIOS_DB:
            ano_r, mes_r, dia_r = r['data'].split('-')
            if (not filtro_dia or filtro_dia == dia_r) and (not filtro_mes or filtro_mes == mes_r) and (not filtro_ano or filtro_ano == ano_r):
                dados_filtrados.append(r)

    conteudo_html = gerar_html_relatorio_adm(dados_filtrados, usuario_atual, filtro_dia, filtro_mes, filtro_ano)
    return render_template_string(conteudo_html)

@app.route('/add-relatorio', methods=['POST'])
def add_relatorio():
    if 'usuario_logado' not in session or session['usuario_logado'] != 'admin':
        return redirect('/')
        
    data = request.form.get('txt_data')
    nfe = request.form.get('txt_nfe')
    canal = request.form.get('txt_canal')
    cliente = request.form.get('txt_cliente')
    destino = request.form.get('txt_destino')
    livro = request.form.get('txt_livro')
    quantidade = int(request.form.get('txt_quantidade', 1))
    valor_nf = float(request.form.get('txt_valor_nf', 0))
    preco_livro = float(request.form.get('txt_preco_livro', 0))
    tarifa_venda = float(request.form.get('txt_tarifa_venda', 0))
    custo_fixo_ml = float(request.form.get('txt_custo_fixo_ml', 0))
    envios = float(request.form.get('txt_envios', 0))
    
    custos_totais = (preco_livro * quantidade) + tarifa_venda + custo_fixo_ml + envios
    valor_lucro = valor_nf - custos_totais
    rentabilidade = (valor_lucro / valor_nf) * 100 if valor_nf > 0 else 0

    novo_id = max(r['id'] for r in RELATORIOS_DB) + 1 if RELATORIOS_DB else 1
    
    RELATORIOS_DB.append({
        "id": novo_id, "data": data, "nfe": nfe, "canal": canal, "cliente": cliente,
        "destino": destino, "livro": livro, "quantidade": quantidade, "valor_nf": valor_nf,
        "preco_livro": preco_livro, "tarifa_venda": tarifa_venda, "custo_fixo_ml": custo_fixo_ml,
        "envios": envios, "valor_lucro": round(valor_lucro, 2), "rentabilidade": round(rentabilidade, 2)
    })
        
    return redirect('/relatorio-adm')

@app.route('/baixar-excel')
def baixar_excel():
    if 'usuario_logado' not in session:
        return redirect('/')
        
    df = pd.DataFrame(RELATORIOS_DB)
    if not df.empty:
        df = df.drop(columns=['id'])
        df.columns = [
            'DATA', 'NFE', 'CANAL DE VENDA', 'CLIENTE', 'DESTINO', 'LIVRO', 
            'QNTIDADE', 'VALOR DA NF', 'PREÇO DO LIVRO', 'TARIFA DE VENDA', 
            'CUSTO FIXO ML', 'ENVIOS', 'VALOR DO LUCRO', 'RENTABILIDADE'
        ]
    
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Faturamento')
    output.seek(0)
    
    return send_file(
        output, 
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True, 
        download_name='Relatorio_Faturamento_Fidelivros.xlsx'
    )

@app.route('/logout')
def realizar_logout():
    session.pop('usuario_logado', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)