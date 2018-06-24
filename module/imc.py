"""
inter module communication
模块间通讯
"""


class IMC(object):
    """  """

    def __init__(self):
        super(IMC, self).__init__()

    MODULE_PROC = {}

    @staticmethod
    def register(_name, _method):
        IMC.MODULE_PROC.update({_name: _method})

    @staticmethod
    def process(_name, _input):
        try:
            __method = IMC.MODULE_PROC[_name]
            return __method(_input)
        except Exception as e:
            print('IMC process[%s]' % e)
            return None
