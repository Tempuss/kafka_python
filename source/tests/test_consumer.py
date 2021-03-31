# Kafka Consumer Test Code
#
# @author       Tempuss(ben3787@gmail.com)
# @date         2021/03/29 11:53 created.
# @copyright    Tempuss All rights reserved.
#
import pytest
from json import (
    dumps,
    load,
    loads,
)

from tests.mock_data import (
    mock_url_list,
    test_topic,
)

from confluent_kafka import (
    KafkaError,
    KafkaException,
)


class TestKafkaConsumer:
    def setUp(self):
        self.topic = "TEST_TOPIC"
        pass

    def test_consume_success(
            self,
            init_produce_data,
            test_consumer,
    ):
        running = True
        test_consumer.subscribe([test_topic])
        while running:

            msg = test_consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    print(msg.topic(), msg.partition(), msg.offset())
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                running = False
                print(msg)

        #assert msg is not None

        test_consumer.close()

        pass