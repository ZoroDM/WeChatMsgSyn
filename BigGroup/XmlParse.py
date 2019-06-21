# xml的解析工作
import json

import xmltodict

# 预处理xml字符串
def xml_pre_handle(string):
    string = string.replace("<br/>", "").replace("&lt;", "<").replace("&gt;", ">")
    return string


# xml转为json
def xml_to_json(xml):
    converted = xmltodict.parse(xml)
    json_str = json.dumps(converted)
    return json_str


# 获取微信名片code，1是微信名片，2是公众号名片
def get_wechat_code(card_type, xml_str):
    pre_handle_str = xml_pre_handle(xml_str)
    json_str = xml_to_json(bytes(pre_handle_str, "UTF-8"))
    json_obj = json.loads(json_str)
    print(json_obj)
    if card_type == 1:
        return json_obj['msg']['@username']
    if card_type == 2:
        return json_obj['msg']['@alias']
