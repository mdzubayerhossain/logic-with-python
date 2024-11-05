import smtplib
import config
from email.mime.text import MIMEText

server = smtplib.SMTP("smtp.gmail.com",587)

server.starttls()

EMAIL = config.Email 
PASS = config.Pass
Sent = config.Sent_Email
server.login(EMAIL,PASS)


message = MIMEText("Sent from py")
message["From"] = EMAIL
message["To"] = Sent
message["Subject"] = "Hello World"


server.sendmail(EMAIL,Sent,message.as_string())

print("Mail is successfully sent")
