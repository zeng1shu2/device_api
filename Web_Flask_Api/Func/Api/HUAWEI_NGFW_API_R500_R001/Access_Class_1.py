# coding:utf-8
import requests
import urllib3
import xmltodict
import json

# 忽略显示 InsecureRequestWarning: Unverified HTTPS request is being made
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Fw_Access(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'Content-Type': 'application/yang.operation+xml',
                        'Authorization': 'Basic YXBpOnpsZ21jdUAxMjM='}

    def get_text(self):
        """请求查询接口"""
        response = requests.request("GET", self.url, headers=self.headers, verify=False)
        return response

    def post_text(self, j_data):
        """新增信息"""
        response = requests.post(self.url, data=j_data, headers=self.headers, verify=False)
        return response

    def put_text(self, j_data):
        """修改系统"""
        response = requests.request('PUT', self.url, headers=self.headers, body=j_data)
        return response

    def del_text(self):
        """删除信息"""
        pass

    def xlm_to_json(self, j_data):
        """信息转换"""
        str_data = j_data.text
        xmlpare = xmltodict.parse(str_data)
        json_str = json.dumps(xmlpare, indent=1)
        dict_str = json.loads(json_str)
        return dict_str

