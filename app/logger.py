import logging
from colorlog import ColoredFormatter

formatter = ColoredFormatter(
    "%(log_color)s%(levelname)s: %(asctime)s [%(name)s] %(reset)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

def getLogger(name):
    LOG = logging.getLogger(name)
    LOG.addHandler(handler)
    LOG.setLevel(logging.DEBUG)
    return LOG

logging.getLogger("httpcore.connection").disabled = True
logging.getLogger("httpcore.http11").disabled = True
logging.getLogger("httpx").disabled = True
logging.getLogger("telegram").disabled = True
logging.getLogger("telegram.ext.ExtBot").disabled = True
logging.getLogger("telegram.ext.Application").disabled = True
logging.getLogger("apscheduler.scheduler").disabled = True
logging.getLogger("apscheduler.executors.default").disabled = True
logging.getLogger("uvicorn").disabled = True
logging.getLogger("fastapi").disabled = True
logging.getLogger("tzlocal").disabled = True