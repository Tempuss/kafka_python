# Kafka Producer Sample
#
# @author       Tempuss(ben3787@gmail.com)
# @date         2021/03/28 01:24 created.
# @copyright    Tempuss All rights reserved.
#
import os
import sys
import json

sys.path.append(os.getcwd())

from confluent_kafka import (
    Producer,
    KafkaError,
    KafkaException,
)

from json import (
    dumps,
    load,
)
from config import config
from common import acked

# Create Connection
try:
    producer = Producer(**config.kafka_produce_conf)
except Exception as ex:
    print(ex)

# Load Json File
with open(config.json_path) as json_file:
    json_data = json.load(json_file)


# Produce URL data
for url in json_data:
    data = {"url": url}
    producer.produce(
        topic=config.kafka_topic,
        value=dumps(data).encode('utf-8'),
        callback=acked
    )
    producer.flush()


producer.flush()
# producer.close()
quit()
