from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os


load_dotenv()
progress_modules = ["Основый Python", "WEB разработка (HTML/CSS)"]
completed_modules = []
time = "7 месяцев"
message_text = f"Привет Мама(Папа), я занимаюсь в школе третье место уже {time}.в процессе я выполнил модули: {completed_modules}! Сейчас я работаю над модулями {progress_modules}. Обучение мне нравится, я получил море знаний!"
if not completed_modules:
    message_text = f"Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. Сейчас я работаю над модулями {progress_modules}. Пока что я улучшаю свои навыки и узнаю много нового!"

msg = MIMEMultipart()
msg["From"] = os.environ['EMAIL_FROM']
msg["To"] = os.environ['EMAIL_FROM']
msg["Subject"] = "Важно!"
msg.attach(MIMEText(message_text, "plain"))

password = os.environ['PASSWORD']
server = smtplib.SMTP_SSL("smtp.yandex.ru:465")
server.login(msg["From"], password)

server.sendmail(msg["From"], msg["To"], msg.as_string())

