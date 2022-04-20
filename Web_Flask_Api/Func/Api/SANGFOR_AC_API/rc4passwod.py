import sys
sys.path.append('/data/My_App/Web_Flask_Api')
sys.path.append('D:/project/device_api/Web_Flask_Api')
from Crypto.Cipher import ARC4 as rc4cipher
import base64



class Pass_Cryption(object):
    def __init__(self, key,data) -> None:
        self.key = bytes(key,encoding='utf-8')
        self.data = data

    def enCryption(self):
        """加密密码"""
        enc = rc4cipher.new(self.key)
        result_res = enc.encrypt(self.data.encode('utf-8'))
        result_res = base64.b64encode(result_res)
        res = str(result_res, 'utf8')
        return res
    
    def deCryption(self):
        """解密密码"""
        result_res = base64.b64decode(self.data)
        enc = rc4cipher.new(self.key)
        result_res = enc.decrypt(result_res)
        res = str(result_res, 'utf8')
        return res


