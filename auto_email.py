import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(from_email, password)
            smtp.sendmail(from_email, to_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    subject = "Automatic Email"
    body = "This is an automatic email sent using Python!"
    to_email = ""  # Replace with the recipient's email address
    from_email = ""  # Replace with your Gmail email address
    password = ""  # Replace with your Gmail password or app password

    send_email(subject, body, to_email, from_email, password)
