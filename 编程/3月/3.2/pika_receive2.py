__author__ = "Narwhale"
import pika,time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello3',durable=True)#durable队列持久化

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # time.sleep(30)
    print('-->',ch,method,properties)
    ch.basic_ack(delivery_tag=method.delivery_tag) #用途是当客户端1突然断开链接，rebbitMQ会将未处理完的消息传给客户端2
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='hello3',

                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()