import logging

def setup_logger(name: str = "jmoksbot", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)

    # Prevents duplicate logs if imported multiple times
    if logger.handlers:
        return logger
    
    logger.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False

    return logger