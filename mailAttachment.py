import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

eMailid = input("Enter your email id: ")
passWrd = input("Enter your password: ")
recipients = []
recipients.append(input("Enter recipient email id: "))
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

msgSbjct = input("Enter message subject: ")
msgBody = input("Enter your message: ")
for i in recipients:
    message = MIMEMultipart()
    message['From'] = eMailid
    message['To'] = i
    message['Subject'] = msgSbjct
    message.attach(MIMEText(msgBody, 'plain'))
    filename = 'ap.jpg'
    attachment = open(filename, "rb")
    p = MIMEBase('application', 'octect-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    message.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    try:
        s.login(eMailid, passWrd)
    except:
        print("incorrect login credentials")
        break

    j = i
    text = message.as_string()
    s.sendmail(eMailid, j, text)
    print("email sent successfully {}".format(j))
    s.quit()