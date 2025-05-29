import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_event_confirmation(to_email: str, event_title: str):
    sender = os.getenv("SENDER_EMAIL")
    host = os.getenv("SMTP_HOST")
    port = int(os.getenv("SMTP_PORT"))
    username = os.getenv("SMTP_USERNAME")
    password = os.getenv("SMTP_PASSWORD")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Confirmation - Événement : {event_title}"
    msg["From"] = sender
    msg["To"] = to_email

    html = f"""
    <html>
      <body>
        <p>Bonjour,<br><br>
           Votre événement <strong>{event_title}</strong> a bien été enregistré !<br>
           Merci d'utiliser EventManager 🎉
        </p>
      </body>
    </html>
    """
    part = MIMEText(html, "html")
    msg.attach(part)

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(sender, to_email, msg.as_string())
