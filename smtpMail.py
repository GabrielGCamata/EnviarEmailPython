from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
#Cria o objeto para o cabecalho
msg = MIMEMultipart()

msg['From'] = "seu@email.aqui"
password = "sua_senha_aqui"
msg['To'] = "gabrielcamata150@hotmail.com"
msg['Subject'] = "Titulo do email"

#Escreve a mensagem
mensagem = "São Paulo >>>>> Corinthians"


# Coloca a mensagem no email
msg.attach(MIMEText(mensagem, 'plain'))

#cria o server
server = smtplib.SMTP('smtp.gmail.com: 587')

#inicia o server
server.starttls()

#Faz o login do email
server.login(msg['From'], password)

#Envia a mensagem pelo server
server.sendmail(msg['From'], msg['To'], msg.as_string())

#Fecha o servidor
server.quit()

#Mensagem de suceso
print ("Email enviado com sucesso para %s:" % (msg['To']))