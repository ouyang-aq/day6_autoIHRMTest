import logging
from logging import handlers
import os

BASEDIR=os.path.dirname(os.path.abspath(__file__))
def init_logging():
    #创建日志器
    logger=logging.getLogger()
    #设置日记等级
    logger.setLevel(logging.INFO)

    #创建处理器
    #创建控制台处理器
    sh=logging.StreamHandler()
    log_name=BASEDIR+"/log/ihrm.log"
    fh=logging.handlers.TimedRotatingFileHandler(log_name,when='D',interval=1,backupCount=7,encoding='utf-8')

    fmt= '%(asctime)s%(levelname)s[%(name)s][%(filename)s(%(funcName)s:%(lineno)d)]-%(message)s'
    formatter=logging.Formatter(fmt)

    fh.setFormatter(formatter)
    sh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(sh)
