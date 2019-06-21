from wxpy import *
from BigGroup import GroupUtil

# 初始化机器人，电脑弹出二维码，用手机微信扫码登陆
bot = Bot()

# 微信登陆后，更新微信群列表（包括未保存到通讯录的群？？？）
bot.groups(update=True, contact_only=False)

# 需要同步消息的群
my_groups = []

# 注册群消息响应事件，同步群消息
@bot.register(Group, except_self=False)
def sync_my_groups(msg):
    print("有群消息啦 ......")
    prefix = '【消息同步助手】' + msg.member.name + ':'
    # 如果消息来自于关联群，则进行同步
    if msg.receiver in my_groups:
        sync_message_in_groups(msg, my_groups, prefix=prefix)


# 注册文件传输助手消息响应事件，根据发送的文本，查找需要同步的群
@bot.register(bot.file_helper, msg_types=[TEXT], except_self=False)
def set_groups_key(msg):
    global my_groups
    my_groups_temp = bot.groups().search(msg.text)
    if len(my_groups_temp) < 2:
        if len(my_groups) == 0:
            bot.file_helper.send_msg("【消息同步助手】找不到合适数量（2个或以上）的群进行消息同步")
        else:
            bot.file_helper.send_msg("【消息同步助手】找不到合适数量（2个或以上）的群进行消息同步，当前同步群为" + GroupUtil.get_groups_name(my_groups))
    else:
        my_groups = my_groups_temp
        bot.file_helper.send_msg("【消息同步助手】成功同步" + GroupUtil.get_groups_name(my_groups) + "群消息")

# 堵塞线程，让机器人保持运行
bot.join()
