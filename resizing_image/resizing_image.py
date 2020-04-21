from conf_resizing_rabbitmq import RabbitmqConsume

conf_rabbitmq = RabbitmqConsume()

def run_resizing():
    conf_rabbitmq.basic_consume()
    conf_rabbitmq.start_consuming()


run_resizing()
