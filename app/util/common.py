import json as py_json
import logging
import time

from app.config import DEBUG_LOG, MAX_CONTENT_LENGTH, ALLOWED_EXTENSIONS, CMD_LOG_LEVEL, FILE_LOG_LEVEL, LOG_FILE
from flask import jsonify, request


def json(body=None):
    """
    * 返回Json数据
    * @param  dict body
    * @return json
    """
    if body is None:
        body = {}
    debug_id = unique_id()
    if (DEBUG_LOG):
        log().info(
            py_json.dumps({
                'LOG_ID': debug_id,
                'IP_ADDRESS': request.remote_addr,
                'REQUEST_URL': request.url,
                'REQUEST_METHOD': request.method,
                'PARAMETERS': request.args,
                'RESPONSES': body
            }))
    body['debug_id'] = debug_id
    return jsonify(body)


def unique_id(prefix=''):
    """
    获取unique id
    """
    return prefix + hex(int(time.time()))[2:10] + hex(int(time.time() * 1000000) % 0x100000)[2:7]


def log(name=None):
    """
    获取日志对象
    :param name 日志类别名
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # 建立一个file handler来把日志记录在文件里，级别为debug以上
    fh = logging.FileHandler(LOG_FILE)
    fh.setLevel(FILE_LOG_LEVEL)
    # 建立一个stream handler来把日志打在CMD窗口上，级别为error以上
    ch = logging.StreamHandler()
    ch.setLevel(CMD_LOG_LEVEL)
    # 设置日志格式 时间 - 名字 - 级别 - 内容
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将相应的handler添加在logger对象中
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger
