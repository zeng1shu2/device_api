# coding:utf-8
import requests
import urllib3
import xmltodict
import json

# 忽略显示 InsecureRequestWarning: Unverified HTTPS request is being made
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 头部请求携带参数
headers = {'Content-Type': 'application/yang.operation+xml',
           'Authorization': 'Basic YXBpOnpsZ21jdUAxMjM='}


class Access_Authorization:
    """
    ;华为UGS防火墙RESTful接口
    ;适用于V500R001C60SPC500或以下版本。
    ;因ssl套接字原因，高于此版本的将会报错
    """

    def get_text(self, url):
        """请求查询接口"""
        response = requests.request("GET", url, headers=headers, verify=False)
        return response

    def post_text(self, url, j_data):
        """新增接口"""
        response = requests.request("POST", url, body=j_data, headers=headers, verify=False)
        return response.status_code

    def put_text(self, url, j_data):
        """修改接口"""
        response = requests.request("PTU", url, body=j_data, headers=headers, verify=False)
        return response.status_code

    def xml_dict(self, j_data):
        """XML-TO-JSON"""
        str_data = j_data.text
        xmlpare = xmltodict.parse(str_data)
        jsonstr = json.dumps(xmlpare, indent=1)
        dict_str = json.loads(jsonstr)
        return dict_str


