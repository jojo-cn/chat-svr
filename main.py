from module.svr import ServerMgr
# from module.packet import FailRetPacket
import argparse


def start():
    print('Run as Service')
    # print(str(FailRetPacket('TestOption', None)))
    one_svr = ServerMgr()
    one_svr.initialize()
    one_svr.run()


def heart_beat():
    print('Run as HeartBeat Check')


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--run-as', type=str, default='')
        args = parser.parse_args()
        print(args.run_as)
        if args.run_as == 'service':            # 启动主服务模块
            start()
        elif args.run_as == 'heartbeat':        # 启动心跳检测模块
            heart_beat()
        elif args.run_as == '':                 # 默认启动主服务
            start()
    except Exception as e:
        print('Exception at Main: %s' % e)
