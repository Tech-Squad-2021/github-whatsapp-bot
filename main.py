import os
from twilio.rest import Client

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
to_whatsapp_no = os.environ['to_whatsapp_no']
from_whatsapp_no = os.environ['from_whatsapp_no']

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Code Pushed in main branch of https://github.com/Tech-Squad-2021/github-whatsapp-bot',
                              from_='whatsapp:'+from_whatsapp_no,
                              to='whatsapp:'+to_whatsapp_no
                          )

print("Message ID:",message.sid)
