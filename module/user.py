
"""
## 登录
{"option":"logon",
 "params":{"logon_name":"",	## 登录名，可以是 账号名、手机号码或者邮箱
           "password":"xxxxxxxx"}	## 密码
}
"""

from module.base_handle import BaseHandle
import pymongo

class User(BaseHandle):
    """Client User information"""

    def __init__(self):
        super(User, self).__init__()
        self.name = '' #  user name
        self.sock_fd = 0
        self.client_id = 0

    def load_module(self):
        """ 模块加载，注册消息处理函数 """
        return {'logon': self.user_logon}

    def user_logon(self, _params, _client):
        try:
            print(_params['logon_name'])
            print(_params['password'])
        except Exception as e:
            print('user handle failed: %s' % e)


class UserList(object):
    """docstring for UserList"""

    def __init__(self):
        super(UserList, self).__init__()
        self.user_list = []

	
		
