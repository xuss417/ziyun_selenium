# coding:utf-8
import logging,time,os
from config.globalparameter import log_path

'''
配置日志文件，输出INFO级别以上的日志
'''
log_path = log_path

class Log:
    def __init__(self):
        self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s]-%(filename)s)-%(levelname)s: %(message)s')
    def setMSG(self, level, msg):

        # 定义Handler输出到文件和控制台
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        #创建一个streamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        # 添加Handler
        self.logger.addHandler(ch )
        # 添加日志信息，输出INFO级别的信息
        if level == 'info':
            self.logger.info(msg)
        elif level=='debug':
            self.logger.debug(msg)
        elif level=='info':
            self.logger.info(msg)
        elif level=='warning':
            self.logger.warning(msg)
        elif level=='error':
            self.logger.error(msg)
        # 移除句柄，否则日志会重复输出
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        fh.close()

    def debug(self, msg):
        self.setMSG('debug', msg)

    def info(self, msg):
        self.setMSG('info', msg)

    def warning(self, msg):
        self.setMSG('warning', msg)

    def error(self, msg):
        self.setMSG('error', msg)