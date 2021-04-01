# coding:utf-8
import requests
import json
from SANGFOR_AC_API.Rancom_md5 import Identification

id_str = Identification('1')
id_str = id_str.md5_code()
params_id = id_str[0]
params_md5 = id_str[1]
url = 'http://172.16.100.250:9999/v1/status/version'
print(params_id)
print(params_md5)
params = {'random': id_str[0], 'md5': id_str[1]}
result_get = requests.get(url, params=params)
print(result_get.url)
print(result_get.text)