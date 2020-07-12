import imaplib
import email
from email.header import decode_header
import webbrowser
import os


username="" # use your email id here
password="" # use your App Password you generated above here.
imap = imaplib.IMAP4_SSL("imap.gmail.com")
result=imap.login(username, password)
imap.select('"[Gmail]/All Mail"',readonly=True) # Use "[Gmail]/Sent Mails" for fetching mails from Sent Mails. 

response, messages = imap.search(None, 'UnSeen')
messages=messages[0].split()

latest=int(messages[-1])
oldest=int(messages[0])

for i in range(latest,latest-20,-1):

    res, msg = imap.fetch(str(i), "(RFC822)")
    
    for response in msg:
        if isinstance(response,tuple):
           msg=email.message_from_bytes(response[1])
           print(msg["Date"])
           print(msg["From"])
           print(msg["Subject"])
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            print(f'Body: {body.decode("UTF-8")}',)




