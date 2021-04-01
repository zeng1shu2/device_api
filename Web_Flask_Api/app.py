# coding:utf-8

from flask import Flask, request
from HUAWEI_NGFW_R500_R005.Access_Class_R005 import Fw_Access
from HUAWEI_NGFW_R500_R005 import Body_Template
from HUAWEI_NGFW_R500_R005.Body_Template import *
from SANGFOR_AC_API.Access_Class_AC import SangFor
from flask_basicauth import BasicAuth
import json

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'zlg'
app.config['BASIC_AUTH_PASSWORD'] = 'zlgmcu@123'
auth = BasicAuth(app)


class UrlError(Exception):
    def __init__(self, message):
        self.message = message


@app.route('/api/Fw/nat/<rule_name>', methods=['POST'])
@auth.required
def ng_port(rule_name):
    if rule_name == 'add_port':
        # 默认返回
        return_dict = {'Code': False, 'Message': False}
        # 获取传入的参数
        get_data = request.get_data()
        # 转换为JSon
        get_data = json.loads(get_data)
        name = get_data.get('name')
        wan_ip = get_data.get('wan_ip')
        lan_ip = get_data.get('lan_ip')
        port = get_data.get('port')
        # 处理传参
        url = url_create
        body = create_mapping(name, wan_ip, lan_ip, port)
        object1 = Fw_Access(url)
        result = object1.post_text(body)
        return_dict['Code'] = result.status_code
        return_dict['Message'] = status_code(result.status_code)
        return json.dumps(return_dict, ensure_ascii=False)
    elif rule_name == 'del_port':
        return_dict = {'Code': False, 'Message': False}
        get_data = request.get_data()
        get_data = json.loads(get_data)
        name = get_data.get('name')
        name_url = del_mapping(name)
        object1 = Fw_Access(name_url)
        result = object1.del_text()
        return_dict['Code'] = result.status_code
        return_dict['Message'] = status_code(result.status_code)
        return json.dumps(return_dict, ensure_ascii=False)
    else:
        raise UrlError('url错误，url地址不存在')


@app.route('/api/Fw/policy/<rule_name>', methods=['POST'])
@auth.required
def ng_policy(rule_name):
    if rule_name == 'rule_add':
        return_dict = {'Code': False, 'Message': False}
        get_data = request.get_data()
        get_data = json.loads(get_data)
        name = get_data.get('name')
        src_zone = get_data.get('src_zone')
        dst_zone = get_data.get('dst_zone')
        src_ip = get_data.get('src_ip')
        dst_ip = get_data.get('dst_ip')
        dst_port = get_data.get('dst_port')
        j_data = create_policy(name, src_zone, dst_zone, src_ip, dst_ip, dst_port)
        url_add = Body_Template.url_add_policy
        object1 = Fw_Access(url_add)
        result = object1.post_text(j_data)
        return_dict['Code'] = result.status_code
        return_dict['Message'] = status_code(result.status_code)
        return json.dumps(return_dict, ensure_ascii=False)
    elif rule_name == 'rule_del':
        return_dict = {'Code': False, 'Message': False}
        get_data = request.get_data()
        get_data = json.loads(get_data)
        name = get_data.get('name')
        name_url = del_policy(name)
        object1 = Fw_Access(name_url)
        result = object1.del_text()
        return_dict['Code'] = result.status_code
        return_dict['Message'] = status_code(result.status_code)
        return json.dumps(return_dict, ensure_ascii=False)
    else:
        raise UrlError('url错误，url地址不存在')


@app.route('/api/Ac/mac/<rule_name>', methods=['POST'])
@auth.required
def ac_controller(rule_name):
    if rule_name == 'add_mac':
        get_data = request.get_data()
        get_data = json.loads(get_data)
        mac_value = get_data.get('mac')
        ip_value = get_data.get('ip')
        object1 = SangFor()
        result = object1.mac_add(mac_value, ip_value)
        return result.text
    elif rule_name == 'del_mac':
        get_data = request.get_data()
        get_data = json.loads(get_data)
        ip_value = get_data.get('ip')
        object1 = SangFor()
        result = object1.mac_del(ip_value)
        return result.text
    elif rule_name == 'search':
        get_data = request.get_data()
        get_data = json.loads(get_data)
        values = get_data.get('values')
        object1 = SangFor()
        result = object1.mac_query(values)
        return result.text
    else:
        raise UrlError('url错误，url地址不存在')


def status_code(status):
    if status == 200:
        status = '请求处理成功。'
        return status
    elif status == 201:
        status = '创建资源成功。'
        return status
    elif status == 204:
        status = '调用rpc方法处理成功。'
        return status
    elif status == 400:
        status = '非法的请求。'
        return status
    elif status == 401:
        status = '请求认证失败。'
        return status
    elif status == 403:
        status = '资源不存在或无权限操作。'
        return status
    elif status == 409:
        status = '资源被占用,或资源不存在。'
        return status
    elif status == 414:
        status = '请求URI长度超出最大长度限制。'
        return status
    elif status == 500:
        status = '请求执行失败，但Server未识别出具体原因。'
        return status
    elif status == 501:
        status = '未知操作，Server无法执行。'
        return status


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
