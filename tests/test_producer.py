from .context import producer
from .context import settings

import os


def test_producer():
    queue_url = os.getenv('SQS_QUEUE_URL')
    print(queue_url)
    p = producer.Producer(queue_url)
    print(p)
