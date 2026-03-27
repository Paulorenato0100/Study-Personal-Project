from bot.scraper import Scraper
from bot.processor import Processor
from bot.exporter import Exporter
from core.logger import Logger
from utils.visual import type_effect, progress_bar
import logging
import os
import time

def run():

    os.system("cls")
    os.system("color 0A")

    Logger.setup()
    log = logging.getLogger(__name__)

    print("""
========================================
     RPA REPORT BOT
   Automação Inteligente de Dados
========================================
""")

    type_effect("Inicializando robô...\n")

    scraper = Scraper()
    processor = Processor()
    exporter = Exporter()

    try:
        type_effect("[1/4] Coletando dados...")
        raw_data = scraper.collect_data()
        progress_bar()

        type_effect("[2/4] Processando dados...")
        processed_data = processor.process(raw_data)
        progress_bar()

        type_effect("[3/4] Gerando relatório...")
        file_path = exporter.export(processed_data)
        progress_bar()

        type_effect("📊 [4/4] Abrindo dashboard...")
        os.system("python -m streamlit run dashboard/app.py")

    except Exception as e:
        log.error(f"Erro geral: {e}")

    finally:
        scraper.close()
        type_effect("\n Processo finalizado com sucesso!")

if __name__ == "__main__":
    run()