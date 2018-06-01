from module.svr import ServerMgr


def start():
	oneSvr = ServerMgr()
	oneSvr.load_config()
	oneSvr.run()


if __name__ == '__main__':
	start()
