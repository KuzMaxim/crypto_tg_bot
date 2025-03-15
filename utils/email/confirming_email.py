import smtplib
import os
from email.mime.text import MIMEText
from random import randrange
from dotenv import load_dotenv#type: ignore
import urllib.parse

load_dotenv()

base_url = 'https://t.me/misisPEbot'


server_email = os.getenv("SERVER_EMAIL")
server_email_password = os.getenv("SERVER_EMAIL_PASSWORD")


async def send_email(getter, salt):
    message = salt
    sender = server_email
    password = server_email_password
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(sender, password)
        params = {'text': message}
        query_string = urllib.parse.urlencode(params)
        msg = "{}?{}".format(base_url, query_string)
        server.sendmail(sender, getter, MIMEText(msg).as_string())

        return message
    except Exception as ex:
        raise Exception("Message was not sent")
    finally:
        server.quit()