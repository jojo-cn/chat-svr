"""
json消息类型
## option  操作码
## params  参数列表

## 登录
{"option":"logon",
 "params":{"logon-name":"",	## 登录名，可以是 账号名、手机号码或者邮箱
           "password":"xxxxxxxx"}	## 密码
}

"""
__all__ = ['MsgHandle']

import json
from module.user import User

class MsgHandle(object):
    """ 消息处理 """

    def __init__(self):
        self.handle_map = {}
        self.db_ctrl = None

        self._user = User()

        #
        self.handle_map.update(self._user.load_module())

    def set_database(self, _db):
        self.db_ctrl = _db


    def handle(self, _data, _client):
        try:
            msg = json.loads(_data)
            op = msg['option']
            params = msg['params']
            if op and params:
                self.handle_map[op](msg, _client, self.db_ctrl)
        except Exception as e:
            print('client send Bad Data!!!: %s' % e)
        _data = _data + ' from Server\r\n'
        _client.writer.write(_data.encode())




