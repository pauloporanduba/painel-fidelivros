# Importamos as ferramentas do Flask para criar o servidor web e gerenciar requisições (requests)
from flask import Flask, request, render_template_string, redirect
# Importamos a biblioteca smtplib para efetuar a conexão com o servidor de e-mails
import smtplib
# Importamos as estruturas para montar a mensagem de e-mail formatada
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Importamos a função do seu outro arquivo que gera a tela em HTML
from interface import gerar_html

# Inicializamos o aplicativo Flask criando o nosso servidor
app = Flask(__name__)

def enviar_email_cadastro(email_usuario, nome_usuario):
    """
    Função detalhada responsável por se conectar ao servidor SMTP do Gmail 
    e enviar o e-mail de boas-vindas para o usuário cadastrado.
    """
    servidor_smtp = "smtp.gmail.com"  # Servidor de saída de e-mails do Gmail
    porta_smtp = 587                  # Porta para conexão segura do tipo TLS
    email_remetente = "seu-email@gmail.com"  # COLOQUE AQUI O SEU E-MAIL DO GMAIL
    senha_app = "xxxx xxxx xxxx xxxx"        # COLOQUE AQUI A SUA SENHA DE APP DE 16 DÍGITOS DO GOOGLE
    
    # Criamos o objeto que vai guardar o cabeçalho e o corpo do e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = email_remetente
    mensagem['To'] = email_usuario
    mensagem['Subject'] = "Bem-vindo ao Fidelivros! Confirmação de Cadastro"
    
    # Estrutura visual do e-mail em HTML que o usuário vai receber na caixa de entrada
    corpo_html = f"""
    <html>
        <body style="font-family: 'Arial', sans-serif; color: #333333;">
            <div style="max-width: 600px; margin: 0 auto; border: 1px solid #dddddd; padding: 20px; border-radius: 8px;">
                <h2 style="color: #D6001C; text-align: center;">Olá, {nome_usuario}!</h2>
                <p>Sua conta no <strong>Fidelivros</strong> foi criada com sucesso com o e-mail <em>{email_usuario}</em>.</p>
                <p>Agora você já pode utilizar a nossa plataforma para gerenciar tudo!</p>
                <hr style="border: 0; border-top: 1px solid #eeeeee; margin-top: 20px;">
                <p style="font-size: 12px; color: #777777; text-align: center;">Sistema Fidelivros.</p>
            </div>
        </body>
    </html>
    """
    # Anexamos o texto formatado em HTML dentro do corpo da nossa mensagem
    mensagem.attach(MIMEText(corpo_html, 'html'))
    
    try:
        # Abrimos a conexão SMTP com o servidor do Gmail na porta segura
        cliente_smtp = smtplib.SMTP(servidor_smtp, porta_smtp)
        cliente_smtp.ehlo()        # Cumprimenta o servidor
        cliente_smtp.starttls()    # Ativa a criptografia de canal TLS
        cliente_smtp.ehlo()        # Cumprimenta novamente em canal seguro
        cliente_smtp.login(email_remetente, senha_app) # Realiza a autenticação
        
        # Envia o e-mail convertendo todo o objeto da mensagem para o formato de texto padrão (string)
        cliente_smtp.sendmail(email_remetente, email_usuario, message=mensagem.as_string())
        cliente_smtp.quit()        # Encerra a conexão com o servidor de forma limpa
        print(f"Sucesso: E-mail enviado para {email_usuario}")
        return True
    except Exception as erro:
        # Se falhar por senha errada ou rede, captura a falha e mostra no terminal do Python
        print(f"Erro ao enviar e-mail: {erro}")
        return False


# --- ROTAS DO NOSSO SITE ---

@app.route('/')
def pagina_inicial():
    """
    Rota principal do site (http://127.0.0.1:5000/).
    Ela simplesmente chama a função do interface.py e renderiza o HTML na tela.
    """
    conteudo_html = gerar_html()
    return render_template_string(conteudo_html)


@app.route('/cadastrar', methods=['POST'])
def processar_cadastro():
    """
    Rota invisível que recebe os dados do formulário quando o botão 'CRIAR CONTA' é clicado.
    """
    # Capturamos o que o usuário preencheu em cada campo usando o atributo 'name' correspondente do HTML
    nome = request.form.get('txt_usuario')
    email = request.form.get('txt_email')
    senha = request.form.get('txt_senha')
    
    print(f"\n--- Novo Cadastro Solicitado ---")
    print(f"Usuário: {nome}")
    print(f"E-mail: {email}")
    
    # Chamamos a função para disparar o e-mail de boas-vindas passando os dados capturados
    enviar_email_cadastro(email_usuario=email, nome_usuario=nome)
    
    # Após processar tudo, redireciona o usuário de volta para a tela inicial limpa
    return redirect('/')


# O bloco abaixo garante que o servidor só vai rodar se executarmos diretamente este arquivo main.py
if __name__ == '__main__':
    # O Flask vai rodar o site localmente na porta 5000 e o debug=True faz o site reiniciar sozinho quando alteramos o código
    app.run(debug=True, port=5000)