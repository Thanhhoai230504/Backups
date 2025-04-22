import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender,receiver,subject,body,app_password):

    massege = MIMEMultipart()
    massege["From"] = sender
    massege["To"] = receiver
    massege['Subject'] = subject
    massege.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, app_password)
        text = massege.as_string()
        server.sendmail(sender, receiver, text)
        print(f"Email đã được gửi đến {receiver}")

        server.quit()
    except Exception as e:
        print(e)
        print("Email không thể gửi được")    