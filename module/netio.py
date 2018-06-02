__all__ = ['NetIO']

import asyncio


class NetIO(object):
	"""docstring for NetIO"""

	def __init__(self, _port):
		super(NetIO, self).__init__()
		self.port = _port
		self.connect_cb = None
		self.read_cb = None
		self.disconn_cb = None
		self.loop = None

	def run_svr(self):
		self.loop = asyncio.get_event_loop()
		cor = asyncio.start_server(self.handle, host='', port=self.port, loop=self.loop)
		svr = self.loop.run_until_complete(cor)
		try:
			self.loop.run_forever()
		except Exception as e:
			print(e)
		svr.close()
		self.loop.run_until_complete(svr.wait_closed())
		self.loop.close()

	def stop_svr(self):
		self.connect_cb = None
		self.read_cb = None
		self.disconn_cb = None

	@asyncio.coroutine
	def handle(self, _reader, _writer):
		""" 新建链接，以及后续的读写处理都在这里 """
		client = None
		if self.connect_cb:
			client = self.connect_cb(_reader, _writer)

		# 循环接收数据 —— 协程
		while True:
			try:
				yield from _writer.drain()
				data = yield from _reader.readline()
				data = data.strip(b'\r\n ')
				if self.read_cb and data and client:
					self.read_cb(data, client)
				if not data:
					break
			except Exception as e:
				print('read data failed: %s' % e)
				break

		# 断开链接，清理数据
		if self.disconn_cb:
			self.disconn_cb(client)

		_writer.close()

	def set_connect_cb(self, _cb):
		self.connect_cb = _cb

	def set_read_cb(self, _cb):
		self.read_cb = _cb

	def set_disconn_cb(self, _cb):
		self.disconn_cb = _cb
