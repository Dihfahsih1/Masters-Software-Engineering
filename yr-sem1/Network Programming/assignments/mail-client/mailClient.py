import smtplib
import csv
import time
import ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import getpass

context = ssl.create_default_context()
port = 465
smtp_server="smtp.gmail.com"

sender_email ="dihfahsih@gmail.com"
password = getpass.getpass("Type your password and press enter: ")
  

msg = MIMEMultipart()
msg['from']= "Mail Client"

with open('mail.html', 'r', encoding="utf8") as file:
    data = file.read().replace('\n', '')
count = 0

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
  server.login(sender_email, password)
  
  
  with open("mail_list.csv") as file:
      reader = csv.reader(file)
      next(reader)
      for name, email in reader:
          html = data.format(name=name)
          msg.attach(MIMEText(html, "html"))

          server.sendmail(sender_email, email, msg.as_string())

          count += 1
          print(str(count) + ". Sent to " + email)

  server.quit()

