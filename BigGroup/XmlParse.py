#xml的解析工作
import json

import xmltodict

# 预处理xml字符串
def xml_pre_handle(string):
    string = string.replace("<br/>", "").replace("&lt;","<").replace("&gt;",">")
    return string

# xml转为json
def xml_to_json(xml):
    convertedDict = xmltodict.parse(xml)
    jsonStr = json.dumps(convertedDict)
    return jsonStr

#获取微信名片code，1是微信名片，2是公众号名片
def get_wechat_code(type,str):
    pre_handle_str = xml_pre_handle(str)
    jsonStr = xml_to_json(bytes(pre_handle_str,"UTF-8"))
    jsonObj = json.loads(jsonStr)
    print(jsonObj)
    if(type == 1):
        return jsonObj['msg']['@username']
    if(type == 2):
        return jsonObj['msg']['@alias']



