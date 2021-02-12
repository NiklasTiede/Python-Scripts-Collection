# go to https://myaccount.google.com/security
# give access by less secure apps


import smtplib
import configparser
import ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

config = configparser.ConfigParser()
config.read('settings.ini')

SENDER_EMAIL = config.get('settings', 'EMAIL_ADDRESS')
EMAIL_PASSWORD = config.get('settings', 'EMAIL_PASSWORD')
RECEIVER_EMAIL = SENDER_EMAIL

message = MIMEMultipart("alternative")
message["Subject"] = "Notification for you!"
message["From"] = SENDER_EMAIL
message["To"] = RECEIVER_EMAIL

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
The Coding Lab has many great tutorials:
http://www.the-coding-lab.com"""

html = """\
<html>
  <body>
    <p>Hi,<br>
       How <b>are</b> you?<br>
       <a href="http://www.the-coding-lab.com">The Coding Lab</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# print(html)

import pathlib
html2 = pathlib.Path("email_template.html").read_text(encoding="utf-8")
print(html2)

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)



# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls(context=ssl.create_default_context())
#     smtp.ehlo()
#
#     smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
#     smtp.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())


print('script executed.')
