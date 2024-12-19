
Setup:
    - Enable two-factor authentication
    - Get app password @ https://myaccount.google.com/u/1/apppassword

Install:

    pip install secure-smtplib

Run:

    python send-gmail.py senderEmail appSpecificPassword recipientEmail "Email Subject" "This is the email content"
