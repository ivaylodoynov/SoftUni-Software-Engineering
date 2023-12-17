import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

credentials = {'username': 'ivaylodoynov8@gmail.com', 'password': 'ivaylodoynov88'}

# Start connection
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Log in to the server
server.login(credentials['username'], credentials['password'])

# Build message
message = MIMEMultipart()
message['Subject'] = 'Demo Mail'
message['From'] = 'ivaylodoynov@gmail.com'
message['To'] = 'ivaylohristov.doynov@omv.com'
message.text = f'Hello! This email is sent from demo! {datetime.now()}'
body = MIMEText(message_text)
message.attach(body)

# Send email
server.send(message)
print('Mail send')
