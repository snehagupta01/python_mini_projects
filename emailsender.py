import smtplib

to=input("Enter the email of recipient\n")
content=input("Enter Content\n")

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com','12345')
    server.sendmail('abc@gmail.com',to,content)
    server.close()

sendEmail(to,content)