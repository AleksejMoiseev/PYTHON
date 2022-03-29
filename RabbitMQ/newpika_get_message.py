import pika

credentials = pika.PlainCredentials(username='user', password='password')
parameters = pika.ConnectionParameters(host='127.0.0.1', port=5672, credentials=credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
method_frame, header_frame, body = channel.basic_get('first')


if method_frame:
    print(method_frame, header_frame, body)
    channel.basic_ack(method_frame.delivery_tag)
else:
    print('No message returned')