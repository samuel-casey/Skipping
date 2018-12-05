import poplib
import email
import string, random
from email import parser

# messages = [server.retr(n+1) for n in range(len(server.list()[1]))]
# emails = [email.message_from_string('\n'.join(message[1])) for message in messages]
# print(emails)
# import getpass, poplib

M = poplib.POP3("pop.secureserver.net")
M.user("response2@capacitycenter.com")
M.pass_("Response21")
numMessages = len(M.list()[1])
for i in range(numMessages):
    for j in M.retr(i+1)[1]:
        print(email.message_from_bytes(j))
        