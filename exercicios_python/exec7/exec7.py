import sys
import smtplib


def send_mail(to, address):
    sender = "noreply.sodexoapp@gmail.com"
    subject = "Enviando mensagem por email"
    headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % \
                                                (sender, to, subject)
    msg = headers + "Hello. How are you?"

    mailserver = smtplib.SMTP("smtp.gmail.com", 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login("noreply.sodexoapp@gmail.com", "sodexoapp")
    mailserver.sendmail("noreply.sodexoapp@gmail.com",\
                                    address, msg)
    mailserver.close()

    print("Mensagem Enviada")

def init():
    to = input("Forneça o nome do remetente: ")
    email_address = input("Forneça seu endereço de email: ")
    send_mail(to, email_address)

if __name__ == "__main__":
    init()
