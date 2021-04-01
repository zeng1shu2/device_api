# coding:utf-8
import requests
import json
from SANGFOR_AC_API.Rancom_md5 import Identification

id_str = Identification('1')
id_str = id_str.md5_code()
params_id = id_str[0]
params_md5 = id_str[1]
print(params_id)
print(params_md5)
#
# headers = {'Content - Type': 'application / json'}
# delete_url = 'http://172.16.100.250:9999/v1/bindinfo/ipmac-bindinfo?_method=DELETE'
# j_data_1 = {
#     "random": "68538",
#     "md5": "f9edee87828bcd0636f2f36bd122eb38",
#     "ip": "111.111.261.22"
# }
# requests1 = requests.request('POST', delete_url, headers=headers, data=j_data_1)
# print(requests1.text)
j_data = '123123'
data = '"random":"{}","md5":"{}","ip":"{}"'.format(
    params_id, params_md5, j_data)

J_data = {
    "random": params_id,
    "md5": None,
    "ip": None
}

print(type(j_data))
print(j_data)