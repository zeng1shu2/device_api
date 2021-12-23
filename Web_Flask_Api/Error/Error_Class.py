# coding:utf-8


class Type_Value_Error(object):
    """处理报错的返回值"""
    def __init__(self, data):
        self.data = data
    
    def Value_Error(self):
        # 值错误或为空
        return_dict = {'Code': 400}
        result = list(self.data.values())[0]
        return_dict['ErrorMas']=result
        return return_dict
        
    @staticmethod
    def Parameter_Error(data):
        # 请求参数错误
        return_dict = {'Code': 400}
        return_dict['ErrorMas'] = data
        return return_dict
