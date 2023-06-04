import datetime
import logging
import os
import json

if not os.path.exists("logs"):
    os.makedirs("logs")
log_file = f"logs/log_" + \
    str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"
logger = logging.getLogger("tests")
fh = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(level=logging.DEBUG)


def log_response(response):
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response JSON: {json.dumps(response.json(), indent=4)}")
