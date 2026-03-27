import pyautogui as p
import os
from datetime import datetime
from time import sleep

# p.FAILSAFE('True')

class DeskNote:

    def gerar_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    def gerar_conteudo(self):
        agora = datetime.now()
        data = agora.strftime("%d/%m/%Y")
        hora = agora.strftime("%H:%M:%S")

        return f"""RELATORIO AUTOMATICO

Data de registro: {data}
Hora de registro: {hora}

Registro para teste RPA.
Execucao realizada com sucesso

Conteudo adicional
Conteudo adicional

Data de registro: {data}
Hora de registro: {hora}

Conteudo adicional
Conteudo adicional

Data de registro: {data}
Hora de registro: {hora}

Finalizacao de testes
.
"""

    def notepad(self):
        p.hotkey('win', 'r')
        sleep(2)
        p.write('notepad', interval=0.05)
        p.press('enter')
        sleep(2)

    def salvar(self, nome):
        p.hotkey('ctrl', 's')
        sleep(2)

        caminho = os.path.join(os.path.expanduser("~"), "Documents", nome)

        p.write(caminho, interval=0.05)
        sleep(1)
        p.press('enter')

    def execucao(self):
        timestamp = self.gerar_timestamp()
        nome_arquivo = f"relatorio_{timestamp}.txt"

        self.notepad()

        conteudo = self.gerar_conteudo()
        p.write(conteudo, interval=0.07)

        self.salvar(nome_arquivo)

        print(f"Arquivo salvo: {nome_arquivo}")


if __name__ == "__main__":
    bot = DeskNote()
    bot.execucao()





# agora = datetime.now()
# data = agora.strftime("%d/%m/%Y")
# hora = agora.strftime("%H:%M:%S")
# print(hora)
# p.hotkey('win', 'r')
# time.sleep(1)
# p.write('notepad', interval=0.05)
# p.press('enter')
# time.sleep(3)
# p.click(500, 500)
# p.write( f'RELATÓRIO AUTOMATICO \n'
#     f'Data de registro: {data}\n'
#     f'Hora de registo: {hora}\n'
#     f'registro para teste RPA\n'
#         , interval=0.05)

# p.hotkey('ctrl', 's')

# print(timestamp)
# timestamp = datetime.now.strftime("%d/%m/%Y", "%H:%M:%S")
# os.system('start chrome https://www.melhorcambio.com/dolar-hoje')
# time.sleep(2)
# print(p.position())
# p.hotkey('win', 'r')
# time.sleep(2)
# p.write('chrome https://www.melhorcambio.com/dolar-hoje', interval=0.05)
# p.press('enter')
# #texto do email
# texto_email = 'e-mail teste para codigo'
# # email remetente, senha, destinatário
# de = 'teste@gmail.com'
# senha = '**********'
# para = 'teste@gmail.com'
# #para02 = ''

# # Setup the MIME
# message = MIMEMultipart()
# message['From'] = de
# message['To'] = para
# #message['To'] = para02
# message['Subject'] = 'Cotação do dolar'   #Título do e-mail

# # Corpo do E-mail com anexos
# message.attach(MIMEText(texto_email, 'plain'))

# # Create SMTP session for sending the mail
# session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
# session.starttls()  # Habilita a segurança
# session.login(de, senha)  # Login e senha de quem envia o e-mail
# texto = message.as_string()
# session.sendmail(de, para, texto)
# session.quit()