import smtplib
from email.mime.text import MIMEText

user = 'your_account@163.com'
password = 'your_password'
from_addr = 'your_account@163.com'
to_addrs = 'to_account@qq.com'
body = '<p>Liu</p> <p>How are you ?</p>'
msg = MIMEText(body, 'plain', 'utf-8')
msg['subject'] = 'Hello'
msg['from'] = from_addr
msg['to'] = to_addrs

smtp163 = smtplib.SMTP('smtp.163.com', 25)
smtp163.ehlo()
smtp163.starttls()
smtp163.login(user, password)
print(msg.as_string())
smtp163.sendmail(from_addr, to_addrs, msg.as_string())
smtp163.quit()
