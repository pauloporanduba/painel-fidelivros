# Arquivo: dados.py

def calcular_resumo(entrada, saida):
    lucro = entrada - saida
    return lucro

def obter_estoque():
    # Simulando os livros e as quantidades em estoque
    lista_livros = [
        {"titulo": "Dom Casmurro", "qtd": 15},
        {"titulo": "O Alquimista", "qtd": 8},
        {"titulo": "Memórias Póstumas", "qtd": 22},
        {"titulo": "O Pequeno Príncipe", "qtd": 5}
    ]
    return lista_livros