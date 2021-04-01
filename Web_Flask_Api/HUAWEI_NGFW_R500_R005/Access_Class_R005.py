# coding:utf-8
import requests
import urllib3
import xmltodict
import json
import ssl
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

# 忽略显示 InsecureRequestWarning: Unverified HTTPS request is being made
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Ssl1_2HttpAdapter(HTTPAdapter):
    """"Transport adapter" that allows us to use SSLv1.2"""

    def init_poolmanager(self, connections, maxsize, block=False, **pool_kwargs):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1_2)


class Fw_Access(object):
    """
    ;华为UGS防火墙RESTful接口
    ;适用于V500R005C20SPC500或以上版本。
    """
    s = requests.Session()
    s.mount('https://', Ssl1_2HttpAdapter())

    # s.verify = False

    def __init__(self, url):
        self.url = url
        self.headers = {'Authorization': 'Basic YXBpOnpsZ21jdUAxMjM='}

    def get_text(self):
        """请求查询接口"""
        result_get = Fw_Access.s.get(self.url, headers=self.headers, verify=False)
        return result_get

    def post_text(self, j_data):
        """新增信息"""
        response = Fw_Access.s.post(self.url, data=j_data, headers=self.headers, verify=False)
        return response

    def put_text(self, j_data):
        """修改系统"""
        response = Fw_Access.s.put(self.url, headers=self.headers, body=j_data, verify=False)
        return response

    def del_text(self):
        """删除信息"""
        response = Fw_Access.s.delete(self.url, headers=self.headers, verify=False)
        return response

    @staticmethod
    def xlm_to_json(j_data):
        """信息转换"""
        str_data = j_data.text
        xmlpare = xmltodict.parse(str_data)
        json_str = json.dumps(xmlpare, indent=1)
        dict_str = json.loads(json_str)
        return dict_str

    @staticmethod
    def json_to_xlm(j_data):
        """信息转换xlm"""
        xml_str = xmltodict.unparse(j_data, pretty=1)
        return xml_str


# if __name__ == '__main__':
#     data = {"rule": {"addr-object": {"elements": {"elem-id": "0", "address-ipv4": "192.168.100.0/24"}}}
#             }
#
#     result = Fw_Access.json_to_xlm(data)
#     print(result)
