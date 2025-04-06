from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
from email.mime.text import MIMEText

def sendemail(email_to, email_subject, email_message):
    message = MIMEMultipart("plain")
    message["From"] = "TU_CORREO@ejemplo.com"  # <-- Cambia esto por tu dirección de correo
    message["To"] = f"{email_to}"
    message["Subject"] = f"{email_subject}"
    text = f'{email_message}'
    message.attach(MIMEText(text))

    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("TU_CORREO@ejemplo.com", "TU_CONTRASEÑA")  # <-- Cambia esto por tu contraseña de correo
    server.sendmail(f'{email_to}', f'{email_to}', message.as_string().encode('utf-8'))
    server.quit()

def email():
    email_to = input("Enter recipient email address: ")

    email_subject = input("Enter the subject of the email: ")

    email_message = input("Enter the email message: ")

    sendemail(email_to, email_subject, email_message)

if __name__ == '__main__':
    try:
        email()
    except:
        print("An error occurred.")
