import logging

def get_logger():
    logger = logging.getLogger("automation")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.fileHandler("test.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger