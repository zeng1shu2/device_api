# coding:utf-8

# 全局url地址
url_check = 'https://172.16.100.253:9999/restconf/data/huawei-nat-server:nat-server'
url_add_policy = 'https://172.16.100.253:9999/restconf/data/huawei-security-policy:sec-policy/vsys=public/static-policy' \
                 '/rule= '


def create_mapping(name, wan_ip, lan_ip, port):
    """NG Firewall Create Port Mapping"""
    url_create = f'https://172.16.100.253:9999/restconf/data/huawei-nat-server:nat-server/server-mapping={str(name)},public'
    body = '<server-mapping>' \
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
           '</server-mapping>' % (wan_ip, port, lan_ip, port)
    # body = {
    #     'server-mapping': {
    #         'protocol': 6,
    #         'global': {
    #             'start-ip': '%s'
    #         },
    #         'global-port': {
    #             'start-port': '%s'
    #         },
    #         'inside': {
    #             'start-ip': '%s'
    #         },
    #         'inside-port': {
    #             'start-port': '%s'
    #         },
    #         'no-reverse': 'true'
    #     }
    # }
    # body = '<server-mapping>' \
    #        '<name>%s</name>' \
    #        '<vsys>public</vsys>' \
    #        '<global-zone>untrust</global-zone>' \
    #        '<protocol>6</protocol>' \
    #        '<global>' \
    #        '<start-ip>%s</start-ip>' \
    #        '</global>' \
    #        '<global-port>' \
    #        '<start-port>%s</start-port>' \
    #        '</global-port>' \
    #        '<inside>' \
    #        '<start-ip>%s</start-ip>' \
    #        '</inside>' \
    #        '<inside-port>' \
    #        '<start-port>%s</start-port>' \
    #        '</inside-port>' \
    #        '<no-reverse>true</no-reverse>' \
    #        '</server-mapping>' % (name, wan_ip, port, lan_ip, port)
    return url_create, body


def del_mapping(name):
    """NG Firewall Del Port Mapping"""
    url_server_del = 'https://172.16.100.253:9000/restconf/data/huawei-nat-server:nat-server/server-mapping={},public' \
        .format(name)
    return url_server_del


def create_policy(name, src_zone, dst_zone, src_ip, dst_ip, dst_port):
    global url_add_policy
    url_add_policy = f'https://172.16.100.253:9000/restconf/data/huawei-security-policy:sec-policy/vsys=public' \
                     f'/static-policy/rule={name}'
    body = "<rule>" \
           f"<desc>{name}</desc>" \
           f"<source-zone>{src_zone}</source-zone> " \
           f"<destination-zone>{dst_zone}</destination-zone>" \
           "<source-ip> " \
           f"<address-ipv4>{src_ip}</address-ipv4>" \
           "</source-ip> " \
           "<destination-ip>" \
           f"<address-ipv4>{dst_ip}</address-ipv4>" \
           "</destination-ip>" \
           "<service> " \
           "<service-items>" \
           "<tcp>" \
           "<source-port>100 200 to 300 600</source-port>" \
           f"<dest-port>{dst_port}</dest-port>" \
           "</tcp>" \
           "</service-items>" \
           "</service>" \
           "<action>true</action>" \
           "</rule> "
    return body


def del_policy(name):
    """NG Firewall Del Port Mapping"""
    url_policy_del = f'https://172.16.100.253:9000/restconf/data/huawei-security-policy:sec-policy/vsys=public/static' \
                     f'-policy/rule={name} '
    return url_policy_del


def create_address(name, **kwargs):
    url_add_addrs = f'https://172.16.33.55:9000/restconf/data/huawei-address-set:address-set/addr-object=public,{name}'
    return url_add_addrs
