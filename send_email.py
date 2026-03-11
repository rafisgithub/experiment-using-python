import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_host = "smtp.gmail.com"
smtp_port = 587
email_user = "smrafi120@gmail.com"
password = "ynuf jmrp xayt gwou"

receiver = "rafi.cse.ahmed@gmail.com"

msg = MIMEMultipart()
msg["From"] = email_user
msg["To"] = receiver
msg["Subject"] = "Test Email"

msg.attach(MIMEText("Hello this is test mail", "plain"))

server = smtplib.SMTP(smtp_host, smtp_port)
server.starttls()
server.login(email_user, password)

server.sendmail(email_user, receiver, msg.as_string())
server.quit()

print("Email sent successfully")