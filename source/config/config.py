# Configuration Class For Entire App
#
# @author       Tempuss(ben3787@gmail.com)
# @date         2021/03/28 01:24 created.
# @copyright    Tempuss All rights reserved.
#
import os
from common import error

class Config:
    """
    설정용 config class
    """
    #kafka_host = os.environ.get("KAFKA_HOST", "192.168.0.4:9092").split(",")
    kafka_host = os.environ.get("KAFKA_HOST", "localhost:9092")
    topic = "test"

    kafka_conf = {
        'bootstrap.servers': kafka_host,
        'retries': 0,
        'error_cb': error,
    }


    def __init__(self):
        pass

config = Config()


