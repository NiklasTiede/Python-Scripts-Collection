
import yagmail

yag = yagmail.SMTP()
contents = [
    "This is the body, and here is just text http://somedomain/image.png",
    "You can find an audio file attached.", '/local/path/to/song.mp3'
]
yag.send('to@someone.com', 'subject', contents)

# Alternatively, with a simple one-liner:
yagmail.SMTP('mygmailusername').send('to@someone.com', 'subject', contents)

##################

import yagmail

receiver = "your@gmail.com"
body = "Hello there from Yagmail"
filename = "document.pdf"

yag = yagmail.SMTP("my@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body,
    attachments=filename,
)
