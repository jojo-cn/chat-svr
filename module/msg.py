

"""
json消息类型
## option  操作码
## params  参数列表

## 登录
{'option':'logon',
 'params':{'logon-name':'',     ## 登录名，可以是 账号名、手机号码或者邮箱
           'password':'xxxxxxxx'} ## 密码
}

"""

class MsgHandle(object):
    """ 消息处理 """

    def __init__(self):
        self.handle_map = {}
