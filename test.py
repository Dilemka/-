# from smtplib import SMTP
 
# HOST = "mySMTP.server.com"
# SUBJECT = "Test email from Python"
# TO = "romantsova@yandex-team.ru"
# FROM = "elenar83@mail.ru"
# text = "Python 3.4 rules them all!"
 
# BODY = "\r\n".join((
#     "From: %s" % FROM,
#     "To: %s" % TO,
#     "Subject: %s" % SUBJECT ,
#     "",
#     text
# ))
 
# server = SMTP("localhost", 8899)
# server.sendmail(FROM, [TO], BODY)
# server.quit()
import smtplib

def send_email(host, subject, to_addr, from_addr, body_text):
    """
    Send an email
    """
 
    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % subject ,
        "",
        body_text
    ))
 
    server = smtplib.SMTP("localhost", 8899)
    server.sendmail(from_addr, [to_addr], BODY)
    server.quit()
    
    
if __name__ == "__main__":
    host = "localhost"
    subject = "Test email from Python"
    to_addr = "romantsova@yandex-team.ru"
    from_addr = "python@mydomain.com"
    body_text = "Python rules them all!"
    send_email(host, subject, to_addr, from_addr, body_text)
