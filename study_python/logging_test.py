
# -*- coding: utf-8 -*-
# @Date    : 2019-04-09 09:26:01
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')