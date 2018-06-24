"""
用户信息传输模块
用于在两个用户之间传递信息
例如聊天内容

## P2P聊天
{
"option": "P2P",
"params":{"msg_id": "abcd123456",                           # 消息ID，唯一标识一个消息
          "from_user": "5b24b4dc04968302e4c61feb",          # 消息发送方ID
          "to_user": "5b24b4dc04968302e4c1111",             # 消息传达方ID
          "create_time": 1529308818.3140554,                # 消息创建的时间戳，由服务器生成，以服务器的时间为准
          "content_text": "hello world",                    # 文本格式的消息主体
          "content_img_tran_id": "",                        # 图片格式的消息传输ID，用于生成图片的下载地址
          "is_forever": False,                              # 标识该消息是永久保存的消息，还是会自动销毁的消息
          "delay_time": 15                                  # 消息销毁的延迟时间（秒），如果是永久消息，则忽略
         }
}


## 聊天室
{"option": "multi_users",
 "params": {"msg_id": "abcd123456",                         # 消息ID，唯一标识一个消息
            "from_user": "5b24b4dc04968302e4c61feb",        # 消息发送方ID
            "room_id": "5b24b4dc04968302e4c61feb",          # 承载消息的房间ID
            "create_time": 1529308818.3140554,              # 消息创建的时间戳，由服务器生成，以服务器的时间为准
            "content_text": "hello world",                  # 文本格式的消息主体
            "content_img_tran_id": "",                      # 图片格式的消息传输ID，用于生成图片的下载地址
            "is_forever": False,                            # 标识该消息是永久保存的消息，还是会自动销毁的消息
            "delay_time": 15                                # 消息销毁的延迟时间（秒），如果是永久消息，则忽略
            }
}
"""

from module.base_handle import BaseHandle
from module.chat_room import ChatRoomManager
from module.imc import IMC
from module.chat_content_mgr import ChatContentMgr
from module.debug_output import debug_screen
from module.packet import *
import json


class Transport(BaseHandle):
    """   """

    def __init__(self):
        super(Transport, self).__init__()
        self._room_mgr = ChatRoomManager()
        self._chat_content_mgr = ChatContentMgr()

    def load_module(self):
        """ 模块消息处理函数注册 """
        return {'p2p_transport': self.p2p_msg_transport,
                'multi_transport': self.multi_users_msg_transport}

    def p2p_msg_transport(self, _params, _client, _db):
        """ 端到端的用户信息传递 """
        _to_user_id = _params['to_user']
        _to_user = IMC.process('get_user', _to_user_id)
        # 将信息保存到数据库
        ret = self._chat_content_mgr.save_msg_to_db(_params, _db)
        if not ret:
            return FailRetPacket('p2p', None)

        if _to_user is not None:
            # 转发给相应的用户
            try:
                pack = NormalRetPacket('p2p', _params)
                _to_user.cli.writer.write(json.dumps(str(pack)) + '\r\n')
            except Exception as e:
                debug_screen(e, __file__, 'p2p_msg_transport')
                return FailRetPacket('p2p', None)

        return SuccessRetPacket('p2p', None)

    def multi_users_msg_transport(self, _params, _client, _db):
        """ 多用户环境信息传递，例如聊天室环境 """
        pass

