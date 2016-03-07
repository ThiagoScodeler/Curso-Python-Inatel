import smtplib

to = input("Forneça o destinatário:");
email = input("Forneça o e-mail:");

sender = "noreply.sodexoapp@gmail.com"
subject = "Send e-mail by Python"
headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % \
                                            (sender, to, subject)
msg = headers + "Hello Thiago. How are you?"
#A linha abaixo configura endereço de servidor e porta de entrada
mailserver = smtplib.SMTP("smtp.gmail.com", 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login("noreply.sodexoapp@gmail.com", "sodexoapp")
mailserver.sendmail("noreply.sodexoapp@gmail.com",\
                                email, msg)
mailserver.close()
print("Mensagem Enviada")
