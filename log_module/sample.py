import logging
logging.basicConfig(level=logging.DEBUG, 
	filename="log.txt",
	format="%(asctime)s=>%(levelname)s==>%(message)s")
logging.info("INFO message")
logging.error("ERROR message")
logging.debug("DEBUG message")
logging.warn("WARNING message")