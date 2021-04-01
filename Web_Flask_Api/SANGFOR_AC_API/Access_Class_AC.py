# coding:utf-8
import requests
import json
from SANGFOR_AC_API.Rancom_md5 import Identification


class SangFor(object):
    def __init__(self):
        self.id_str = 1
        id_str = Identification(self.id_str)
        id_str = id_str.md5_code()
        self.params_id = id_str[0]
        self.params_md5 = id_str[1]

    def version_query(self):
        """版本查询"""
        url = 'http://172.16.100.250:9999/v1/status/version'
        params = {'random': self.params_id, 'md5': self.params_md5}
        result_get = requests.get(url, params=params)
        return result_get

    def mac_query(self, value):
        query_url = 'http://172.16.100.250:9999/v1/ipmac-bindinfo'
        params = {'random': self.params_id, 'md5': self.params_md5, 'search': value}
        result_get = requests.get(query_url, params=params)
        return result_get

    def mac_del(self, ip):
        headers = {'Content - Type': 'application / json'}
        delete_url = 'http://172.16.100.250:9999/v1/bindinfo/ipmac-bindinfo?_method=DELETE'
        data = {
            "random": self.params_id,
            "md5": self.params_md5,
            "ip": ip
                }
        result_post = requests.post(delete_url, headers=headers, data=data)
        return result_post

    def mac_add(self, mac, ip):
        headers = {'Content - Type': 'application / json'}
        addr_url = 'http://172.16.100.250:9999/v1/bindinfo/ipmac-bindinfo'
        data = {
            "random": self.params_id,
            "md5": self.params_md5,
            "mac": mac,
            "ip": ip
        }
        result_post = requests.post(addr_url, headers=headers, data=data)
        return result_post


if __name__ == "__main__":
    app = SangFor()
    result_data = app.mac_query('11.11.11.11')
    print(result_data)
#     result_del = app.mac_del('10.10.100.200')
#     print(result_del)
#     result_addr = app.mac_add('00-0c-45-12-3d-12', '10.10.100.201')
#     print(result_addr)