# Kafka Consumer Sample
#
# @author       Tempuss(ben3787@gmail.com)
# @date         2021/03/28 02:28 created.
# @copyright    Tempuss All rights reserved.
#
import os
import sys
import json

sys.path.append(os.getcwd())

from confluent_kafka import (
    Consumer,
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
    consumer = Consumer(**config.kafka_consumer_conf)
except Exception as ex:
    print(ex)

running = True


def basic_consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(),
                                      msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                consume_message = json.loads(msg.value())
                print(consume_message)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


def shutdown():
    running = False


basic_consume_loop(
    consumer=consumer,
    topics=[config.kafka_topic],
)

quit()
