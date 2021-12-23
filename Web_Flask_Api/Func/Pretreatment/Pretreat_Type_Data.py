# coding:utf-8
"""处理字段类型"""


import json


class Pretreat_Data(object):
    """初始化Class"""

    def __init__(self, Data):
        self.data = Data

    def Func_Type(self):
        """获取已选择的权限类型"""
        result_list = []
        for data in self.data.items():
            if list(data)[1][0] in "1":
                result_list.append(list(data))
        return result_list

    def VPN_Type(self):
        """获取VPN权限类型"""
        # result_list = []
        # for data in self.data.items():
        #     if list(data)[1][0] in "0" or list(data)[1][0] in "1":
        #         result_list.append(list(data))
        # return result_list
        try:
            vpn_type = self.data.get('VPN权限类型')[0]
            return vpn_type
        except:
            return json.dumps(-1)

    def VPN_Group(self):
        """根据获取的权限类型返回对应的组名称"""
        Number_str = self.data.get('VPN用户组')[0] 
        if Number_str == '0':
            namegroup = '致远电子'
        elif Number_str == '1':
            namegroup = '立功科技'
        elif Number_str == '2':
            namegroup = '研发中心'
        else :
            return json.dumps('用户组不存在')
        return namegroup

    def Func_Type_Value(self):
        """根据获取的权限类型，获取对应的值,返回一个字典"""
        result = self.Func_Type()
        result_dict = {}
        Error = []
        for _data in result:
            if "端口映射权限" in _data[0]:
                result_port = {}
                try:
                    result_port["IP地址"] = self.data.get("IP地址")[0]
                    result_port["结束时间"] = self.data.get("结束时间")[0]
                    if len(self.data.get("目的IP地址")[0]) == 0:
                        Error.append('destination ip address cannot be empty')
                        result_dict[0] = Error
                    else:
                        result_port["目的IP地址"] = self.data.get("目的IP地址")[0]
                except:
                    Error.append('destination ip address not exist')
                    result_dict[0] = Error
                try:
                    if len(self.data.get("目的端口号")[0]) == 0:
                        Error.append('destination port cannot be empty')
                        result_dict[0] = Error
                    else:
                        result_port["目的端口号"] = self.data.get("目的端口号")[0]
                        result_port["计算机名"] = self.data.get(
                            "计算机名")[0] + self.data.get("目的端口号")[0]
                except:
                    Error.append('destination port not exist')
                    result_dict[0] = Error
                result_dict[1] = result_port
            elif "USB通讯权限" in _data[0]:
                result_usb = {}
                try:
                    result_usb["计算机名"] = self.data.get("计算机名")[0]
                    result_usb["IP地址"] = self.data.get("IP地址")[0]
                    if len(self.data.get("服务名")[0]) == 0:
                        Error.append('server cannot be empty')
                        result_dict[0] = Error
                    else:
                        result_usb["服务名"] = self.data.get("服务名")[0]
                except:
                    Error.append('server not exist')
                    result_dict[0] = Error
                result_dict[2] = result_usb
            elif "串口权限" in _data[0]:
                result_serial = {}
                try:
                    result_serial["计算机名"] = self.data.get("计算机名")[0]
                    result_serial["IP地址"] = self.data.get("IP地址")[0]
                    if len(self.data.get("原始文件名_MD5")[0]) == 0:
                        Error.append('original file_MD5 connot be empty')
                        result_dict[0] = Error
                    else:
                        result_serial["原始文件名_MD5"] = self.data.get("原始文件名_MD5")[
                            0]
                except:
                    Error.append('original file_MD5 not exist')
                    result_dict[0] = Error
                result_dict[3] = result_serial
            elif "网络设备_软件权限" in _data[0]:
                result_network = {}
                try:
                    result_network["计算机名"] = self.data.get("计算机名")[0]
                    result_network["IP地址"] = self.data.get("IP地址")[0]
                    if len(self.data.get("设备IP地址")[0]) == 0:
                        Error.append('device ip addresss connot be empty')
                        result_dict[0] = Error
                    else:
                        result_network["设备IP地址"] = self.data.get("设备IP地址")[0]
                except:
                    Error.append('device ip addresss not exist')
                    result_dict[0] = Error
                try:
                    if len(self.data.get("程序原始文件名_MD5_1")[0]) == 0:
                        Error.append('original file_MD5 connot be empty')
                        result_dict[0] = Error
                    else:
                        result_network["程序原始文件名_MD5_1"] = self.data.get("程序原始文件名_MD5_1")[
                            0]
                except:
                    Error.append('original file_MD5 not exist')
                    result_dict[0] = Error
                result_dict[4] = result_network
            elif "托盘程序" in _data[0]:
                result_todisk = {}
                try:
                    result_todisk["计算机名"] = self.data.get("计算机名")[0]
                    result_todisk["IP地址"] = self.data.get("IP地址")[0]
                    if len(self.data.get("程序名")[0]) == 0 :
                        Error.append('appname connot be empty')
                    else:
                        result_todisk['程序名'] = self.data.get('程序名')[0]
                except:
                    Error.append('appname not exist')
                    result_dict[0] = Error
                try:
                    if len(self.data.get("程序绝对路径")[0]) == 0 :
                        Error.append('apppath connit be empty')
                    else:
                        result_todisk["程序绝对路径"] = self.data.get("程序绝对路径")[0]
                except:
                    Error.append('app_path not exist')
                    result_dict[0] = Error
                result_dict[7] = result_todisk
            # elif "VPN账号权限" in _data[0]:
            #     _result = self.VPN_Type()
            #     print(_data)
            #     for _data in _result:
            #         # 0代表新建，1代表续期
            #         if '0' in _data[1]:
            #             result_vpn = {}
            #             result_vpn["公司名称"] = self.data.get("公司名称")[0]
            #             result_vpn["计算机名"] = self.data.get("计算机名")[0]
            #             result_vpn["结束时间"] = self.data.get("结束时间")[0]
            #             result_vpn["申请人"] = self.data.get("申请人")[0]
            #             result_vpn["VPN用户组"] = self.VPN_Group()  # 转换用户组
            #             result_vpn["VPN_YF"] = self.data.get("VPN_YF")[0]
            #             result_dict[5] = result_vpn
            #         elif '1' in _data[1]:
            #             result_vpn = {}
            #             result_vpn["公司名称"] = self.data.get("公司名称")[0]
            #             result_vpn["申请人"] = self.data.get("申请人")[0]
            #             result_vpn["计算机名"] = self.data.get("计算机名")[0]
            #             result_vpn["结束时间"] = self.data.get("结束时间")[0]
            #             result_dict[6] = result_vpn
            elif "VPN账号权限" in _data[0]:
                _result = self.VPN_Type()
                # 0代表新建，1代表续期
                if '0' in _result:
                    result_vpn = {}
                    result_vpn["公司名称"] = self.data.get("公司名称")[0]
                    result_vpn["计算机名"] = self.data.get("计算机名")[0]
                    result_vpn["结束时间"] = self.data.get("结束时间")[0]
                    result_vpn["申请人"] = self.data.get("申请人")[0]
                    result_vpn["VPN用户组"] = self.VPN_Group()  # 转换用户组
                    result_vpn["VPN_YF"] = self.data.get("VPN_YF")[0]
                    result_dict[5] = result_vpn
                elif '1' in _result:
                    result_vpn = {}
                    result_vpn["公司名称"] = self.data.get("公司名称")[0]
                    result_vpn["计算机名"] = self.data.get("计算机名")[0]
                    result_vpn["结束时间"] = self.data.get("结束时间")[0]
                    result_dict[6] = result_vpn
        return result_dict
