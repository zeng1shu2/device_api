# coding:utf-8

_Url_token = "http://192.168.5.114:8050/CustomerApi/GetToken"

_Url_Node = "http://192.168.5.114:8050/CustomerApi/GetNode"

_Url_Depinfo = "http://192.168.5.114:8050/CustomerApi/GetDepInfo"

_Url_ChangeUsb = "http://192.168.5.114:8050/CustomerApi/ChangeUsbPolicy"

_Url_ChangeSerial = "http://192.168.5.114:8050/CustomerApi/ChangeSerialCtrlPolicy"

_Url_ChangeNet = "http://192.168.5.114:8050/CustomerApi/ChangeNetCtrlPolicy"

_Url_ChangeTpConfig =  "http://192.168.5.114:8050/CustomerApi/ChangeTpConfigPolicy"

_User_Info = {
    "account": "admin",
    "password": "zlgmcu!@#1"
}

# service、no为必填（no为部门节点）
_ChangeUsb = {
    "service": "",
    "serialnumber": "",
    "action": 0,
    "remark": "",
    "no": 0,
    "type": 2,
    "systemType": 1,
    "nodeType": 1
}

# process、no为必填（no为部门节点）
_ChangeSerial = {
    "process": "",
    "cmdline": "",
    "company": "",
    "ptype": 0,
    "session": 0,
    "action": 0,
    "remark": "",
    "no": 0,
    "type": 2,
    "systemType": 1,
    "nodeType": 1
}

# process、no为必填（no为部门节点）
_ChangeNet = {
    "process": "",
    "cmdline": "",
    "local": "",
    "remote": "",
    "protocol": 0,
    "company": "",
    "ptype": 0,
    "session": 0,
    "action": 0,
    "remark": "",
    "no": 0,
    "type": 2,
    "systemType": 1,
    "nodeType": 1
}

# TpConfig、no为必填(no为部门节点)
_ChangeTp = {
  "name": "",
  "path": "",
  "no": 2,
  "type": 2,
  "systemType": 1,
  "nodeType": 1
}
