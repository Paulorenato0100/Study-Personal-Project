import logging
import time

class Processor:

    def __init__(self):
        self.log = logging.getLogger(__name__)

    def process(self, data):
        self.log.info("Processando dados...")
        time.sleep(1)

        processed = []

        for item in data:
            texto = item["texto"]

            processed.append({
                "Autor": item["autor"].upper(),
                "Texto": texto,
                "Tamanho_Texto": len(texto),
                "Qtd_Palavras": len(texto.split())
            })

        time.sleep(1)

        self.log.info("Dados processados com sucesso")

        return processed