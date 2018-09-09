import requests
import itchat

def ro_bot(message):
    apiurl='http://www.tuling123.com/openapi/api'
    data={
    'key' : '//your key',
    'info': message,
    }
    try:
        ro_message=requests.post(apiurl,data=data).json()
        return ro_message.get('text')
    except:
        return 'NULL'

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    message=msg.get('Content')
    reply=ro_bot(message)
    itchat.send(reply,toUserName=msg.fromUserName)

#while(1):
#    message = input("me:")
#    if(message=='0'):
#        break
#    print('bot:'+ro_bot(message))
itchat.auto_login(hotReload=1,enableCmdQR=2)
itchat.run()
