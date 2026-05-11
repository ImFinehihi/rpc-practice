import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='hello')

print("Đang chờ message...")

def callback(ch, method, properties, body):
    print("Nhận được:", body.decode())

channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()
