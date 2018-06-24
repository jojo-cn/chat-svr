
"""
## 登录
{"option":"logon",
 "params":{"logon_name":"Stanley",	## 登录名，可以是 账号名、手机号码或者邮箱
           "password":"202cb962ac59075b964b07152d234b70"}	## 密码 MD5 加密
}

## 登出
{"option":"logoff",
 "params":{"user_id":"5b24b4dc04968302e4c61feb"}    # 要登出的用户ID
}
"""

from module.base_handle import BaseHandle
from module.err import Err
from module.imc import IMC
from module.packet import *
from hashlib import md5


class User(object):
    """
    Client User information
    """

    def __init__(self):
        super(User, self).__init__()
        self.name = ''  #  user name
        self.user_id = ''
        self.cli = None


class UserList(object):
    """docstring for UserList"""

    def __init__(self):
        super(UserList, self).__init__()
        self._user_list = {}

    def add_user(self, _user_dict):
        self._user_list.update(_user_dict)

    def release_user(self, _user_id):
        try:
            del self._user_list[_user_id]
        except Exception as e:
            pass

    def is_user_logon(self, _user_id):
        if not isinstance(_user_id, str):
            # 参数格式不正确
            return False
        if _user_id in self._user_list:
            return True
        else:
            return False

    def report_user_by_id(self, _user_id):
        try:
            return self._user_list[_user_id]
        except Exception as e:
            return None


class UserHandler(BaseHandle):
    """ User action handler """

    def __init__(self):
        super(UserHandler, self).__init__()
        self._all_users = UserList()
        #
        # 用户文档（相当于用户表）
        self._db_doc = 'user_info'
        #
        # 注册模块间通讯
        IMC.register('get_user', self.get_user_by_id)

    def load_module(self):
        """ 模块加载，注册消息处理函数 """
        return {'logon': self.user_logon,
                'logoff': self.user_logoff}

    def user_logon(self, _params, _client, _db):
        try:
            name = _params['logon_name']
            pwd = _params['password']
            m = md5()
            m.update(pwd.encode())
            pwd_md5 = m.hexdigest()
            cur = _db[self._db_doc].find({'username': name, 'password': pwd_md5})
            # 确认用户名密码是否存在且正确
            if cur.count > 0:
                # 确认该用户是否已经登陆了
                one = cur.next()
                if self._all_users.is_user_logon(one['_id']):
                    return FailRetPacket('logon', {'err_massage': Err.USER_ALREADY_LOGON})

                # 登录成功
                n_user = User()
                n_user.name = name
                n_user.user_id = str(one['_id'])
                n_user.cli = _client
                _client.user = n_user

                # 添加到用户列表中
                self._all_users.add_user({n_user.user_id: n_user})

                return SuccessRetPacket('logon', {'user_id': n_user.user_id})
            else:
                return FailRetPacket('logon', {'err_massage': Err.USER_LOGON_FAILED})
        except Exception as e:
            print('user logon failed: %s' % e)
            return False

    def user_logoff(self, _params, _client, _db):
        user_id = _params['user_id']
        self._all_users.release_user(user_id)

    def get_user_by_id(self, __user_id):
        return self._all_users.report_user_by_id(__user_id)

