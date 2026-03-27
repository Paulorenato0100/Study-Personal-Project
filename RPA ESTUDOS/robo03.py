import pyautogui as p
import os
from time import sleep
import shutil
import openpyxl

class OrgDesk:

    def __init__(self):
        
        self.docs = "documentos"
        self.img = "imagens"
        self.plans = "planilhas"
        self.pdfs = "pdfs"
        self.outros = "outros"


    def orgpastas(self):

        self.base_path = os.path.join(os.path.expanduser("~"), "Downloads")
        os.makedirs(os.path.join(self.base_path,self.docs), exist_ok=True)
        os.makedirs(os.path.join(self.base_path,self.img), exist_ok=True)
        os.makedirs(os.path.join(self.base_path,self.plans), exist_ok=True)
        os.makedirs(os.path.join(self.base_path,self.pdfs), exist_ok=True)
        os.makedirs(os.path.join(self.base_path,self.outros), exist_ok=True)


    def abrirexplorer(self):
        p.hotkey('win', 'e')
        sleep(2)
        p.hotkey('Ctrl', 'L')
        sleep(2)

        self.orgpastas()

    def listagem_e_mover(self):

        downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        lista = os.listdir(self.base_path)
        print(f'arquivos listados: {lista}')

        # for arquivos in lista:
        #     if arquivos.endswith(".pdf"):
        #         shutil.move(self.pdfs)
        #     elif arquivos.endswith(".")