import pandas as pd
from datetime import datetime
import os
import logging
import time

class Exporter:

    def __init__(self):
        self.log = logging.getLogger(__name__)

    def export(self, data):
        try:
            self.log.info("Gerando Excel...")
            time.sleep(1)

            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            output_dir = os.path.join(base_dir, "output")
            os.makedirs(output_dir, exist_ok=True)

            file_name = os.path.join(
                output_dir,
                f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            )

            df = pd.DataFrame(data)
            df.to_excel(file_name, index=False)

            time.sleep(1)

            if os.path.exists(file_name):
                self.log.info(f"Arquivo salvo: {file_name}")
                # os.startfile(file_name)

                # TXT VISUAL (extra pro vídeo)
                txt_path = file_name.replace(".xlsx", ".txt")

                with open(txt_path, "w", encoding="utf-8") as f:
                    f.write("RELATORIO AUTOMATIZADO\n\n")
                    f.write(f"Total de registros: {len(data)}\n")

                os.startfile(txt_path)

                return file_name

            else:
                self.log.error("Erro ao salvar arquivo")
                return None

        except Exception as e:
            self.log.error(f"Erro: {e}")
            return None