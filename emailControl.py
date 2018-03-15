#! python3
import imapclient
import pyzmail
import smtplib
from email.mime.text import MIMEText
import subprocess
import traceback
import time
import logging
logging.basicConfig(filename='D:\MyPython\Automate\emailControlLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

My_Email = 'from_email@163.com'
Re_Email = 'to_email@qq.com'
Re_Email_PW = 'your_to_email_password'
# Re_Email_PW = input('Re_Email_PW=')
IMAP_Server = 'imap.qq.com'
SMTP_Server = 'smtp.qq.com'
SMTP_Port = 465
subProgram = 'D:\qBittorrent\qbittorrent.exe'


def get_instructions():
    # Login in to the IMAP server
    logging.debug('Connecting to IMAP server at %s' % IMAP_Server)
    imapObj = imapclient.IMAPClient(IMAP_Server)
    imapObj.login(username=Re_Email, password=Re_Email_PW)
    imapObj.select_folder('INBOX')
    logging.debug('Connected')

    # Fetching all instruction emails.
    uids = imapObj.search(['FROM', 'from_email@163.com'])
    rawmessage = imapObj.fetch(uids, ['BODY[]'])
    instructions = []
    for uid in rawmessage.keys():
        message = pyzmail.PyzMessage.factory(rawmessage[uid][b'BODY[]'])
        if message.html_part is not None:
            body = message.html_part.get_payload().decode(message.html_part.charset)
        if message.text_part is not None:
            body = message.text_part.get_payload().decode(message.text_part.charset)
        instructions.append(body)
    logging.debug(instructions)

    if len(uids) > 0:
        imapObj.delete_messages(uids)
        imapObj.expunge()

    imapObj.logout()
    return instructions


def parser_instructions(instruction):
    # Send an email response about the task.
    responseBody =  'Instruction received and completed.\nResponse:\n'

    # Parse the email's body to figure out te instructions.
    lines = instruction.split('\r\n')
    for line in lines:
        if line.startswith('magnet:?'):
            subprocess.Popen(subProgram + ' ' + line)
            responseBody += 'Downloading magnet link\n'

    logging.debug('Connecting to SMTP server at %s' % SMTP_Server)
    msg = MIMEText(responseBody, 'plain', 'utf-8')
    msg['subject'] = 'Response'
    msg['from'] = Re_Email
    msg['to'] = My_Email
    smtpObj = smtplib.SMTP_SSL(SMTP_Server, SMTP_Port)
    smtpObj.ehlo()
    smtpObj.login(Re_Email, Re_Email_PW)
    logging.debug('Connected.')
    smtpObj.sendmail(Re_Email, My_Email, msg.as_string())
    logging.debug('Email Sent')
    smtpObj.quit()

print('Email control started.Press crtl+C to quit.')
logging.debug('Email control started.')
while True:
    logging.debug('Getting instructions from emails.')
    try:
        instructions = get_instructions()
        for instruction in instructions:
            logging.debug('Doing instruction:' + instruction)
            parser_instructions(instruction)
    except Exception as err:
        logging.error(traceback.format_exc())

    logging.debug('Done processing instructions.Pausing for 15 minutes.')
    time.sleep(60*30)
