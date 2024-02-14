import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)
logging.critical("Critical")
logging.error("Error")
logging.warning("warrning")
logging.info("Info")
logging.debug("Debug")