import smtplib

to = input("Enter the email address of the receiver :")

message =input("Enter the message : ")

def sendEmail(to,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('your email','obnl hojs ttqk cgza')
    server.sendmail('your email',to,message)
    server.close()
    print("MESSAGE SUCCESSFULLY SENT!!!")
    
sendEmail(to,message)