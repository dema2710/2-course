import time

from config import get_connection
import pika


def process_new_message(channel: pika.adapters.blocking_connection.BlockingChannel, method, properties, body):
    print(body, 5555555555555555555555555)
    # time.sleep(1)
    channel.basic_ack(delivery_tag=method.delivery_tag)


def consume_message(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'news'
    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=process_new_message,
        # auto_ack=True
    )

    channel.start_consuming()


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            consume_message(channel)


if __name__ == "__main__":
    main()