import smtplib
import csv
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pwinput

context = ssl.create_default_context()
port = 465
smtp_server="smtp.gmail.com"

sender_email ="dihfahsih@gmail.com"
password = pwinput.pwinput("Type your password and press enter: ")
  

msg = MIMEMultipart()
msg['from']= "Mail Client"
msg['subject'] = "Testing Mail Client Using gmail"

with open('html_template.html', 'r', encoding="utf8") as file:
    data = file.read()
    
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

