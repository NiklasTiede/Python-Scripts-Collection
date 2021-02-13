# Send Emails with Python!

Sending emails can be handy for notifying yourself or other people. In the following 2 scripts are presented which use a mail account to send emails But be aware that you have to go to https://myaccount.google.com/security and let less secure apps access your gmail account (or follow google's docs for using the safer option).

[yagmail script](./notification/email_yagmail.py) | The `notification` folder contains a script that takes advantage of the [yagmail](https://github.com/kootenpv/yagmail) library. It demonstrates how to send a simple notification email to yourself.

[smtp script](./confirmation/email_smtp.py) | The second folder `confirmation` contains a script that generates confirmation emails using the standard library`smtplib`. Multiple emails are send to some user's email addresses. Furthermore, [Jinja2](https://github.com/pallets/jinja) is used to render an HTML template.
