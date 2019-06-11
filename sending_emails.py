import smtplib, ssl

smtp_server = 'smtp.gmail.com'  # for gmail
port = 587 # for ssl

sender = 'refenement2@gmail.com'
password = input('Enter your password here: ')

# Encryprion context
context = ssl.create_default_context()

# Creating unencrypted connection and attempt upgrade it
try:
    server = smtplib.SMTP(smtp_server, port) #make a server object
    server.ehlo() # indentify yourself
    server.starttls(context=context) #upgrade connection
    server.ehlo()
    server.login(sender, password)

    print('It worked!')

except Exception as e:
    print(e)
finally:
    server.quit() #close connection to the server
    
