import logging
import logging.handlers
import time
import os

#默认
'''
logging.basicConfig(filename='test.log',
                    filemode='a+',
                    level=logging.INFO,
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt ="%d-%m-%Y %H:%M:%S")

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
'''
#自定义logger
logger = logging.getLogger(__name__)
'''
dt = time.strftime('%Y-%m-%d', time.localtime(time.time()))
log_path = os.path.dirname(os.getcwd()) + '/Logs/'
log_name = log_path + dt + '.log'
logfile = log_name
'''
handler1 = logging.StreamHandler()
#handler2 = logging.FileHandler(logfile)
# 每隔 1小时 划分一个日志文件，interval 是时间间隔，备份文件为 10 个
handler2 = logging.handlers.TimedRotatingFileHandler('../Logs/test.log', when="W0", interval=1, backupCount=10)


logger.setLevel(level=logging.DEBUG)
handler1.setLevel(level=logging.WARNING)
handler2.setLevel(level=logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

logger.addHandler(handler1)
logger.addHandler(handler2)

# 分别为 10、30、30
# print(handler1.level)
# print(handler2.level)
# print(logger.level)

# 每隔 1000 Byte 划分一个日志文件，备份文件为 3 个
#file_handler = logging.handlers.RotatingFileHandler("test.log", mode="w", maxBytes=1000, backupCount=3, encoding="utf-8")


logger.debug('This is a customer debug message')
logger.info('This is an customer info message')
logger.warning('This is a customer warning message')
logger.error('This is an customer error message')
logger.critical('This is a customer critical message')