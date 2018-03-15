import imapclient
import pyzmail
import pprint
import os

user = 'your_email_account@qq.com'
password = 'your_password'
imapObj = imapclient.IMAPClient('imap.qq.com')
imapObj.login(username=user, password=password)
pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['FROM', 'lmac0603@163.com'])
print(UIDs)
rawmessage = imapObj.fetch(UIDs[0], ['BODY[]'])
message = pyzmail.PyzMessage.factory(rawmessage[UIDs[0]][b'BODY[]'])
print(message.get_subject())
if message.text_part != None:
    text = message.text_part.get_payload().decode(message.text_part.charset)
    print(text)
html = message.html_part.get_payload().decode(message.html_part.charset)
with open('emailHtml.html', 'w', encoding='utf-8') as file:
    file.write('<meta charset="utf-8">\n'+ html)
    file.close()
imapObj.logout()
