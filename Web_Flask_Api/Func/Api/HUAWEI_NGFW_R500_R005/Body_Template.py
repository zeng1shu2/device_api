
# coding:utf-8

# 全局url地址
url_check = 'https://172.16.100.253:9999/restconf/data/huawei-nat-server:nat-server'
url_add_policy = 'https://172.16.100.253:9999/restconf/data/huawei-security-policy:sec-policy/vsys=public/static-policy' \
                 '/rule= '

# 创建端口映射
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
    return url_create, body

# 删除端口映射
def del_mapping(name):
    """NG Firewall Del Port Mapping"""
    url_server_del = 'https://172.16.100.253:9999/restconf/data/huawei-nat-server:nat-server/server-mapping={},public' \
        .format(name)
    return url_server_del

# 创建安全策略
def create_policy(name, stop_time , dst_ip, dst_port):
    url_add_policy = f'https://172.16.100.253:9999/restconf/data/huawei-security-policy:sec-policy/vsys=public' \
                     f'/static-policy/rule={str(name)}'
    body = "<rule>" \
        "<desc>%s</desc>" \
        "<parent-group>Manp_Port</parent-group>" \
        "<source-zone>untrust</source-zone>" \
        "<destination-zone>trust</destination-zone>" \
        "<destination-ip>" \
        "<address-ipv4>%s/32</address-ipv4>" \
        "</destination-ip>" \
        "<service>" \
        "<service-items>" \
        "<tcp>" \
        "<source-port>0 to 65535</source-port>" \
        "<dest-port>%s</dest-port>" \
        "</tcp>" \
        "</service-items>" \
        "</service>" \
        "<policy-log>true</policy-log>" \
        "<session-log>true</session-log>" \
        "<enable>true</enable>" \
        "<action>true</action>" \
        "</rule>" % (stop_time, dst_ip, dst_port)
    return url_add_policy, body

# 删除安全策略
def del_policy(name):
    """NG Firewall Del Port Mapping"""
    url_policy_del = f'https://172.16.100.253:9999/restconf/data/huawei-security-policy:sec-policy/vsys=public/static' \
                     f'-policy/rule={name} '
    return url_policy_del

# 创建地址
def create_address(name, **kwargs):
    url_add_addrs = f'https://172.16.100.253:9999/restconf/data/huawei-address-set:address-set/addr-object=public,{name}'
    return url_add_addrs

# 查看安全策略
def show_policy(name):
    url_add_policy = f'https://172.16.100.253:9999/restconf/data/huawei-security-policy:sec-policy/vsys=public/static-policy/rule={name}'
    return url_add_policy

# 查看用户
def show_users(name):
    url_show_user = f'https://172.16.100.240:9999/restconf/data/huawei-user-management-fw:user-manage/vsys=public/user={str(name)},default'
    return url_show_user

# 创建用户
def create_user(name,passw,dept,time_r):
    url_add_create_user = f'https://172.16.100.240:9999/restconf/data/huawei-user-management-fw:user-manage/vsys=public/user={str(name)},default'
    body = '<user>' \
           '<alias>%s</alias>' \
           '<password>$0$%s</password>' \
           '<parent-user-group>/default/%s</parent-user-group>' \
           '<expiration-time>' \
           '<expiration-time>%sT23:59:59Z</expiration-time>' \
           '</expiration-time>' \
           '<login-attribute>' \
           '<multi-ip-online>false</multi-ip-online>' \
           '</login-attribute>' \
           '<ip-mac-binding>'\
           '<no-binding/>' \
           '</ip-mac-binding>' \
           '<enabled>true</enabled>' \
           '</user>' % (name,passw,dept,time_r)
    return url_add_create_user, body

# 修改用户时间
def modife_user(name,passw,dept,time_r):
    """修改用户时间"""
    url_modif_user = f'https://172.16.100.240:9999/restconf/data/huawei-user-management-fw:user-manage/vsys=public/user={str(name)},default'
    body =  '<user>' \
            '<alias></alias>' \
            '<password>%s</password>' \
            '<parent-user-group>%s</parent-user-group>' \
            '<expiration-time>' \
            '<expiration-time>%sT23:59:59Z</expiration-time>' \
            '</expiration-time>' \
            '</user>' % (passw,dept,time_r)
    return url_modif_user, body


    
