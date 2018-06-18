"""
聊天室模块
"""


class ChatRoom(object):
    """   """

    def __init__(self):
        super(ChatRoom, self).__init__()
        self.room_id = ''           # 房间ID
        self.user_collection = []   # 进入该房间的用户集
        # 数据库数据集名称
        self._db_doc = 'room'


class ChatRoomManager(object):
    """  """
    def __init__(self):
        super(ChatRoomManager, self).__init__()
        self._room_collection = {}      # 房间集合
