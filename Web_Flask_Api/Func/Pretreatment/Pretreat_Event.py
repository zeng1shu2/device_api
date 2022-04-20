# coding:utf-8

"""预处理执行事件类"""
# 从Web_Flask_Api目录下开始查询包
import sys
import string
sys.path.append('/data/My_App/Web_Flask_Api')
sys.path.append('D:/project/Web_Flask_Api')
from Log import log
from Func.Api.SDC5_API.Access_Class_SDC import Sdc_Access
from Func.Api.HUAWEI_NGFW_R500_R005.Body_Template import *
from Func.Api.HUAWEI_NGFW_R500_R005 import Body_Template
from Func.Api.HUAWEI_NGFW_R500_R005.Access_Class_R005 import Fw_Access
from Func.Pretreatment.WieXin_info import *
from Func.Api.SANGFOR_AC_API.Ac_url_Dom import Evenet_Ac_Dom
from Func.Api.HUAWEI_AGILE_CONTROLLER import Agile_Mac
from random import *
log = log.logs()




class Pretreat_Event(object):
    def __init__(self, get_data):
        self.get_data = get_data

    def Numberpass(self):
        """生成随机8-10位大小写密码"""
        characters = string.ascii_letters +  string.digits
        password = "".join(choice(characters) for x in range(randint(8,10)))
        return password

    def Event_Fw_Port(self):
        """执行防火墙的端口映射"""
        data_info = self.get_data.get(1)
        # 获取需要的端口映射参数
        name = data_info.get("计算机名")
        wan_ip = data_info.get('目的IP地址')
        lan_ip = data_info.get('IP地址')
        port = data_info.get('目的端口号')
        # 传入参数
        body = create_mapping(name, wan_ip, lan_ip, port)
        url = list(body)[0]
        data = list(body)[1]
        object1 = Fw_Access(url)
        result = object1.post_text(data)
        _status = result.status_code
        return _status

    def Event_Fw_Policy(self):
        """执行安全策略放行"""
        data_info = self.get_data.get(1)
        # 获取策略需要的策略参数
        name = data_info.get("计算机名")
        dst_ip = data_info.get("IP地址")
        dst_port = data_info.get("目的端口号")
        stop_time = data_info.get("结束时间")
        # 传入参数
        body = create_policy(name, stop_time, dst_ip, dst_port)
        url = list(body)[0]
        data = list(body)[1]
        object1 = Fw_Access(url)
        result = object1.post_text(data)
        _status = result.status_code
        return _status

    def Event_Fw_create_user(self):
        """创建用户-vpn账号"""
        data_info = self.get_data.get(5)
        passw = self.Numberpass() # 随机密码
        
        #获取创建用户的参数
        name = data_info.get('计算机名')
        dept = data_info.get('VPN用户组')
        time_r = data_info.get('结束时间')
        company = data_info.get('公司名称')
        user_type = data_info.get('VPN_YF')
        # 传入参数
        body = create_user(name, passw, dept, time_r)
        url = list(body)[0]
        data = list(body)[1]
        object1 = Fw_Access(url)
        result = object1.post_text(data.encode('utf-8'))
        _status = result.status_code
        if _status == int(201):
            url = Weixin_url(company)
            url = url.Url_type()
            port = User_Type(user_type)
            port = port.teturn_port()
            # 给新建用户发送账号信息
            info = WeiXin_info(url)
            info.WinXin_Content(name, port, passw)
            return _status
        else:
            return _status
            
    def Event_Fw_Modify(self):
        """vpn用户信息修改"""
        data_info = self.get_data.get(6)
        # 获取修改参数
        name = data_info.get('计算机名')
        time_r = data_info.get('结束时间')
        company = data_info.get('公司名称')
        # 查看用户信息
        url = show_users(name)
        object1 = Fw_Access(url)
        result = object1.get_text()
        j_data = Fw_Access.xlm_to_json(result)
        # 获取到用户信息的组和密码
        try:
            passw = j_data['reply']['data']['user-manage']['vsys']['user'].get('password')
            dept = j_data['reply']['data']['user-manage']['vsys']['user'].get('parent-user-group')
        except:
            # 用户不存在
            log.warning('修改vpn失败,原因是用户存在。')
            return -2
        # 传入参数
        body = modife_user(name, passw, dept, time_r)
        url = list(body)[0]
        data = list(body)[1]
        object1 = Fw_Access(url)
        result = object1.put_text(data.encode('utf-8'))
        _status = result.status_code
        if _status == int(204):
            url = Weixin_url(company)
            url = url.Url_type()
            # 给新建用户发送账号信息
            info = WeiXin_info(url)
            info.WinXin_Content_time(name, time_r)
            return _status
        else:
            return _status

    def Event_Sdc_ChangeUsb(self):
        """执行添加USB权限"""
        data_info = self.get_data.get(2)
        # 获取策略需要的策略参数
        addr_ip = data_info.get("IP地址")
        service = data_info.get("服务名")
        no = Sdc_Access().Sdc_User_info(addr_ip)
        # 传入参数
        object1 = Sdc_Access().Sdc_ChangeUsb(service, no)
        return object1

    def Event_Sdc_ChangeSerial(self):
        """执行添加串口权限"""
        data_info = self.get_data.get(3)
        # 获取策略需要的策略参数
        addr_ip = data_info.get("IP地址")
        process = data_info.get("原始文件名_MD5")
        no = Sdc_Access().Sdc_User_info(addr_ip)
        # 传入参数
        object1 = Sdc_Access().Sdc_ChangeSerial(process, no)
        return object1

    def Event_Sdc_ChangeNet(self):
        """执行添加网络权限"""
        data_info = self.get_data.get(4)
        # 获取策略需要的策略参数
        addr_ip = data_info.get("IP地址")
        dives_ip = data_info.get("设备IP地址")
        process = data_info.get('程序原始文件名_MD5_1')
        no = Sdc_Access().Sdc_User_info(addr_ip)
        # 传入参数
        object1 = Sdc_Access().Sdc_ChangeNet(process=process, no=no, remote=dives_ip)
        return object1
    
    def Event_Sdc_ChangeDesk(self):
        """执行添加托盘程序权限"""
        data_info = self.get_data.get(7)
        # 获取策略需要的策略参数
        addr_ip = data_info.get("IP地址")
        todisk_name = data_info.get("程序名")
        todisk_path = data_info.get("程序绝对路径")
        no = Sdc_Access().Sdc_User_info(addr_ip)
        # 传入参数
        object1 = Sdc_Access().Sdc_ChangeDesk(name=todisk_name, path=todisk_path, no=no)
        return object1

    def Evebt_Ac_ChangeUrl(self):
        """添加URL白名单"""
        data_info = self.get_data.get(8)
        # 获取策略需要的参数
        addr_url = data_info.get('url地址')
        Ac_Dom = Evenet_Ac_Dom(addr_url)
        Ac_Dom_1 = Ac_Dom.Login_ac()
        # 类型，判断是致远还是周立功
        company = data_info.get("公司名称")
        if company in '7893214819773270159':
            zy = Ac_Dom.Gain_Url_value('技术支持无限制的网站')
            url_data = zy['data']['url']
            url_data = url_data + '\r\n%s' % addr_url
            data = '{"opr":"modify","data":{"id":"","name":"技术支持无限制的网站","depict":"","url":"'+url_data+'","keyword":""}}'
            data = data.encode('utf-8')
            zy = Ac_Dom.Update_Url(data)
            if zy ['success'] is True:
                Ac_Dom.Sysctl_Config()
                return 200
            else:
                # 域名创建失败
                return 1001
        elif company in '-8486162257746376183':
            zlg = Ac_Dom.Gain_Url_value('ZLG技术支持')
            url_data = zlg['data']['url']
            url_data = url_data + '\r\n%s' % addr_url
            data = '{"opr":"modify","data":{"id":"","name":"ZLG技术支持","depict":"","url":"'+url_data+'","keyword":""}}'
            data = data.encode('utf-8')
            zlg = Ac_Dom.Update_Url(data)
            if zlg['success'] is True:
                Ac_Dom.Sysctl_Config()
                return 200
            else:
                # 域名创建失败
                return 1001
        else:
            # 公司名称不存在
            log.warning('公司名称不存在')
            return 1000
    
    def Event_AC_ChangeMac(self):
        """添加设备白名单"""
        data_info = self.get_data.get(9)
        # 获取参数
        username = data_info.get('计算机名')
        address_mac = data_info.get('mac地址')
        # 执行传参
        object1 = Agile_Mac.Add_Mac(address_mac, username)
        return object1