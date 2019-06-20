import smtplib
import string
import traceback
import sys

fromaddr = 'drew@wellthoughts.org'
password = 'Paulrevere31!'
toaddrs  = 'appiispanen@gmail.com'
server_smtp = 'wellthoughts.org'
port_smtp = 465

msg = 'Test message ^^'
BODY = "From: %s To: %s Subject: %s Hello!!! What\'s up? %s :) \r\n".format(fromaddr,toaddrs,msg)

try :
    server = smtplib.SMTP_SSL(host=server_smtp, port=port_smtp)
    server.set_debuglevel(True)
    server.esmtp_features['auth'] = 'LOGIN PLAIN'
    server.login('bbrown', password)
    server.sendmail(fromaddr, toaddrs, str(BODY))
    server.quit()
except :
    raise