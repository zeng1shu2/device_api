# coding:utf-8

"""状态码信息说明"""


class Info_Status_Code(object):
    def __init__(self, info_code):
        self.info_code = info_code
        self.return_dict = {'Code': False,"Meg":"Nome"}

    def Huawei_Fw_Status_Code(self):
        """ 华为防火墙状态码 """
        if self.info_code == 200:
            status = '请求处理成功。'
            return status
        elif self.info_code == 201:
            status = '创建资源成功。'
            return status
        elif self.info_code == 204:
            status = '调用rpc方法处理成功。'
            return status
        elif self.info_code == -1:
            self.return_dict['Meg'] = '用户不存在。'
            return self.return_dict
        elif self.info_code == 400:
            self.return_dict['Meg'] = '非法的请求。'
            return self.return_dict
        elif self.info_code == 401:
            self.return_dict['Meg'] = '请求认证失败。'
            return self.return_dict
        elif self.info_code == 403:
            status = '资源不存在或无权限操作。'
            return status
        elif self.info_code == 409:
            self.return_dict['Meg'] = '资源被占用,或资源不存在。'
            return self.return_dict
        elif self.info_code == 414:
            self.return_dict['Meg'] = '请求URI长度超出最大长度限制。'
            return self.return_dict
        elif self.info_code == 500:
            self.return_dict['Meg'] = '请求执行失败，但Server未识别出具体原因。'
            return self.return_dict
        elif self.info_code == 501:
            self.return_dict['Meg'] = '未知操作，Server无法执行。'
            return self.return_dict

    def Sdc_Status_Code(self):
        """ 沙盒状态码 """
        if self.info_code == 200:
            status = '请求处理成功。'
            return status
        elif self.info_code == 400:
            self.return_dict['Meg'] = '请求参数错误。'
            return self.return_dict
        elif self.info_code == 401:
            self.return_dict['Meg'] = 'token无效/无权限调用此接口。'
            return self.return_dict
        elif self.info_code == 500:
            self.return_dict['Meg'] = 'Server Error。'
            return self.return_dict

    def Ac_Status_Code(self):
        """sangfor_AC状态码"""
        if self.info_code == 200:
            status = '请求处理成功。'
            return status
        elif self.info_code == 1000:
            self.return_dict['Meg'] = 'Company doesn`t exist'
            return self.return_dict
        elif self.info_code == 1001:
            self.return_dict['Meg'] = 'Domian Creation fail '
            return self.return_dict
        elif self.info_code == 500:
            self.return_dict['Meg'] = 'Server Error。'
            return self.return_dict
    
    def Huawei_Ac_Status_Code(self):
        """huawei_AC状态码"""
        # if self.info_code['success'] == True:
        #     status = '请求处理成功。'
        #     return  status
        if self.info_code == 401:
            self.return_dict['Meg'] = '存在相同MAC的设备。'
            return self.return_dict
        elif self.info_code == 500:
            self.return_dict['Meg'] = 'Server Error。'
            return self.return_dict