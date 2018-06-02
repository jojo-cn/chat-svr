"""
处理客户端心跳，
超过心跳时间的客户端踢出
"""


class HeartBeat(object):

    def __init__(self, _time, _client_list):
        self.heart_time = _time
        self.client_list = _client_list

