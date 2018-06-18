import pymongo


class DBConnector(object):
    """ 数据库连接管理 """

    def __init__(self, _dbname, _ip, _port):
        self.db_name = _dbname
        self.db_ip = _ip
        self.db_port = int(_port)

        self.core_db = None

    def connect(self):
        try:
            self.core_db = pymongo.MongoClient(host=self.db_ip, port=self.db_port)[self.db_name]
        except Exception as e:
            print('mongodb connect failed, %s' % e)
            raise e
