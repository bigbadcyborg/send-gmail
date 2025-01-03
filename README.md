
Setup:<br>
    - Enable two-factor authentication within gmail account settings<br>
    - Get app password @ http://myaccount.google.com/u/1/apppassword<br>

Install:

    pip install secure-smtplib

Run:

    python send-gmail.py senderEmail appSpecificPassword recipientEmail "Email Subject" "This is the email content"

Automate using Python:

    import subprocess
    
    result = subprocess.run(["python", "send-gmail.py", senderEmail, appSpecificPassword, recipientEmail, subject, msg], capture_output=True, text=True)



