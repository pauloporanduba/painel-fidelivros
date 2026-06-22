# Arquivo: interface.py

def gerar_html(entradas, saidas, lucro, livros):
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fidelivros - Início</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&display=swap');

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

        /* Container do Fundo com a sua imagem local e o efeito escurecido */
        .background-container {{
            position: relative;
            width: 100%;
            height: 100%;
            /* O linear-gradient aplica a camada preta com 40% de opacidade (0.4) para dar destaque */
            background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), 
                             url('imagens/fundo_principal_site.png');
            background-size: cover;
            background-position: center;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        /* Bloco centralizado para alinhar os elementos verticalmente */
        .conteudo-central {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            z-index: 2;
        }}

        /* Imagem da Logo Principal */
        .logo-principal {{
            width: auto;
            height: 180px; /* Ajuste a altura conforme achar melhor */
            margin-bottom: 15px;
        }}

        /* --- Estilo Atualizado para as Letras --- */
        .letras-principal {{
            color: #FFFFFF; /* Branco para a cor principal do texto */
            font-size: 50px; /* Ajuste o tamanho conforme necessário */
            font-weight: 900; /* Texto bem grosso */
            text-transform: uppercase;
            margin-bottom: 35px;
            /* Contorno (stroke) Vermelho e Branco para destaque total */
            text-shadow: 
                -2px -2px 0 #D6001C,  1px -1px 0 #D6001C,
                -2px 1px 0 #D6001C,   1px 1px 0 #D6001C,
                0px 2px 0 #FFFFFF,    0px -2px 0 #FFFFFF,
                2px 0px 0 #FFFFFF,    -2px 0px 0 #FFFFFF;
        }}
        /* ---------------------------------------- */

        /* Botão Artificial INICIAR criado com CSS */
        .botao-iniciar {{
            display: inline-block;
            background-color: #D6001C; /* Vermelho Fidelivros */
            color: #FFFFFF;
            font-size: 22px;
            font-weight: 700;
            text-transform: uppercase;
            text-decoration: none;
            padding: 14px 65px;
            border: 3px solid #FFFFFF; /* Borda branca idêntica ao Canva */
            border-radius: 50px; /* Cantos totalmente arredondados */
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
            cursor: pointer;
        }}

        /* Efeito de hover (passar o mouse) no botão artificial */
        .botao-iniciar:hover {{
            background-color: #b50017;
            transform: scale(1.05); /* Dá um leve zoom ao passar o mouse */
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
        }}
    </style>
</head>
<body>

    <div class="background-container">
        <div class="conteudo-central">
            <!-- Puxando a sua imagem da logo local -->
            <img src="imagens/fidelivros_logo_principal.png" alt="Logo Fidelivros" class="logo-principal">

            <!-- Novo Texto em Branco e Vermelho -->
            <h1 class="letras-principal">fidelivros</h1>

            <!-- Botão artificial interativo -->
            <a href="#" class="botao-iniciar">INICIAR</a>
        </div>
    </div>

</body>
</html>
"""
    return html