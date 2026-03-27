# from playwright.sync_api import Playwright, sync_playwright
# from time import sleep

# def bot(playwright: Playwright):
#     browser = playwright.chromium.launch(channel='msedge', headless=False)
#     pagina = browser.new_page()
#     pagina.goto("https://app.hugme.com.br")
#     pagina.wait_for_load_state("load", timeout=15000)

#     login_usuario = pagina.locator("xpath=/html/body/div[1]/div[1]/div[1]/section/div[3]/form/div/input")
#     login_usuario.wait_for(state="visible", timeout=5000)
#     login_usuario.type("xx", delay=100)
#     pagina.locator("xpath=/html/body/div[1]/div[1]/div[1]/section/div[3]/form/button").click()

#     pagina.wait_for_load_state("load", timeout=15000)
#     login_senha = pagina.locator("xpath=/html/body/div[1]/div[1]/div[1]/section/div[4]/form/div[2]/input")
#     login_senha.wait_for(state="visible", timeout=15000)
#     login_senha.type("xx", delay=100)

#     # CAPTCHA
#     print("Resolva o CAPTCHA manualmente...")
#     # Clica no botão de login normalmente
#     pagina.locator("xpath=/html/body/div[1]/div[1]/div[1]/section/div[4]/form/button").click()

#     # Aguarda redirecionamento após login
#     pagina.wait_for_url("https://app.hugme.com.br/app.html#/", timeout=15000)
#     pagina.wait_for_load_state("load", timeout=15000)
#     sleep(5)

#     menu_opcao = pagina.locator("nav menu ul li").nth(5)
#     menu_opcao.wait_for(state="visible", timeout=10000)
#     menu_opcao.hover()
#     sleep(10)
#     menu_opcao.click()

#     pagina.wait_for_url("https://app.hugme.com.br/app.html#/dados/tickets/exportar/", timeout=15000)
#     pagina.wait_for_load_state("load", timeout=15000)
#     sleep(10)
#     print("Menu acessado com sucesso!")

#     filtros = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/footer/div/div[2]/a")
#     filtros.click()
#     valorfiltro = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/footer/div/div[2]/div/div[2]/div/div/div/ul/li[32]/a")
#     valorfiltro.click()
#     sleep(15)

#     box = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/div[1]/div[1]/div[1]/select")
#     box.click()
#     valorbox1 = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/div[1]/div[1]/div[1]/select/option[2]")
#     valorbox1.click()
#     nomedoarquivo1 = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/div[1]/div[1]/div[2]/input")
#     nomedoarquivo1.type("112025_Midway Financeira")
#     botao_exportar = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/footer/button")
#     botao_exportar.click()
#     sleep(10)
#     valorbox2 = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/div[1]/div[1]/div[1]/select/option[3]")
#     valorbox2.click()
#     nomedoarquivo2 = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/div[1]/div[1]/div[2]/input")
#     nomedoarquivo2.type("112025_Loja Online")
#     botao_exportar = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/footer/button")
#     botao_exportar.click()
#     sleep(10)
#     valorbox3 = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/div[1]/div[1]/div[1]/select/option[4]")
#     valorbox3.click()
#     nomedoarquivo3 = pagina.locator("xpath==/html/body/div[4]/div/div/div/div[1]/div/div[1]/div[1]/div[2]/input")
#     nomedoarquivo3.type("112025_Carters")
#     botao_exportar = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/footer/button")
#     botao_exportar.click()
#     sleep(10)
#     valorbox4 = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/div[1]/div[1]/div[1]/select/option[5]")
#     valorbox4.click()
#     nomedoarquivo4 = pagina.locator("xpath=xpath==/html/body/div[4]/div/div/div/div[1]/div/div[1]/div[1]/div[2]/input")
#     nomedoarquivo4.type("112025_Midway Digital")
#     botao_exportar = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/footer/button")
#     botao_exportar.click()
#     sleep(300)

# with sync_playwright() as playwright:
#     bot(playwright)

from playwright.sync_api import Playwright, sync_playwright
import random
import time
import os
from datetime import datetime
import re
from dateutil.relativedelta import relativedelta

def simular_comportamento(pagina):
    for _ in range(10):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        pagina.mouse.move(x, y, steps=random.randint(5, 15))
        time.sleep(random.uniform(0.2, 0.5))
    # Scroll na página
    pagina.mouse.wheel(0, random.randint(200, 600))
    time.sleep(random.uniform(0.5, 1.5))

def exportar_arquivo(pagina, opcao_index, nome_arquivo):
    select_box = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/div[1]/div[1]/div[1]/select")
    select_box.click()
    valor_box = pagina.locator(f"xpath=/html/body/div[4]/div/div/div/div[1]/div/div[1]/div[1]/div[1]/select/option[{opcao_index}]")
    valor_box.click()

    input_nome = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/div[1]/div[1]/div[2]/input")
    input_nome.fill(nome_arquivo)

    botao_exportar = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/footer/button")
    botao_exportar.click()
    time.sleep(10)

# -----------------------------
# Fluxo principal
# -----------------------------
def bot(playwright: Playwright):
    perfil_real = r"C:\Users\4061014\AppData\Local\Google\Chrome\User Data"  # Ajuste para seu usuário

    context = playwright.chromium.launch_persistent_context(
        user_data_dir=perfil_real,
        channel="chrome", 
        headless=False
    )
    pagina = context.new_page()

    # Acessar página
    pagina.goto("https://app.hugme.com.br", timeout=30000)
    pagina.wait_for_load_state("load")

    # Verifica se já está logado
    if "app.html#/" in pagina.url:
        print("Sessão já autenticada, pulando login...")
    else:
        print("Faça login manualmente e resolva o CAPTCHA...")
        simular_comportamento(pagina)
        # Aguarda até estar logado
        pagina.wait_for_url("https://app.hugme.com.br/app.html#/", timeout=0)  # Sem timeout, espera indefinidamente
        print("Login concluído!")

    # Navegar até exportação
    menu_opcao = pagina.locator("nav menu ul li").nth(5)
    menu_opcao.wait_for(state="visible", timeout=10000)
    menu_opcao.hover()
    time.sleep(2)
    menu_opcao.click()

    pagina.wait_for_url("https://app.hugme.com.br/app.html#/dados/tickets/exportar/", timeout=15000)
    pagina.wait_for_load_state("load")
    time.sleep(5)
    print("Menu acessado com sucesso!")

    # Aplicar filtros
    filtros = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/footer/div/div[2]/a")
    filtros.click()
    valorfiltro = pagina.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div/footer/div/div[2]/div/div[2]/div/div/div/ul/li[32]/a")
    valorfiltro.click()
    time.sleep(5)

    # Exportações
    exportar_arquivo(pagina, 2, "112025_Midway Financeira")
    exportar_arquivo(pagina, 3, "112025_Loja Online")
    exportar_arquivo(pagina, 4, "112025_Carters")
    exportar_arquivo(pagina, 5, "112025_Midway Digital")

    print("Exportações concluídas!")
    time.sleep(300)

pasta = r"C:\Users\4061014\Downloads"

with sync_playwright() as playwright:
    bot(playwright)


