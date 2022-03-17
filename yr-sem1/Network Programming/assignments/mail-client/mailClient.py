import smtplib
import csv
import time
import ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context)

sender_email ="dihfahsih@mail.com"
with open('password.txt', 'r') as psw:
  password=psw.read()
  
server.ehlo()
server.login(sender_email, password)

msg = MIMEMultipart()
msg['from']= "Mail Client"

with open('mail.html', 'r', encoding="utf8") as file:
    data = file.read().replace('\n', '')
count = 0

with open("mail_list.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for name, email in reader:
        html = data.format(name=name)
        msg.attach(MIMEText(html, "html"))

        server.sendmail(
            sender_email, email, msg.as_string()
        )

        count += 1
        print(str(count) + ". Sent to " + email)

server.quit()

