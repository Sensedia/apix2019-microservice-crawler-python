import os, json, pika
from datetime import datetime
from validators.schema_validator import validate
from services.crawler import amazon_processor, marisa_processor, pernambucanas_processor, zoom_processor

connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ['RABBIT_SERVER']))

channel = connection.channel()
channel.queue_declare(queue=os.environ['RABBIT_KIT_QUEUE'])
channel.queue_declare(queue='RABBIT_SUGGESTION_QUEUE')
channel.queue_declare(queue=os.environ['RABBIT_PRE_SPECIFICATION_QUEUE'])

def callback(ch, method, properties, body):
    if body is None:
        return
    
    kit = json.loads(body)
    if not validate(kit):
        return

    print('Received ' + str(kit))
    data = []
    now = datetime.now().isoformat()
      
    for specification in kit['specifications']:
        
        # amazon
        data += amazon_processor(kit, specification, now)

        # marisa
        data += marisa_processor(kit, specification, now)

        # pernambucanas
        data += pernambucanas_processor(kit, specification, now)

        # zoom
        data += zoom_processor(kit, specification, now)

    if (len(data) > 0):
        channel.basic_publish(exchange='', routing_key=os.environ['RABBIT_SUGGESTION_QUEUE'], body=json.dumps(data))
        print('Sending ' + str(len(data)) + ' suggestions')
    
    channel.basic_publish(exchange='', routing_key=os.environ['RABBIT_PRE_SPECIFICATION_QUEUE'], body=kit)
    print('Sending kit')

channel.basic_consume(queue=os.environ['RABBIT_KIT_QUEUE'], on_message_callback=callback, auto_ack=True)

print('Waiting for messages in "' + os.environ['RABBIT_KIT_QUEUE'] + '"')

channel.start_consuming()