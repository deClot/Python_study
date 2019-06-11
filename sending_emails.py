import smtplib, ssl

smtp_server = 'smtp.gmail.com'  # for gmail
port = 465 # for ssl

sender = 'refenement2@gmail.com'
password = input('Enter your password here: ')

receiver = 'refenement@gmail.com'
message = """\
From: {}
To: {}
Subject: Hi There!
This message was sent from Python!
""".format(sender, receiver)

# Encryprion context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)

    #send email
    server.sendmail(sender, receiver, message)


