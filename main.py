import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


msg = MIMEMultipart()
msg['From'] = 'mubarakshin.damier@yandex.ru'
msg['To'] = 'mubarakshin.damier@yandex.ru'
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
email = 'mubarakshin.damier@yandex.ru'
password = 'oklrnsnwwpaeqxsh'  
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
