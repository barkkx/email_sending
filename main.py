import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

import os


load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = email
msg['Subject'] = 'Письмо'

incomplete_modules = ['Основы Python', 'GitHub', 'API']
complete_modules = ['Python введение', 'Командная строка', 'Введение в WEB-разработку', 'Введение в JS']
time = '3 месяца'

answer = input("У тебя есть закрытые модули?(да/нет): ").lower().strip()
if "да" in answer:
    message = f'Привет, Мама! Я занимаюсь в школе уже {time}. Я завершил модули: {", ".join(complete_modules)}.'
elif "нет" in answer:
    message = f'Привет, Мама! Я занимаюсь в школе уже {time}. Сейчас работаю над модулями: {", ".join(incomplete_modules)}. Учёба интересная, узнаю много нового!'
else:
    message = f'Сейчас работаю над модулями: {", ".join(incomplete_modules)}. Учёба мне нравится, получаю много знаний!'

msg.attach(MIMEText(message, "plain"))
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(email, password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()