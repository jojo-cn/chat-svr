__all__ = ['ClientList', 'Client']

import time

#
#
class Client(object):
    """docstring for Client"""
    def __init__(self, _reader, _writer):
        super(Client, self).__init__()
        self.port = _reader._transport._sock.getpeername()[1] #  端口
        self.addr = _reader._transport._sock.getpeername()[0] #  IP
        self.reader = _reader #  输入接口
        self.writer = _writer #  输出接口
        self.keep_live_time = time.time()


##########################################################
# 客户端列表
#
class ClientList(object):
    """ 客户端管理器 """
    def __init__(self):
        super(ClientList, self).__init__()
        self.client_list = []

    def add_client(self, _reader, _writer):
        """ 新增客户端连接 """
        print('have client: %d' % _reader._transport._sock.fileno())
        cli = Client(_reader, _writer)
        self.client_list.append(cli)
        return cli

    def del_client(self, _client):
        print('delete client: %d' % _client.reader._transport._sock.fileno())
        ind = self.client_list.index(_client)
        del self.client_list[ind]
		
