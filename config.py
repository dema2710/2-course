import ssl

import pika

# Region	amazon-web-services::eu-north-1
# Cluster	kebnekaise.lmq.cloudamqp.com (DNS load balanced)
# Hosts	kebnekaise-01.lmq.cloudamqp.com
# (Availability Zone eun1-az1)
# Created at	2025-04-15 16:38 UTC+00:00
#
# AMQP details
# User & Vhost	iohctqqq
# Password	***  Rotate password
# Ports	5672 (5671 for TLS)
# URL	amqps://iohctqqq:***@kebnekaise.lmq.cloudamqp.com/iohctqqq

RMQ_HOST = "kebnekaise.lmq.cloudamqp.com"
RMG_PORT = 5671
RMQ_USER = "iohctqqq"
RMQ_PASSWORD = "Tcj-Xft7GNHNg0-qmPRuY8l2WiAlKlwP"
RMG_VIRTUAL_HOST = "iohctqqq"

ssl_context = ssl.create_default_context()

connection_params = pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMG_PORT,
    virtual_host=RMG_VIRTUAL_HOST,
    credentials=pika.PlainCredentials(username=RMQ_USER, password=RMQ_PASSWORD),
    ssl_options=pika.SSLOptions(context=ssl_context)
)

def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(parameters=connection_params)