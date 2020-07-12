'''
GoTo sender's Gmail account first and turn_On/Allow the toggle of "Access of Less Secure Apps" using this link-
https://www.google.com/settings/security/lesssecureapps so that SMTP server can login to sender's gmail account without
security errors.
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'Your_email@gmail.com'
msg['To'] = 'To_email@gmail.com'
msg['Subject'] = 'simple email in python 3'
message = 'here is the email hello sir'
msg.attach(MIMEText(message))


def SendEmail(From, to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()  # identify ourselves to smtp gmail client
        server.starttls()  # secure our email with tls encryption
        server.login(From, 'Your_email_password')  # Update your Email password here!
        server.sendmail(From, to, content)
        print("Mail Sent Successfully!")
    except:
        print("Error occurred while sending mail")


SendEmail(msg['From'], msg['To'], msg.as_string())
