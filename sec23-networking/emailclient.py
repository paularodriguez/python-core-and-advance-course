import smtplib
from email.mime.text import MIMEText

body = "This is a test email. How are you?"

msg = MIMEText(body)
msg['From'] = "paula@zapiens.org"
msg['To'] = "paula.rp93@gmail.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

emailUsername = "TODO_USERNAME"
emailPassword = "TODO_PASSWORD"

server.login(emailUsername, emailPassword)
server.send_message(msg)

print("Mail sent")

server.quit()