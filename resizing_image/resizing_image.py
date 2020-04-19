from conf_resizing_rabbitmq import RabbitmqConsume

conf_rabbitmq = RabbitmqConsume()

if __name__ == '__main__':
    conf_rabbitmq.basic_consume()
    conf_rabbitmq.start_consuming()
