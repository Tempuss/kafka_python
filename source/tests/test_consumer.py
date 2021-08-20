# Kafka Consumer Test Code
#
# @author       Tempuss(ben3787@gmail.com)
# @date         2021/03/29 11:53 created.
# @copyright    Tempuss All rights reserved.
#
import pytest
import sys, os
import subprocess
sys.path.append(os.getcwd())

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
from config import config

class TestKafkaConsumer:
    def setUp(self):
        pass

    def test_consume_success(
            self,
            test_consumer,
    ):
        running = True
        test_consumer.subscribe([config.kafka_topic])
        # subprocess.call(["pytest -s tests/test_produce.py"])
        subprocess.Popen(
            [f"python produce/produce.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        while running:
            msg = test_consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                assert msg.error() is False
            else:
                running = False
                assert msg.value() is not None

            # 지속적인 produce를 위해서 pytest 코드를 서브프로세스로 실행

        test_consumer.close()
