# coding=utf-8

"""

"""

__all__ = [
    'getLogger',
    'DEBUG',
    'INFO',
    'WARN',
    'ERROR',
    'FATAL']

import time
import logging
import logging.handlers
from logging import getLogger, INFO, WARN, DEBUG, ERROR, FATAL, WARNING, CRITICAL
from firefly.server.globalobject import GlobalObject

LOG_FILE_MAXBYTES = 31457280
LOG_FILE_BACKUPCOUNT = 1000
LOG_LEVEL = logging.DEBUG

MODULE_NAME = GlobalObject().json_config.get("name", '')

filename = time.strftime('%Y-%m-%d', time.localtime(time.time()))
LOG_FILENAME = 'logs/{filename}.log'.format(filename = filename)
FORMAT = '[%(asctime)s]-%(levelname)-8s<%(name)s>{%(filename)s:%(lineno)s} -> %(message)s'
formatter = logging.Formatter(FORMAT)
normalHandler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes = LOG_FILE_MAXBYTES, backupCount = LOG_FILE_BACKUPCOUNT)
normalHandler.setFormatter(formatter)
normalLog = getLogger(MODULE_NAME)
normalLog.setLevel(LOG_LEVEL)
normalLog.addHandler(normalHandler)

ERROR_LOG_FILENAME = 'logs/ERROR_{filename}.log'.format(filename = filename)
errorHandler = logging.handlers.RotatingFileHandler(ERROR_LOG_FILENAME, maxBytes = LOG_FILE_MAXBYTES, backupCount = LOG_FILE_BACKUPCOUNT)
errorHandler.setFormatter(formatter)
errorLog = getLogger(MODULE_NAME+'_error')
errorLog.setLevel(LOG_LEVEL)
errorLog.addHandler(errorHandler)

class IbbgameLog(object):

    def __init__(self, normalLog, errorLog):
        if not isinstance(normalLog, logging.Logger) or not isinstance(errorLog, logging.Logger):
            raise Exception('create BsfbLog class param error!')
        self.normalLog = normalLog
        self.errorLog = errorLog


    def setLevel(self, level):
        self.normalLog.setLevel(level)


    def debug(self, msg, *args, **kwargs):
        if self.normalLog.isEnabledFor(DEBUG):
            self.normalLog._log(DEBUG, msg, args, **kwargs)


    def info(self, msg, *args, **kwargs):
        if self.normalLog.isEnabledFor(INFO):
            self.normalLog._log(INFO, msg, args, **kwargs)


    def warning(self, msg, *args, **kwargs):
        if self.normalLog.isEnabledFor(WARN):
            self.normalLog._log(WARNING, msg, args, **kwargs)


    def warn(self, msg, *args, **kwargs):
        if self.normalLog.isEnabledFor(WARN):
            self.normalLog._log(WARN, msg, args, **kwargs)


    def error(self, msg, *args, **kwargs):
        if self.errorLog.isEnabledFor(ERROR):
            self.normalLog._log(ERROR, msg, args, **kwargs)
            self.errorLog._log(ERROR, msg, args, **kwargs)


    def critical(self, msg, *args, **kwargs):
        if self.errorLog.isEnabledFor(CRITICAL):
            self.normalLog._log(CRITICAL, msg, args, **kwargs)
            self.errorLog._log(CRITICAL, msg, args, **kwargs)


    def fatal(self, msg, *args, **kwargs):
        if self.errorLog.isEnabledFor(FATAL):
            self.normalLog._log(FATAL, msg, args, **kwargs)
            self.errorLog._log(FATAL, msg, args, **kwargs)


logger = IbbgameLog(normalLog, errorLog)
