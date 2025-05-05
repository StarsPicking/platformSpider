import logging

# from .crawler_util import *
# from .slider_util import *
# from .time_util import *


# def init_loging_config():
#     level = logging.INFO
#     logging.basicConfig(
#         level=level,
#         format="%(asctime)s %(name)s %(levelname)s (%(filename)s:%(lineno)d) - %(message)s",
#         datefmt='%Y-%m-%d %H:%M:%S'
#     )
#     _logger = logging.getLogger("PlatfromSpider")
#     _logger.setLevel(level)
#     return _logger
# logger = init_loging_config()

# 自定义日志格式
logger = logging.getLogger("django")
logger.info("fdfdfdsfs")
print(logger.__dict__)

