"""
数据包
"""
__all__ = ['SuccessRetPacket', 'FailRetPacket', 'NormalRetPacket']


class SuccessRetPacket(object):
    """ """
    def __init__(self, _option, _msg):
        super(SuccessRetPacket, self).__init__()
        self._option = _option
        self._msg = {'Result': 'Success'}
        if _msg is not None:
            self._msg.update(_msg)

    def __str__(self):
        return '{"option": %s, "params": %s}' % (self._option, str(self._msg))


class FailRetPacket(object):
    """ """
    def __init__(self, _option, _msg):
        super(FailRetPacket, self).__init__()
        self._option = _option
        self._msg = {'Result': 'Failed'}
        if _msg is not None:
            self._msg.update(_msg)

    def __str__(self):
        return '{"option": %s, "params": %s}' % (self._option, str(self._msg))


class NormalRetPacket(object):
    """ """
    def __int__(self, _option, _msg):
        self._option = _option
        self._msg = _msg

    def __str__(self):
        ret = {"option": self._option}
        if self._msg is not None:
            ret.update({"params": self._msg})
        return str(ret)

