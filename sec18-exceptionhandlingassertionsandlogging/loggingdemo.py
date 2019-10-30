import logging

# default log level is warning
# Use basicConfig to specify the log file and the log level
logging.basicConfig(filename="myLog.log", level=logging.INFO)

logging.critical("Critical");
logging.error("Error");
logging.warning("Warning");
logging.info("Info");
logging.debug("Debug");
