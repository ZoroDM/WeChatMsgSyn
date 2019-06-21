import XmlParse


# 根据接收到的群消息，重新组合消息内容
def get_return_msg(msg):
    # 储存发送人的群里备注名字
    msg_send_name = msg['ActualNickName'] if 'ActualNickName' in msg.keys() else "未知"

    # 最终形成转发到其他群的消息内容
    msg_content = ''

    ##################################   发送的消息是文本
    if msg['Type'] == 'Text':
        msg_content += "【文本消息】" + msg['Text']

    # 发送的消息是好友推荐，暂时不知道怎么处理
    elif msg['Type'] == 'Friends':
        msg_content += "【好友推荐】" + msg['Text']

    ##################################   发送的消息是名片
    elif msg['Type'] == 'Card':
        # 微信个人名片
        if (msg['RecommendInfo']['VerifyFlag'] == 0):
            msg_content += "【微信名片】" + msg['RecommendInfo']['NickName'] + '，微信号为 ' + XmlParse.get_wechat_code(1, msg[
                'Content'])
        else:
            msg_content += "【公众号名片】" + msg['RecommendInfo']['NickName'] + '，微信号为 ' + XmlParse.get_wechat_code(2, msg[
                'Content'])
    ##################################   发送的消息是位置信息
    elif msg['Type'] == 'Map':
        msg_content += "【位置信息】" + msg['Text'] + "；地图链接" + msg['Url']

    ##################################   分享消息
    elif msg['Type'] == 'Sharing':
        # 分享酷狗音乐
        if (msg['AppMsgType'] == 36):
            msg_content += "【歌曲分享】" + msg['Text']
        # 发送小程序
        elif (msg['AppMsgType'] == 33):
            msg_content += "【小程序分享】" + msg['Text']
        # 发送文章链接
        elif (msg['AppMsgType'] == 5):
            msg_content += "【文章分享】" + msg['Text'] + "；链接" + msg['Url']
        else:
            msg_content += "【未知的分享】"

    ##################################   发送附件
    elif msg['Type'] == "Attachment":
        msg_content += "【附件上传】" + msg['FileName']

    ##################################    发送视频
    elif msg['Type'] == "Video":
        msg_content += "【发送视频】" + msg['FileName']

    ##################################   发送的消息是图片
    elif msg['Type'] == "Picture":
        msg_content += "【发送图片】" + msg['FileName']

    ##################################   发送的消息是语音
    elif msg['Type'] == "Recording":
        msg_content += "【发送语音】" + msg['FileName']

    ##################################   其他未知消息
    else:
        msg_content += "【未知消息】"

    return msg_send_name + "：" + msg_content
