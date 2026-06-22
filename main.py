# Arquivo: main.py

# Importamos as funções das outras guias (dados e interface)
from dados import calcular_resumo, obter_estoque
from interface import gerar_html

print("=== ATUALIZAÇÃO DO PAINEL FIDELIVROS ===")

# O comando input() lê o que você digita no terminal.
# Usamos o 'float()' para converter o texto em número decimal.
valor_entrada = float(input("Digite o total de ENTRADAS de hoje (R$): "))
valor_saida = float(input("Digite o total de SAÍDAS de hoje (R$): "))

# Processamos as informações usando as outras guias
lucro_final = calcular_resumo(valor_entrada, valor_saida)
lista_livros = obter_estoque()

# Mandamos a guia interface gerar o texto em formato HTML
html_final = gerar_html(valor_entrada, valor_saida, lucro_final, lista_livros)

# Salvamos esse texto dentro do arquivo index.html
with open("index.html", "w", encoding="utf-8") as arquivo:
    arquivo.write(html_final)

print("\n---------------------------------------------------------")
print("Sucesso! Abra ou atualize o 'index.html' no seu navegador")
print("para ver o site com os valores que você digitou!")
print("---------------------------------------------------------")