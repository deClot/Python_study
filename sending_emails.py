import smtplib, ssl

smtp_server = 'smtp.gmail.com'  # for gmail
port = 465 # for  ssl

sender = 'refenement2@gmail.com'
password = input('Enter your password here: ')

#Encryprion context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    print('It worked!')
