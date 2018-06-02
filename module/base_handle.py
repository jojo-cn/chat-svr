

class BaseHandle(object):
    """ 消息处理基类，所有方法都需要继承类自己实现 """

    def __init__(self):
        pass

    def load_module(self):
        """ 模块加载，注册消息处理函数 """
        return NotImplemented

    def handle(self, _params, _client):
        """  具体的消息处理方法 """
        return NotImplemented
