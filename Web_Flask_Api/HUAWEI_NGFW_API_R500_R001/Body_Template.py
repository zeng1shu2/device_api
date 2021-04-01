# coding:utf-8


url_server = 'https://172.16.33.55:9000/restconf/data/huawei-nat-server:nat-server/server-mapping=test1,public'


def create_mapping(name, wan_ip, lan_ip, port):
    """服务器端口映射"""

    body = '<server-mapping>' \
           '<name>%s</name>' \
           '<vsys>public</vsys>' \
           '<global-zone>untrust</global-zone>' \
           '<protocol>6</protocol>' \
           '<global>' \
           '<start-ip>%s</start-ip>' \
           '</global>' \
           '<global-port>' \
           '<start-port>%s</start-port>' \
           '</global-port>' \
           '<inside>' \
           '<start-ip>%s</start-ip>' \
           '</inside>' \
           '<inside-port>' \
           '<start-port>%s</start-port>' \
           '</inside-port>' \
           '<no-reverse>true</no-reverse>' \
           '</server-mapping>' % (name, wan_ip, port, lan_ip, port)
    return body


def del_mapping(name):
    """删除"""
    url_server_del = 'https://172.16.33.55:9000/restconf/data/huawei-nat-server:nat-server/server-mapping={},public' \
        .format(name)
    return url_server_del
