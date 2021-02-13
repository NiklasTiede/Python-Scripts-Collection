import configparser

import yagmail

# credentials of sender email account:
config = configparser.ConfigParser()
config.read("../settings.ini")
SENDER_EMAIL = config.get("settings", "EMAIL_ADDRESS")
EMAIL_PASSWORD = config.get("settings", "EMAIL_PASSWORD")

receiver = SENDER_EMAIL
body = "Hello there from Yagmail"
filename = "cat.jpg"

yag = yagmail.SMTP("niklastiede2@gmail.com", password=EMAIL_PASSWORD)
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body,
    attachments=filename,
)
