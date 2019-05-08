import logging
from logging.handlers import HTTPHandler
import sys

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

#Streamhandler
stream_handler = logging.Stream(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
logger.addHandler(stream_handler)

#FileHandler
file_handler = logging.FileHandler('output.log')
file_handler.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#log
logger.info('this is a log info')
logger.debug('debugging')
logger.warning('WWWWarning')
logger.info('finish')

