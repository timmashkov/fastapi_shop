import json
import os
from aio_pika import connect_robust
import pika
from dotenv import load_dotenv

from core.config import logger

load_dotenv()


class PikaClient:
    host = os.environ.get("RABBIT_HOST")
    port: int = os.environ.get("RABBIT_PORT")
    queue_name: str = os.environ.get("PUBLISH_QUEUE")
    consume_queue: str = os.environ.get("CONSUME_QUEUE")

    def __init__(self, process_call):
        self.publish_queue_name = self.queue_name
        self.connection = pika.BlockingConnection(self.host)
        self.channel = self.connection.channel()
        self.publish_queue = self.channel.queue_declare(queue=self.publish_queue_name)
        self.callback_queue = self.publish_queue.method.queue
        self.response = None
        self.process_call = process_call
        logger.info("Rabbit is connected")

    async def consume(self, loop):
        connection = await connect_robust(host=self.host, port=self.port, loop=loop)
        channel = await connection.channel()
        queue = await channel.declare_queue(self.consume_queue)
        await queue.consume(self.process_incoming_message, no_ack=False)
        logger.info("Established async connection")
        return connection

    async def process_incoming_message(self, message):
        message.ack()
        body = message.body
        logger.info("Received message")
        if body:
            self.process_call(json.loads(body))

    def message_sent(self, message):
        self.channel.basic_publish(
            exchange="",
            routing_key=self.publish_queue_name,
            properties=pika.BasicProperties(reply_to=self.callback_queue),
            body=json.dumps(message),
        )
