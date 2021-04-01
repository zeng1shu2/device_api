# coding:utf-8

# 生成随机的random值
import random

result = random.randint(333333, 99999999)
result_str = str(result)
# 生成前端密钥与random的MD5值
import hashlib

password_str = '1'
value_tuple = password_str, result_str
value_str = ''.join(value_tuple)
print(value_str)


def md5Encode(str):
    # 参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误
    m = hashlib.md5(str.encode(encoding='utf-8'))
    return m.hexdigest()


result = md5Encode(value_str)