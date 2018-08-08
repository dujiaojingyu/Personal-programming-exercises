__author__ = "Narwhale"
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))     #建立一个socket

channel = connection.channel()  #声明一个管道，通过管道发消息
channel.queue_declare(queue='hello3',durable=True ) #声明queue，durable队列持久化
channel.basic_publish(
    exchange='',
    routing_key='hello3',
    body='Hello Woeld',
    properties = pika.BasicProperties(
    delivery_mode=2,)#消息持久化
)
print("[x] sent 'Hello Woeld'")
connection.close()