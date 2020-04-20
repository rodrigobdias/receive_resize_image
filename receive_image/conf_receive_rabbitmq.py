import pika

class Config():
    """Basic RabbitMQ configuration"""

    def __init__(self):
        self.queue = 'json_data'
        self.guest = 'guest'
        self.host = 'rabbitmq'
        self.port = 5672
        self.virtual_host = '/'

        self.cred = pika.PlainCredentials(self.guest, self.guest)
        self.params = pika.ConnectionParameters(host=self.host,
                                                port=self.port,
                                                virtual_host=self.virtual_host,
                                                credentials=self.cred
                                               )
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(self.queue, durable=True)

class RabbitmqPublish(Config):

    def __init__(self):
        super().__init__()

    def basic_publish(self, json_data_serialized):
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue,
                                   body=json_data_serialized,
                                   properties=pika.BasicProperties(
                                   delivery_mode=2,  # make message persistent
                                  ))







