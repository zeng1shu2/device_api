# -*- coding: utf-8 -*-
import requests
import urllib3
import execjs
import json
import os
import sys
sys.path.append('/data/My_App/Web_Flask_Api')
sys.path.append('D:/project/device_api/Web_Flask_Api')
from Func.Api.SANGFOR_AC_API.rc4passwod import Pass_Cryption


class Check(object):
    def __init__(self) -> None:
        urllib3.disable_warnings()
        self.session = requests.session()

    def check_web(self, web_url):
        try:
            status_code = self.session.get(web_url, verify=False, timeout=(5))
            return status_code.status_code
        except:
            return '网络不可达'  # TODO : 后期写入日志。

    def Checkpath(self, path):
        result = os.path.exists(path)
        return result


class Evenet_Ac_Dom(object):
    def __init__(self, domain):
        urllib3.disable_warnings()
        user_data = {
            "key" : "zlgmcu@123",
            "user": "devlyrS4+w==",
            "pwd" : "buPm+KK/1zMSwA=="
        }
        user = Pass_Cryption(user_data['key'],user_data['user'])
        pwd = Pass_Cryption(user_data['key'],user_data['pwd'])
        self.session = requests.session()
        self.path_conf = './Func/Api/SANGFOR_AC_API'
        self.path_js = './Func/Api/SANGFOR_AC_API/AC.js'
        self.domain = domain
        self.username = user.deCryption()
        self.password = pwd.deCryption()

    def Headers(self):
        """请求头"""
        anticsrf = self.AntiCsrfToken()
        headers = {
            'Content-Type': 'application/json',
            'Referer': 'https://172.16.100.250:25840/index.php',
            'Host': '172.16.100.250:25840',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://172.16.100.250:25840',
            'x-sangfor-anticsrf': ''+anticsrf+''
        }
        return headers

    def js_pass(self):
        """加密密码"""
        with open(self.path_js, encoding='utf-8') as f:
            jsdata = f.read()
        js_pass = execjs.compile(jsdata)
        _js_pass = js_pass.call('do_encrypt', self.password)
        return _js_pass

    def getMiddle(slef, text, left, right):  # 查找函数
        l = text.find(left) + len(left)
        r = text.find(right, l)
        return text[l:r]

    def Login_ac(self):
        js_pass = self.js_pass()
        data = '{"opr": "login","data": {"user": "'+self.username + \
            '","pwd": "'+js_pass+'","privacy_check": "true"}}'
        headers = {
            'Referer': 'https://172.16.100.250:25840/login.html',
            'Content-Type': 'Application/X-www-Form',
            'Host': '172.16.100.250:25840',
            'Connection': 'keep-alive'
        }
        req = self.session.post('https://172.16.100.250:25840/cgi-bin/login.cgi',
                                verify=False, data=data, headers=headers, timeout=(5))
        req.encoding = "utf-8"
        result_req = json.loads(req.text)
        if result_req['success'] is False:
            print('AC登录失败输入的用户或密码错误')
        else:
            return result_req

    def AntiCsrfToken(self):
        result_req = self.session.get(
            'https://172.16.100.250:25840/index.php', verify=False, timeout=(5))
        result_req.encoding = "utf-8"
        anticsrf = self.getMiddle(result_req.text, 'SFAntiCsrfToken = "', '";')
        return anticsrf

    def Sysctl_Config(self):
        """立即生效"""
        data = '{"opr":"status"}'
        headers = self.Headers()
        result_req = self.session.post(
            'https://172.16.100.250:25840/cgi-bin/cfg-status.cgi',
                verify=False, data=data, headers=headers, timeout=(5))
        result_req.encoding = 'utf-8'
        result_req = json.loads(result_req.text)
        return result_req

    def Gain_Url_list(self):
        """获取所有URl组名"""
        data = '{"anode":null,"opr":"list"}'  # 获取URL分类库列表
        headers = self.Headers()
        result_req = self.session.post(
            'https://172.16.100.250:25840/cgi-bin/objurlgrp.cgi',
                verify=False, data=data, headers=headers, timeout=(5))
        result_req.encoding = 'utf-8'
        result_req = json.loads(result_req.text)
        return result_req

    def Gain_Url_value(self, name):
        """获取url组的值"""
        headers = self.Headers()
        data = '{opr: "listItem", "name":"%s"}'%(name)# 获取URL列表
        data = data.encode('utf-8')
        result_req = self.session.post(
            'https://172.16.100.250:25840/cgi-bin/objurlgrp.cgi', verify=False, data=data, headers=headers, timeout=(5))
        result_req.encoding = 'utf-8'
        result_req = json.loads(result_req.text)
        return result_req

    def Update_Url(self,data):
        """更新URL"""
        headers = self.Headers()
        result_req = self.session.post(
            'https://172.16.100.250:25840/cgi-bin/objurlgrp.cgi', verify=False, data=data, headers=headers, timeout=(5))
        result_req.encoding = "utf-8"
        result_req = json.loads(result_req.text)
        return result_req


# if __name__ == ("__main__"):
#     domain = 'www.test1.zlgmcu.com'
#     Ac_Dom = Evenet_Ac_Dom(domain)
#     ss = Ac_Dom.Login_ac()
#     abc11 = Ac_Dom.Gain_Url_value('测试') 
#     print(abc11)
#     url_data = abc11['data']['url']
#     url_data = url_data + '\r\n2222'
#     url_data = url_data + '\r\n3333'
#     # 更新url
#     data = '{"opr":"modify","data":{"id":"","name":"测试","depict":"","url":"'+url_data+'","keyword":""}}'
#     data = data.encode('utf-8')
#     abc12 = Ac_Dom.Update_Url(data)
#     if abc12 ['success'] is True:
#         result = Ac_Dom.Sysctl_Config()
#         print(result)
#         print('成功')

#     else:
#         print('失败')