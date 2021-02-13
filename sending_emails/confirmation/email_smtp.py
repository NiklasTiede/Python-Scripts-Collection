

import configparser
import json
import pathlib
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Template

# credentials of sender email account:
config = configparser.ConfigParser()
config.read("../settings.ini")
SENDER_EMAIL = config.get("settings", "EMAIL_ADDRESS")
EMAIL_PASSWORD = config.get("settings", "EMAIL_PASSWORD")


# message in plain text:
text_template = """\
Hey fellow,
You've been successfully registered, {{ firstName }}!
{% if premium %}
You also gained the premium membership!
{% endif %}
"""

# message in html (see html file) and plain text are rendered:
html_template = pathlib.Path("email_template.html").read_text(encoding="utf-8")
html_template = Template(html_template)
text_template = Template(text_template)

# load user data
with open("userData.json", "r") as f:
    users = json.load(f)

# send an email for each user:
for user_email, info in users.items():
    firstName, lastName = info.values()

    html = html_template.render(firstName=firstName, premium=True)
    text = text_template.render(firstName=firstName, premium=True)

    message = MIMEMultipart("alternative")
    message["Subject"] = "Your Registration was successful!"
    message["From"] = SENDER_EMAIL
    message["To"] = user_email

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls(context=ssl.create_default_context())
        smtp.ehlo()
        smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
        smtp.sendmail(SENDER_EMAIL, user_email, message.as_string())

