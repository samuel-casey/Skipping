import smtplib
import string
import traceback
import sys


def send_email (to_address, subject, message_content):
    fromaddr = 'Drew@Wellthoughts.org'
    password = 'Jacrew31!'
    toaddrs = to_address

    server_smtp = 'wellthoughts.org'
    port_smtp = 465

    SUBJECT = subject
    message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n%s""" % (fromaddr, toaddrs, SUBJECT, message_content)

    print(message)

    message=message.encode('utf8')

    try :
        server = smtplib.SMTP_SSL(host=server_smtp, port=port_smtp)
        server.set_debuglevel(True)
        server.esmtp_features['auth'] = 'LOGIN PLAIN'
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, message)
        server.quit()
    except :
        server.quit()
        raise


