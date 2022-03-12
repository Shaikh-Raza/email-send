import smtplib
from email.message import EmailMessage
email_address = 'onlykadirshaikh@gmail.com'
email_password = 'zejvpiiilturvjky'
msg = EmailMessage()
msg['Subject'] = 'Tradetron Login Successfull!'
msg['From'] = email_address
msg['To'] = email_address

msg.add_alternative("""    <!DOCTYPE html>
<html>
    <body>
            <h1 style="color:SlateGray;">Tradetron Login Successfull!</h1>
        </body>
    </html>
""", subtype='html')

i = 1

while i == 1 :
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        time.sleep(3600)
        i = i+1
