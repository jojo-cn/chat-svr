

class User(object):
	"""Client User infomation"""
	def __init__(self):
		super(User, self).__init__()
		self.name = '' #  user name
		self.sock_fd = 0
		self.client_id = 0


class UserList(object):
	"""docstring for UserList"""
	def __init__(self):
		super(UserList, self).__init__()
		self.user_list = []

	
		
