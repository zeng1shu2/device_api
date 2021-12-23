# coding:utf-8
from flask import Flask, request
from Func.Pretreatment.Pretreat_Type_Data import Pretreat_Data
from Func.Pretreatment.Pretreat_Event import Pretreat_Event
from Func.Pretreatment.Pretreat_Status import Info_Status_Code
from Error.Error_Class import Type_Value_Error
import json


app = Flask(__name__)


# 接口测试
@app.route('/api/test', methods=['GET'])
def ng_test():
    return_dict = json.dumps('OK')
    return return_dict


# 解决跨域访问问题
@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ


@app.route('/api/<path:rule_name>', methods=['POST', 'PUT'])
def ng_port(rule_name):
    return_dict = {'Code': False}
    if (rule_name == "policy"
        or rule_name == "policy/Users"
        or rule_name == "policy/UserModif"
        or rule_name == "policy/ChangeUsbPolicy"
        or rule_name == "policy/ChangeSerialCtrlPolicy"
        or rule_name == "policy/ChangeNetWorkRequest"
        or rule_name == "policy/ChangeChangeDesk"):
        # 获取传入的参数
        try:
            get_data = request.get_json()
            # print(get_data)
        except:
            ValueError = Type_Value_Error.Parameter_Error('请求的参数错误')
            return ValueError, 400
        if get_data is None or not bool(get_data):
            ValueError = Type_Value_Error.Parameter_Error('请求的数据不能为空')
            return ValueError, 400
        else:
            # 获取权限类型
            permission = Pretreat_Data(get_data)
            permission = permission.Func_Type_Value()
            # 判断类型是否有错误如果有则返回错误原因
            if 0 in permission:
                ValueError = Type_Value_Error(permission)
                ValueError = ValueError.Value_Error()
                # 返回错误类型
                return ValueError, 400
            permission_type = list(permission.keys())
            # 判断获取的类型是否存在
            if len(permission_type) >= 1:
                # 判断权限类型是否为多类型
                if len(permission_type) >= 2:
                    # 执行多权限处理并返回执行的结果
                    status_code_type = []
                    for i in permission_type:
                        # 根据对应的权限进行业务处理并将返回码加到列表里
                        if i == 1:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Fw_Port()
                            status_code_type.append(_status)
                            if _status == int(201):
                                #: 新建成功后创建对应的策略
                                _policy = event.Event_Fw_Policy()
                                if _policy == int(201):
                                    continue
                            else:
                                status_code_type.append(_status)
                                # 如果端口映射失败将不在继续执行其他权限
                                return_code = Info_Status_Code(_status)
                                return_dict = return_code.Huawei_Fw_Status_Code()
                                return_dict['Code'] = _status
                                return return_dict, 400
                        elif i == 2:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Sdc_ChangeUsb()
                            status_code_type.append(_status)
                            if _status == int(200):
                                continue
                            else:
                                status_code_type.append(_status)
                                return_code = Info_Status_Code(_status)
                                return_dict = return_code.Sdc_Status_Code()
                                return_dict['Code'] = _status
                                return return_dict, 400
                        elif i == 3:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Sdc_ChangeSerial()
                            status_code_type.append(_status)
                            if _status == int(200):
                                continue
                            else:
                                status_code_type.append(_status)
                                return_code = Info_Status_Code(_status)
                                return_dict = return_code.Sdc_Status_Code()
                                return_dict['Code'] = _status
                                return return_dict, 400
                        elif i == 4:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Sdc_ChangeNet()
                            status_code_type.append(_status)
                            if _status == int(200):
                                continue
                            else:
                                status_code_type.append(_status)
                                return_code = Info_Status_Code(_status)
                                return_dict = return_code.Sdc_Status_Code()
                                return_dict['Code'] = _status
                                return return_dict, 400
                        elif i == 5:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Fw_create_user()
                            status_code_type.append(_status)
                            if _status == int(201):
                                continue
                            else:
                                status_code_type.append(_status)
                                return_code = Info_Status_Code(
                                    list(_status)[0])
                                return_dict = return_code.Huawei_Fw_Status_Code()
                                return_dict['Code'] = list(_status)[0]
                                return return_dict, 400
                        elif i == 6:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Fw_Modify()
                            status_code_type.append(_status)
                            if _status == int(204):
                                continue
                            else:
                                status_code_type.append(_status)
                                return_code = Info_Status_Code(_status)
                                return_dict = return_code.Huawei_Fw_Status_Code()
                                return_dict['Code'] = _status
                                return return_dict, 400
                        elif i == 7:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Sdc_ChangeDesk()
                            status_code_type.append(_status)
                            if _status == int(200):
                                continue
                            else:
                                status_code_type.append(_status)
                                return_code = Info_Status_Code(_status)
                                return_dict = return_code.Sdc_Status_Code()
                                return_dict['Code'] = _status
                                return return_dict, 400
                    return json.dumps('OK')
                else:
                    # 执行单一权限处理并返回结果
                    for i in permission_type:
                        # 根据对应的权限进行业务处理
                        if i == 1:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Fw_Port()
                            if _status == int(201):
                                #: 新建成功后创建对应的策略
                                _policy = event.Event_Fw_Policy()
                                if _policy == int(201):
                                    continue
                            else:
                                return_code = Info_Status_Code(_status)
                                return_dict = return_code.Huawei_Fw_Status_Code()
                                return_dict['Code'] = _status
                                return return_dict, 400
                        elif i == 2:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Sdc_ChangeUsb()
                            if _status == int(200):
                                continue
                            else:
                                return_dict['Code'] = _status
                                return_code = Info_Status_Code(_status)
                                return_code = return_code.Sdc_Status_Code()
                                result_s = json.dumps(return_code)
                                return result_s, 400
                        elif i == 3:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Sdc_ChangeSerial()
                            if _status == int(200):
                                continue
                            else:
                                return_dict['Code'] = _status
                                return_code = Info_Status_Code(_status)
                                return_code = return_code.Sdc_Status_Code()
                                result_s = json.dumps(return_code)
                                return result_s, 400
                        elif i == 4:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Sdc_ChangeNet()
                            if _status == int(200):
                                continue
                            else:
                                return_dict['Code'] = _status
                                return_code = Info_Status_Code(_status)
                                return_code = return_code.Sdc_Status_Code()
                                result_s = json.dumps(return_code)
                                return result_s, 400
                        elif i == 5:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Fw_create_user()
                            if _status == int(201):
                                continue
                            else:
                                return_code = Info_Status_Code(_status)
                                return_dict = return_code.Huawei_Fw_Status_Code()
                                return_dict['Code'] = _status
                                return return_dict, 400
                        elif i == 6:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Fw_Modify()
                            if _status == int(204):
                                continue
                            else:
                                return_code = Info_Status_Code(_status)
                                return_dict = return_code.Huawei_Fw_Status_Code()
                                return_dict['Code'] = _status
                                return return_dict, 400
                        elif i == 7:
                            event = Pretreat_Event(permission)
                            _status = event.Event_Sdc_ChangeDesk()
                            if _status == int(200):
                                continue
                            else:
                                return_code = Info_Status_Code(_status)
                                return_dict = return_code.Sdc_Status_Code()
                                return_dict['Code'] = _status
                                return return_dict, 400
                    return json.dumps('OK')
            else:
                return json.dumps('OK')
    else:
        # 返回一个请求错误
        ValueError = Type_Value_Error.Parameter_Error('url错误，url地址不存在')
        return ValueError, 400


if __name__ == '__main__':
    app.run()
