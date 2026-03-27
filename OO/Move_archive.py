import os
import pandas as pd
import shutil 

# localizador da pasta de downloads e do caminho final do diretório 
pasta_download = os.path.expanduser("~/Downloads")
pasta_destino = 'digite a pasta'

# listagem dos arquivos que possuem o nome exibição 
arquivos = [f for f in os.listdir(pasta_download) if "Exibição" in f]

for arquivo in arquivos:
    caminho_arquivo = os.path.join(pasta_download,arquivo)
    caminho_final = os.path.join(pasta_destino,arquivo)

    if os.path.exists(pasta_destino):
        print("substituindo arquivo ja existente")
    else: print("arquivo movido para {pasta_destino}")

    shutil.move(caminho_arquivo, caminho_final)

print("processamento concluido")
