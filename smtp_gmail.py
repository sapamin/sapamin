import sys
from email.mime.text import MIMEText
import smtplib
import imaplib
import email
from email.header import decode_header, make_header
input=sys.stdin.readline
content=""
print("ID:",end="")
id=str(input())
print("PASSWORD:",end="")
pw=str(input())

while(1):
    print("Mode:",end="")
    mode=str(input())


    if mode=="send\n":
        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp.ehlo()
        smtp.login(id, pw)
        print("TO:", end="")
        to = str(input())
        print("SUBJECT:", end="")
        sub = str(input())
        print("MESSAGE:", end="")
        message = str(input())
        mesg = MIMEText(message)
        mesg['Subject'] = sub
        mesg['To'] = to
        smtp.sendmail(id,to, mesg.as_string())
        smtp.quit()
        print("send success")
        continue

    elif mode=="receive\n":
        imap = imaplib.IMAP4_SSL('imap.gmail.com',"993")
        imap.login(id, pw)
        rv, data = imap.select()
        recent_no = data[0]
        rv, fetched = imap.fetch(recent_no, '(RFC822)')
        msg = email.message_from_bytes(fetched[0][1])
        fr = make_header(decode_header(msg.get('From')))
        subject = make_header(decode_header(msg.get('Subject')))

        if msg.is_multipart():
            for part in msg.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    body = part.get_payload(decode=True)
                    break
        else:
            body = msg.get_payload(decode=True)

        body = body.decode('utf-8')
        print(body)
        f = open("last email_"+ ".html", "wb")
        f.write(body.encode())
        f.close()
        imap.close()
        imap.logout()
        print("receive success")
        continue

    else:
        print(mode)
        print("quit")
        break