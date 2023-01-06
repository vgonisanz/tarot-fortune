"""
Logs and time utils
"""
import os
from functools import wraps
from time import time

import logging
import structlog


logger = structlog.get_logger(__file__)


def setup_logger():
    logging.root.handlers = []
    logging.basicConfig(format='%(asctime)s - %(name)s : %(levelname)s : %(message)s',
                        level=logging.DEBUG)
    logging.getLogger('PIL').setLevel(logging.ERROR)


def timeit(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        logger.info("timeit", name=f.__name__, t_in_s=round(te-ts, 2))
        return result
    return wrap


def get_default_resources_path():
    path = os.path.join(os.path.dirname(__file__), 'resources')
    if not os.path.exists(path):
        raise ValueError(f"El path '{path}' no existe.")
    return path


def get_cards_json(language: str = 'es'):
    path = os.path.join(get_default_resources_path(), f'text/{language}/cards.json')
    if not os.path.exists(path):
        raise ValueError(f"El archivo '{path}' no existe.")
    return path


def get_card_path(id: str, deck: str = "rider-taite-tarot"):
    path = os.path.join(get_default_resources_path(), "cards", f"{deck}", f"{id}.jpg")
    if not os.path.exists(path):
        raise ValueError(f"El archivo '{path}' no existe.")
    return path
