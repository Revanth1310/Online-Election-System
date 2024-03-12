import random
import smtplib
from email.mime.text import MIMEText

def generate_otp():
    # Generate a 6-digit random OTP
    return ''.join([str(random.randint(0, 9)) for i in range(6)])

def send_otp_email(email, otp):
    sender_email = "jokerdeva18@gmail.com"
    sender_password = "acnu bsol osui tlps"

    # Create the email message
    message = MIMEText(f"Your OTP is: {otp}")
    message["Subject"] = "OTP for Email Verification"
    message["From"] = sender_email
    message["To"] = email

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [email], message.as_string())

# Your authentication process
def authenticate_user(useremail):
        otp = generate_otp()
        send_otp_email(useremail, otp)
        return otp
        