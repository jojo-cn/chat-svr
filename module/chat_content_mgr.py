"""
聊天内容管理
"""
from module.debug_output import debug_screen


class ChatContentMgr(object):
    """  """

    def __init__(self):
        super(ChatContentMgr, self).__init__()

        self._db_doc = 'chat_massage'

    def get_msg_saved_in_db(self, _user_id, _db):
        pass

    def save_msg_to_db(self, _msg, _db):
        try:
            db_temp = {'haveRead': 'no'}
            db_temp.update(_msg)
            _db[self._db_doc].insert_one(db_temp)
            return True
        except Exception as e:
            debug_screen(e, __file__, 'save_msg_to_db')
            return False


