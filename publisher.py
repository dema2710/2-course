import pika.adapters.blocking_connection

from config import get_connection
from time import sleep


def produce_message(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'news'
    channel.queue_declare(queue=QUEUE)
    message = 'hello kitty ))) {item}'
    for item in range(1):
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE,
            body=message.format(item=item)
        )


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            produce_message(channel)


if __name__ == "__main__":
    main()