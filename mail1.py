import smtplib

eMailid = input("Enter your email id: ")
passWrd = input("Enter your password")
recipients = []
recipients.append(input("Enter recipient email id: "))
message = input("Enter your message: ")
while True:
    print('''press 1 to add another recipient
press 0 to send email
    ''')
    a = int(input("Enter your choice: "))
    if a == 0:
        break
    elif a == 1:
        recipients.append(input("Enter recipient email id: "))
    else:
        print("enter a valid choice")
try:
    for i in recipients:
        print("sending email to", i)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(eMailid, passWrd)
        try:
            s.sendmail(eMailid, i, message)
            print("email sent successfully {}".format(i))
        except:
            print("couldn't send email")
        s.quit()
except:
    print("invalid user id or password!!")
