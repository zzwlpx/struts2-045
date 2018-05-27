# -*- coding: UTF-8 -*-
#开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件   
import logging
import logging.handlers

class Logger():
    #def __init__(self, logname, loglevel, logger):
    def __init__(self):
        
        logger='searchPrint'
        logfile='check.txt'
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件,每天一个日志文件
        tfilehandler = logging.handlers.TimedRotatingFileHandler(logfile,'D',1)

        tfilehandler.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        consolehandler = logging.StreamHandler()
        consolehandler.setLevel(logging.DEBUG)
        
        # 定义handler的输出格式
        formatter = logging.Formatter('%(message)s')
        #formatter = logging.Formatter(formatter)
        #formatter = format_dict[int(loglevel)]
        tfilehandler.setFormatter(formatter)
        consolehandler.setFormatter(formatter)
        #smtphandler.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(tfilehandler)
        self.logger.addHandler(consolehandler)
        #self.logger.addHandler(smtphandler)

    
    def getlogger(self):
        return self.logger
log=Logger().getlogger()
