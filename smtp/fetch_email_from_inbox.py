import imaplib
import email

imap_host = "imap.gmail.com"
email_user = "smrafi120@gmail.com"
password = "ynuf jmrp xayt gwou"

mail = imaplib.IMAP4_SSL(imap_host)
mail.login(email_user, password)

mail.select("inbox")

# Example search by sender
status, messages = mail.search(None, '(FROM "rafi.cse.ahmed@gmail.com")')

email_ids = messages[0].split()

for e_id in email_ids:
    status, msg_data = mail.fetch(e_id, "(RFC822)")

    for response in msg_data:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            print("From:", msg["From"])
            print("Subject:", msg["Subject"])

mail.logout()