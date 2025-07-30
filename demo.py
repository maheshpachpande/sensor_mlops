from sensor.logger import logging
from sensor.exception import CustomException
import sys

logging.info("Logging has started")

try:
    a = 1/0
except Exception as e:
    raise CustomException(e)