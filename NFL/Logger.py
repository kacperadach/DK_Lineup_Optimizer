import logging

def generate_logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

LOGGER = generate_logger()

def get_logger():
    return LOGGER
