import itchat
import GetReturnMsg

from itchat.content import *

itchat.login()

# 监听所有的群消息，并转发到文件传输助手
@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def forward(msg):
    print(msg)
    return_msg = GetReturnMsg.get_return_msg(msg)
    itchat.send_msg(return_msg, toUserName='filehelper')
    # 如果还有附件，再发送一次附件
    if msg['Type'] == "Attachment" or msg['Type'] == "Video" or msg['Type'] == 'Picture' or msg['Type'] == 'Recording':
        msg['Text'](msg['FileName'])
        itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']), 'filehelper')

itchat.run()