import pika
import cv2
import pickle

class Config():
    """Basic RabbitMQ configuration"""

    def __init__(self):
        self.queue = 'json_data'
        self.guest = 'guest'
        self.cred = pika.PlainCredentials(self.guest, self.guest)
        self.params = pika.ConnectionParameters(host='127.0.0.1',
                                                port=5672,
                                                virtual_host='/',
                                                credentials=self.cred
                                               )
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(self.queue, durable=True)

class RabbitmqConsume(Config):

    def __init__(self):
        super().__init__()

    def basic_consume(self):
        def callback(ch, method, properties, body):
            """Will process a message."""

            data_deserialized = pickle.loads(body)

            image = data_deserialized["image"]
            width = data_deserialized["width"]
            height = data_deserialized["height"]
            filename = data_deserialized["filename"]

            new_filename = filename.rsplit('.')[0] + "_resize." + filename.rsplit('.')[1]

            image_resize = cv2.resize(image, (width, height))

            cv2.imwrite(new_filename, image_resize)

        self.channel.basic_consume(queue=self.queue,
                                   auto_ack=True,
                                   on_message_callback=callback
                                  )

    def start_consuming(self):
        """Waiting for messages."""
        self.channel.start_consuming()




