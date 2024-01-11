import smtplib

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('predictorai2@gmail.com','obnl hojs ttqk cgza')
    server.sendmail('predictorai2@gmail.com','alezjkqqlbvovzxzif@cazlp.com','testing email automation!')
    server.close()
    
sendEmail()