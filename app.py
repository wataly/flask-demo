import logging
import os
import time
from logging import FileHandler
from app import app
from app.config import LOG_PATH

if __name__ == '__main__':
    # 日志句柄
    fh = FileHandler(os.path.join(LOG_PATH, '{}.log'.format(time.strftime('%Y%m%d'))))
    # 日志级别
    fh.setLevel(logging.DEBUG)
    # 进程日志输出到文件
    app.logger.addHandler(fh)
    # 方便本地测试时指定端口
    app.debug = True
    app.run(host='0.0.0.0', port=9529)
    # app.debug = False
    # app.run()