import os
import unicodedata

# Caminho da pasta onde estão os arquivos
caminho = r"digite seu caminho"

for arquivo in os.listdir(caminho):
    # Caminho completo do arquivo original
    caminho_antigo = os.path.join(caminho, arquivo)

    # Ignora diretórios
    if os.path.isdir(caminho_antigo):
        continue

    # Normaliza o texto removendo acentos
    nome_sem_acento = unicodedata.normalize('NFKD', arquivo).encode('ASCII', 'ignore').decode('ASCII')

    # Verifica se o arquivo tinha "interações" no nome e foi alterado
    if "interacoes" in nome_sem_acento.lower() and arquivo != nome_sem_acento:
        caminho_novo = os.path.join(caminho, nome_sem_acento)
        os.rename(caminho_antigo, caminho_novo)
        print(f'Renomeado: {arquivo} -> {nome_sem_acento}')