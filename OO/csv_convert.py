import os 
import pandas as pd 
from datetime import datetime
import shutil
import openpyxl 

# ARQUIVOS PAYTRUE
pasta_downloads = os.path.expanduser("~/Downloads")
pasta_destino = r"digite sua pasta"
padrao_nome = "202601 -"
arquivos = [f for f in os.listdir(pasta_downloads) if padrao_nome in f and f.endswith(".xlsx")]
print(f"Arquivos encontrados: {arquivos}")

if not arquivos:
    print("Nenhum arquivo correspondente encontrado.")
else:
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta_downloads, arquivo)
        df = pd.read_excel(caminho_arquivo, header=0, engine="openpyxl")
        colunas_para_excluir = ["icones", "logos"]
        df = df.drop(columns=[col for col in colunas_para_excluir if col in df.columns], errors="ignore")
        df = df.dropna(how="all").reset_index(drop=True)
        arquivo_csv = os.path.join(pasta_downloads, arquivo.replace(".xlsx", ".csv"))
        df.to_csv(arquivo_csv, index=False, sep=";")
        
        # Manipulação CSV
        
        df = pd.read_csv(arquivo_csv, sep=";", skiprows=1, header=0)
        df.to_csv(arquivo_csv, sep=";",index=False)
        caminho_final = os.path.join(pasta_destino, os.path.basename(arquivo_csv))
        if os.path.exists(caminho_final):
            print(f"Arquivo com mesmo nome encontrado. Excluindo: {os.path.basename(caminho_final)}")
            os.remove(caminho_final)
        else:
            print(f"Movendo arquivo para {pasta_destino}")
        shutil.move(arquivo_csv, caminho_final)
        print(f"Arquivo {arquivo_csv} gerado e movido com sucesso!")

    print("Processamento concluído.")