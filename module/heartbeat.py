"""
处理客户端心跳，
超过心跳时间的客户端踢出

## 客户端心跳保活
{"option": "heartbeat",
 "params": {}
}
"""
from time import time
from module.base_handle import BaseHandle


class HeartBeat(BaseHandle):

    def __init__(self):
        super(HeartBeat, self).__init__()

    def load_module(self):
        return {'heartbeat': self.update_keep_alive}

    def update_keep_alive(self, _params, _client, _db):
        _client.keep_live_time = time()
