import smtplib
import ssl
import argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, email_subject, email_body):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = email_subject

    # Add body to email
    message.attach(MIMEText(email_body, "plain"))

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        # Connect to the Gmail SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description='Send an email using the SMTP protocol.')
    parser.add_argument('senderEmail', help='Your email address')
    parser.add_argument('senderPass', help='Your email password')
    parser.add_argument('recipientEmail', help='Recipient email address')
    parser.add_argument('emailSubject', help='The subject of the email')
    parser.add_argument('emailBody', help='The body of the email')
    args = parser.parse_args()

    send_email(args.senderEmail, args.senderPass, args.recipientEmail, args.emailSubject, args.emailBody)

if __name__ == '__main__':
    main()