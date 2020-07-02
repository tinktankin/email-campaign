

import imaplib
import email
from email.header import decode_header
import webbrowser
import os


username=""
password=""
imap = imaplib.IMAP4_SSL("imap.gmail.com")
result=imap.login(username, password)
imap.select('"[Gmail]/All Mail"',readonly=True)
#imap.select("INBOX")
response, messages = imap.search(None, 'UnSeen')
messages=messages[0].split()
#print(messages)
latest=int(messages[-1])
oldest=int(messages[0])

#print("Latest : ",latest," oldest :",oldest)

for i in range(latest,latest-20,-1):

    res, msg = imap.fetch(str(i), "(RFC822)")
    
    for response in msg:
        if isinstance(response,tuple):
           msg=email.message_from_bytes(response[1])
           print(msg["Date"])
           print(msg["From"])
           print(msg["Subject"])


