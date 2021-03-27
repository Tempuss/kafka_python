# Kafka Producer Sample
#
# @author       Tempuss(ben3787@gmail.com)
# @date         2021/03/28 01:24 created.
# @copyright    Tempuss All rights reserved.
#
import os
import sys
sys.path.append(os.getcwd())

from confluent_kafka import Producer
from json import dumps
from config import config

try:
    producer = Producer(**config.kafka_conf)
    producer.poll()
except Exception as ex:
    print(ex)
    sys.exit()


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))
#
# for i in range(1):
#     data = {'str': 'result' + str(i)}
#     producer.produce(
#         topic=config.topic,
#         value=dumps(data).encode('utf-8'),
#         #callback=acked
#     )
#     producer.flush()

