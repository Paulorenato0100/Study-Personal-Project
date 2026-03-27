from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

class Scraper:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.log = logging.getLogger(__name__)

    def collect_data(self):
        self.log.info("Abrindo navegador...")

        self.driver.get("https://quotes.toscrape.com/")
        time.sleep(2)

        # scroll suave (efeito visual)
        for i in range(0, 1000, 200):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(0.3)

        quotes = self.driver.find_elements(By.CLASS_NAME, "quote")

        data = []

        self.log.info("Coletando dados...")

        for q in quotes:
            text = q.find_element(By.CLASS_NAME, "text").text
            author = q.find_element(By.CLASS_NAME, "author").text

            data.append({
                "texto": text,
                "autor": author
            })

            time.sleep(0.4)  # efeito visual

        self.log.info(f"{len(data)} registros coletados")

        return data

    def close(self):
        self.log.info("Fechando navegador...")
        self.driver.quit()