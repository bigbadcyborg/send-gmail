
Setup:<br>
    - Enable two-factor authentication within gmail account settings<br>
    - Get app password @ https://myaccount.google.com/u/1/apppassword<br>

Install:

    pip install secure-smtplib

Run:

    python send-gmail.py senderEmail appSpecificPassword recipientEmail "Email Subject" "This is the email content"

Python automation:
    
    def sendGmail( result, symbol, numBuying, success, orderId, optional="" ):
        msg = result + " " + symbol + " " + numBuying + " " + success + " " + orderId + " " + optional
        subject = "Successful transaction of " + symbol + "(" + numBuying + ")"
        
        result = subprocess.run(["python", "send-gmail.py", senderEmail, appSpecificPassword, recipientEmail, subject, msg], capture_output=True, text=True)
    
        print(result.stdout)

