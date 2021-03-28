# Kafka Producer Test Code
#
# @author       Tempuss(ben3787@gmail.com)
# @date         2021/03/28 01:24 created.
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


class TestKafkaProducer:
    def setUp(self):
        self.topic = "TEST_TOPIC"
        pass

    def acked(self, error, msg):
        #todo callback event를 이용해서 offset과 value 값 테스트 방안 필요
        print(msg.offset())
        print(loads(msg.value()))
        return msg.offset()

    def test_produce_success(
            self,
            test_producer,
    ):
        produce_offset = 0
        for url in mock_url_list:
            data = {"url": url}
            test_producer.produce(
                topic=test_topic,
                value=dumps(data).encode('utf-8'),
                callback=self.acked
            )
            # https://docs.confluent.io/5.4.2/clients/confluent-kafka-python/index.html#confluent_kafka.Producer.poll
            # Return Number of Callback events
            produce_offset += test_producer.poll()
            left_queue = test_producer.flush()

        assert len(mock_url_list) is produce_offset
        assert left_queue is 0
        assert 1 is 1
