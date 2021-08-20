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
    kafka_host = os.environ.get("KAFKA_HOST", "0.0.0.0:29092")

    kafka_produce_conf = {
        'bootstrap.servers': kafka_host,
        'broker.address.family': 'v4',
        'retries': 0,
        'error_cb': error,
    }

    kafka_consumer_conf = {
        'bootstrap.servers': kafka_host,
        'broker.address.family': 'v4',
        'group.id': "1",
        'error_cb': error,
    }

    kafka_topic = "crawl_url_list"

    json_path = "./data/url_list.json"


    def __init__(self):
        pass


config = Config()
