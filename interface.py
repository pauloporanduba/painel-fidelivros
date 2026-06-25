# Arquivo: interface.py

def gerar_html():
    """
    Função que retorna a estrutura do HTML da página de Login restrita.
    Apenas usuários previamente cadastrados pelo administrador podem tentar o acesso.
    """
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fidelivros - Login Restrito</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;900&display=swap');

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Montserrat', sans-serif;
        }}

        body, html {{
            height: 100%;
            overflow: hidden;
        }}

        /* Container do Fundo com o caminho correto do Flask (static/) e a camada escura */
        .background-container {{
            position: relative;
            width: 100%;
            height: 100%;
            background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), 
                             url('static/imagens/fundo_principal_site.png');
            background-size: cover;
            background-position: center;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        /* Bloco centralizado para o formulário */
        .conteudo-central {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            z-index: 2;
            width: 100%;
            max-width: 400px;
            padding: 20px;
        }}

        /* Imagem da Logo Principal */
        .logo-principal {{
            width: auto;
            height: 150px;
            margin-bottom: 10px;
        }}

        /* Texto Fidelivros com contorno */
        .letras-principal {{
            color: #FFFFFF;
            font-size: 42px;
            font-weight: 900;
            text-transform: uppercase;
            margin-bottom: 30px;
            text-shadow: 
                -2px -2px 0 #D6001C,  1px -1px 0 #D6001C,
                -2px 1px 0 #D6001C,   1px 1px 0 #D6001C,
                0px 2px 0 #FFFFFF,    0px -2px 0 #FFFFFF,
                2px 0px 0 #FFFFFF,    -2px 0px 0 #FFFFFF;
        }}

        /* Container dos campos de entrada */
        .form-container {{
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-bottom: 20px;
        }}

        /* Estilização dos Inputs */
        .input-fidelivros {{
            width: 100%;
            padding: 14px 20px;
            font-size: 16px;
            font-weight: 500;
            border: 2px solid #FFFFFF;
            border-radius: 50px;
            background-color: rgba(255, 255, 255, 0.9);
            color: #333333;
            outline: none;
            transition: all 0.3s ease;
        }}

        .input-fidelivros:focus {{
            border-color: #D6001C;
            box-shadow: 0 0 10px rgba(214, 0, 28, 0.5);
        }}

        /* Container do Botão */
        .botoes-container {{
            width: 100%;
        }}

        /* Botão Entrar Único (Vermelho com borda branca) */
        .botao-entrar {{
            width: 100%;
            background-color: #D6001C;
            color: #FFFFFF;
            font-size: 18px;
            font-weight: 700;
            text-transform: uppercase;
            border: 3px solid #FFFFFF;
            border-radius: 50px;
            padding: 14px;
            cursor: pointer;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }}

        .botao-entrar:hover {{
            background-color: #b50017;
            transform: scale(1.03);
        }}
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

                <div class="botoes-container">
                    <button type="submit" class="botao-entrar">ENTRAR</button>
                </div>
            </form>
        </div>
    </div>

</body>
</html>
"""
    return html