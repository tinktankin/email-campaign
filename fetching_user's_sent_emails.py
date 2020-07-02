import imaplib
import email
from email.header import decode_header
import webbrowser
import os


server="imap.gmail.com"

username=""
password=""

imap = imaplib.IMAP4_SSL(server)

imap.login(username,password)

res,messages=imap.select('"[Gmail]/Sent Mail"')

messages=int(messages[0])

for i in range(messages, messages-20, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            From=msg["From"]
            subject=msg["Subject"]
            print(From," ",subject)






