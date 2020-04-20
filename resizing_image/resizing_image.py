#!/usr/bin/env python3

from conf_resizing_rabbitmq import RabbitmqConsume
import threading
import daemon
from time import sleep

conf_rabbitmq = RabbitmqConsume()

def start():
    conf_rabbitmq.basic_consume()

    print(' [*] Waiting for messages.')

    conf_rabbitmq.start_consuming()

if __name__ == '__main__':
    start()
