# coding:utf-8
from requests.api import post
import urllib3
import json
# 忽略显示 InsecureRequestWarning: Unverified HTTPS request is being made
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Weixin_url(object):
    """根据公司返回一个url"""
    def __init__(self, company):
        self.company=company

    def Url_type(self):
        if self.company == '7893214819773270159':
            return 'https://apiw.zlgmcu.com/restcloud/rest/wxwork/zy_system/send_message'
        elif self.company == '-8486162257746376183':
            return 'https://apiw.zlgmcu.com/restcloud/rest/wxwork/zlg_system/send_message'
        else:
            return json.dumps('on').encode('utf-8')

class User_Type(object):
    """根据用户类型返回对应的端口号，0=true, 1= false"""
    def __init__(self, user_type, company):
        self.user_type = user_type
        self.company = company 
    def teturn_port(self):
        if self.user_type == '1' and self.company == '7893214819773270159':
            return int(8440)
        elif self.user_type == '1' and self.company == '-8486162257746376183':
            return int(9880)
        elif self.user_type == '0':
            return int(33001)
            
            
class WeiXin_info(object):
    """发送账号信息"""
    def __init__(self, url):
        self.url = url
        self.headers = {"content-type": "application/json"}

    def WinXin_Content(self, uname, port, password):
        s_data = {}
        uname = uname
        s_data['touser'] = uname
        s_data['msgtype'] = 'text'
        s_data['text'] = {}
        s_data['text']['content'] = (
            '请注意查收您的VPN信息:\nVPN服务器地址: 121.33.243.38\n端口: %s\n用户名: %s\n密码: %s\n温馨提示，这些信息涉及公司商业秘密，请注意保密。' \
                % (port, uname, password))
        post(url=self.url, json=s_data,headers=self.headers, verify=False)

    def WinXin_Content_time(self, uname, teme_r):
        s_data = {}
        uname = uname
        s_data['touser'] = uname
        s_data['msgtype'] = 'text'
        s_data['text'] = {}
        s_data['text']['content'] = '您的VPN账户已修改:\n使用权限延长至 %s 23:59:59。' % teme_r
        post(url=self.url, json=s_data,headers=self.headers, verify=False)

    def WinXin_Content_pass(self, uname, password):
        s_data = {}
        uname = uname
        s_data['touser'] = uname
        s_data['msgtype'] = 'text'
        s_data['text'] = {}
        s_data['text']['content'] = '您的VPN账户密码已重置为:%s ' % password
        post(url=self.url, json=s_data,headers=self.headers, verify=False)
