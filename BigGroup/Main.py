# import itchat
# import GetReturnMsg
#
# # 生成二维码，扫描登陆
# from itchat.content import *
#
# itchat.login()
#
#
# # 监听所有的群消息，并转发到文件传输助手
# @itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
# def forward(msg):
#     print(msg)
#     return_msg = GetReturnMsg.get_return_msg(msg)
#     itchat.send_msg(return_msg, toUserName='filehelper')
#     # 如果还有附件，再发送一次附件
#     if msg['Type'] == "Attachment" or msg['Type'] == "Video" or msg['Type'] == 'Picture' or msg['Type'] == 'Recording':
#         msg['Text'](msg['FileName'])
#         itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']), 'filehelper')
#         #itchat.send('@%s@%s' % ('fil', msg['FileName']), 'filehelper')
#
# itchat.run()
import itchat
from wxpy import *

# 导入wxpy模块的全部内容
from BigGroup import GroupUtil

bot = Bot()

# 初始化机器人，电脑弹出二维码，用手机微信扫码登陆

bot.groups(update=True, contact_only=False)

# 微信登陆后，更新微信群列表（包括未保存到通讯录的群？？？）

my_groups = []

# for i in range(1, len(my_groups)):
#     my_groups[i].update_group(members_details=True)

# 注册消息响应事件，一旦收到关联群的消息，就执行下面的代码同步消息
@bot.register(Group, except_self=False)
def sync_my_groups(msg):
    print("监听中！！！！！！！1")
    prefix = '【消息同步助手】' + msg.member.name + ':'
    # 给转发的消息加上前缀，显示群成员名字和冒号。群成员名字从备注、群昵称、微信昵称里面按顺序自动获取。
    if(msg.receiver in my_groups):
        sync_message_in_groups(msg, my_groups, prefix=prefix)
    # sync_message_in_groups(msg, my_groups)

@bot.register(bot.file_helper, except_self=False)
def set_groups_key(msg):
    global my_groups
    my_groups_temp = bot.groups().search(msg.text)
    if (len(my_groups_temp) < 2):
        if (len(my_groups) == 0):
            bot.file_helper.send_msg("【消息同步助手】找不到合适数量（2个或以上）的群进行消息同步")
        else:
            bot.file_helper.send_msg("【消息同步助手】找不到合适数量（2个或以上）的群进行消息同步，当前同步群为" + GroupUtil.get_groups_name(my_groups))
    else:
        my_groups = my_groups_temp
        bot.file_helper.send_msg("【消息同步助手】成功同步" + GroupUtil.get_groups_name(my_groups) + "群消息")


bot.join()

# 堵塞线程，让机器人保持运行
