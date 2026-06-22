# Arquivo: main.py

# Importamos a lógica e o visual das outras guias
from dados import calcular_resumo, obter_estoque
from interface import gerar_html

# 1. Definimos os dados atuais do dia
valor_entrada = 1850.00
valor_saida = 250.00

# 2. Processamos as informações usando as outras guias
lucro_final = calcular_resumo(valor_entrada, valor_saida)
lista_livros = obter_estoque()

# 3. Mandamos a guia interface gerar o texto em formato HTML
html_final = gerar_html(valor_entrada, valor_saida, lucro_final, lista_livros)

# 4. Salvamos esse texto dentro de um arquivo .html de verdade
with open("index.html", "w", encoding="utf-8") as arquivo:
    arquivo.write(html_final)

print("Sucesso! O arquivo 'index.html' foi gerado e atualizado com os novos dados.")
# 5. Testando o save do Git