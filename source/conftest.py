import pytest
import os
import sys

sys.path.append(os.getcwd())

from config import config
from common import acked
from json import (
    load,
    dumps,
)

from tests.mock_data import (
    test_topic,
    mock_url_list,
)

from confluent_kafka import (
    Consumer,
    Producer,
    KafkaError,
    KafkaException,
)


@pytest.fixture(scope="function")
def test_producer():
    producer = Producer(**config.kafka_produce_conf)
    yield producer

@pytest.fixture(scope="function")
def test_consumer():
    consumer = Consumer(**config.kafka_consumer_conf)
    yield consumer


@pytest.fixture(scope="function")
def init_produce_data(
        test_producer,
):
    for url in mock_url_list:
        data = {"url": url}
        test_producer.produce(
            topic=test_topic,
            value=dumps(data).encode('utf-8'),
            callback=acked
        )
        test_producer.flush()

