__all__ = ['ServerMgr']

from module.netio import NetIO
from module.client import *
from module.msg import MsgHandle
from module.heartbeat import HeartBeat
import configparser


class ServerMgr(object):
	"""docstring for ServerMgr"""

	def __init__(self):
		super(ServerMgr, self).__init__()
		self.port = None
		self.client_mgr = ClientList()  # 客户端管理
		self.msg_handle = MsgHandle()
		self.heart_mgr = None
		self.svr = None

	def load_config(self):
		conf = configparser.ConfigParser()
		try:
			conf.read('conf.ini')
			self.port = int(conf['server']['port'])
			self.heart_mgr = HeartBeat(int(conf['server']['heartbeat']), self.client_mgr)
		except Exception as e:
			print('ini read failed: %s' % e)
			return False
		return True

	def run(self):
		if not self.port:
			self.port = 52314  # 在未设置端口时启用默认端口
		self.svr = NetIO(self.port)
		self.svr.set_read_cb(self.read_callback)
		self.svr.set_connect_cb(self.connect_callback)
		self.svr.set_disconn_cb(self.disconn_callback)
		self.svr.run_svr()

	def stop(self):
		self.svr.stop_svr()

	def connect_callback(self, _reader, _writer):
		""" 客户端创建链接，加入客户端列表 """
		return self.client_mgr.add_client(_reader, _writer)

	def read_callback(self, _data, _client):
		""" 处理客户端发来的数据 """
		_data = _data.decode()
		print(_data)
		self.msg_handle.handle(_data, _client)


	def disconn_callback(self, _client):
		""" 客户端断开链接，执行清理工作 """
		self.client_mgr.del_client(_client)
