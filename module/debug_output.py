
"""
日志输出
"""
__all__ = ['debug_file', 'debug_screen']

import os
import time


def make_log_dir():
    try:
        cur_dir = os.getcwd()
        cur_dir += '\\log'
        if not os.path.exists(cur_dir):
            os.mkdir(cur_dir)
    except Exception as e:
        print('debug module make_log_dir fail: [%s]' % e)


def debug_file(_dbg, _file, _func):
    make_log_dir()
    try:
        file_path = os.getcwd() + '\\log\\log.txt'
        out = open(file_path, 'a')
        msg = '[%s][%s][%s][%s]\r\n' % (time.ctime(), _file, _func, _dbg)
        out.write(msg)
        out.flush()
        out.close()
    except Exception as e:
        print('[%s][debug_output.py][debug_file][%s]' % (time.ctime(), e))


def debug_screen(_dbg, _file, _func):
    print('[%s][%s][%s][%s]' % (time.ctime(), _file, _func, _dbg))
    debug_file(_dbg, _file, _func)


