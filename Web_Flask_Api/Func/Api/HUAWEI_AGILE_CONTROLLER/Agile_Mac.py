# -*- coding: utf-8 -*-
import requests
import urllib3
import json
import sys
sys.path.append('/data/My_App/Web_Flask_Api')
sys.path.append('D:/project/device_api/Web_Flask_Api')


class Evenet_Ac_Dom(object):
    def __init__(self):
        urllib3.disable_warnings()
        self.session = requests.session()

    def hashcode(self):
        req = self.session.get(
            'https://192.168.5.45:8443/OPMUI/jsp/secospace/login.jsp', verify=False, timeout=(5))
        req.encoding = "utf-8"
        hashcode = self.getMiddle(
            req.text, 'type="hidden" value="', '"></input>')
        return hashcode

    def getMiddle(slef, text, left, right):  # 查找函数
        l = text.find(left) + len(left)
        r = text.find(right, l)
        return text[l:r]

    def Login_ac(self):
        code = self.hashcode()
        data = {
            "userName": "api",
            "password": "zlgmcu@789",
            "hashcode": code,
            "validCode": ""
        }
        headers = {
            'Referer': 'https://192.168.5.45:8443/OPMUI/jsp/secospace/login.jsp',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': '192.168.5.45:8443',
            'Connection': 'keep-alive'
        }
        req_login = self.session.post('https://192.168.5.45:8443/OPMUI/business/tsmLogin!login.action',
                                verify=False, data=data, headers=headers, timeout=(5))
        req_login.encoding = "utf-8"
        Token = self.getMiddle(req_login.text, '"data":"', '",')
        cookie = req_login.headers.get(
            'Set-Cookie').split(',')[1].strip('; Path=/OPMUI/; Secure; HttpOnly')
        return Token, cookie

    def Add_mac(self, token, cookie, mac_address, name):
        # 研发设备组ID为238
        data = {
            "groupId": 238,
            "policyname": "",
            "isassignpolicy": 0,
            "isassigngroup": 1,
            "dhcpServerInterfaceTypeVaule": 0,
            "deviceTypeVaule": 0,
            "mac": mac_address,
            "ip": "",
            "vendor": "",
            "osName": "",
            "deviceType": "请选择",
            "hostName": "",
            "policyName": "",
            "assignGroup": "on",
            "description": name,
            "ipAddress": "",
            "port": "",
            "dhcpServerIp": "",
            "dhcpServerInterfaceType": "请选择",
            "dhcpServerInterfaceName": "",
            "policyId": ""
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": ''+cookie+'; Domain=huawei.com; XSRF-TOKEN='+token+'',
            "Host": "192.168.5.45:8443",
            "Referer": "https://192.168.5.45:8443/OPMUI/jsp/secospace/index.jsp?lang=zh_CN",
            "X-Requested-With": "XMLHttpRequest",
            "X-XSRF-TOKEN": token
        }
        res = self.session.post('https://192.168.5.45:8443/OPMUI/secospace/endPointAction!saveEndPoints.action',
                                verify=False, data=data, headers=headers, timeout=(5))
        res.encoding = "utf-8"
        result = json.loads(res.text)
        return result


def Add_Mac(add_mac,name):
    Dom_A = Evenet_Ac_Dom()
    login_token = Dom_A.Login_ac()
    addmac = Dom_A.Add_mac(login_token[0],login_token[1],add_mac,name)
    return addmac


# if __name__ == ('__main__'):
#     mac = '11-11-11-11-11-11'
#     name = 'test'
#     doc = Add_Mac(mac,name)
#     print(doc)
