# coding:utf-8

import sys
sys.path.append('/data/My_App/Web_Flask_Api')
sys.path.append('D:/Users/zengshu/Desktop/Web_Flask_Api')
from Func.Api.SDC5_API import config_user
import json
import urllib3
import requests

# 忽略显示 InsecureRequestWarning: Unverified HTTPS request is being made
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Sdc_Api_key(object):
    def __init__(self):
        self.url = config_user._Url_token
        self.data = config_user._User_Info
        self.headers = {"Content-Type": "application/json; charset=utf-8"}

    def Get_key(self):
        key = 'Bearer '
        result_post = requests.post(
            url=self.url, json=self.data, headers=self.headers)
        result = json.loads(result_post.text)
        token = key+result['token']
        return token


class Sdc_Access(object):
    def __init__(self):
        self.headers = {
            "Authorization": "",
            "Content-Type": "application/json; charset=utf-8"
        }
        token = Sdc_Api_key()
        token = token.Get_key()
        self.headers["Authorization"] = token

    def Sdc_Node(self):
        """获取节点信息"""
        url = config_user._Url_Node
        result = requests.post(
            url, json={"nodeType": 32}, headers=self.headers)
        result = json.loads(result.text)
        return result

    def Sdc_DepInfo(self):
        """获取部门信息"""
        url = config_user._Url_Depinfo
        result = requests.post(url=url, headers=self.headers)
        result = json.loads(result.text)
        return result

    def Sdc_User_info(self, addr_ip):
        """获取请求的用户所在的部门，返回一个int"""
        result = self.Sdc_Node()
        result = result.get('data')
        for j_data in result:
            if j_data['NetAddress'] == addr_ip:
                Dept_data = j_data
        Dept_number = Dept_data.get('DepartmentId')
        return Dept_number

    def Sdc_ChangeUsb(self, service, no):
        """添加USB服务权限"""
        url = config_user._Url_ChangeUsb
        config_user._ChangeUsb["service"] = service
        config_user._ChangeUsb["no"] = no
        data = config_user._ChangeUsb
        result = requests.post(url=url, json=data, headers=self.headers)
        return result.status_code

    def Sdc_ChangeSerial(self, process, no):
        """添加串口权限"""
        url = config_user._Url_ChangeSerial
        config_user._ChangeSerial["process"] = process
        config_user._ChangeSerial["no"] = no
        data = config_user._ChangeSerial
        result = requests.post(url=url, json=data, headers=self.headers)
        return result.status_code

    def Sdc_ChangeNet(self, **kwargs):
        """添加网络进程权限"""
        url = config_user._Url_ChangeNet
        if kwargs.get("process") is not None:
            process = kwargs.get("process")
            config_user._ChangeNet["process"] = process
        if kwargs.get("local") is not None:
            local = kwargs.get("local")
            config_user._ChangeNet["local"] = local
        if kwargs.get("remote") is not None:
            remote = kwargs.get("remote")
            config_user._ChangeNet["remote"] = remote
        if kwargs.get("no") is not None:
            no = kwargs.get("no")
            config_user._ChangeNet["no"] = no
        data = config_user._ChangeNet
        result = requests.post(url=url, json=data, headers=self.headers)
        return result.status_code

    def Sdc_ChangeDesk(self,name,path,no):
        """添加托盘权限权限"""
        url = config_user._Url_ChangeTpConfig
        config_user._ChangeTp['name'] = name
        config_user._ChangeTp['path'] = path
        config_user._ChangeTp['no'] = no
        data = config_user._ChangeTp
        result = requests.post(url=url, json=data, headers=self.headers)
        return result.status_code

    # def test(self):
    #     tesdt = {
    #                 "name": "yesy",
    #                 "path": "yest",
    #                 "no": 2,
    #                 "type": 2,
    #                 "systemType": 1,
    #                 "nodeType": 1
    #                 }
    #     url = config_user._Url_ChangeTpConfig
    #     result = requests.post(url=url, json=tesdt, headers=self.headers)
    #     print(result.request.body)
    #     print(result.text)
    #     return result.status_code

# test = Sdc_Access()
# result = test.Sdc_User_info('172.16.33.44')
# print(result)
# resuly = test.Sdc_DepInfo()
# print(resuly)
# result = test.test()
# print(result)

