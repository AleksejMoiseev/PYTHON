from kombu import Exchange, Queue
from message_bus.shema import BrokerScheme
from message_bus.instapubliser import KombuPublisher
from message_bus.message import CampaignRunEvent, Message
from message_bus.interfaces import Publisher
from datetime import datetime

media_exchange = Exchange('media', 'direct', durable=True)
video_queue = Queue('video', exchange=media_exchange, routing_key='video')
image_queue = Queue('image', exchange=media_exchange, routing_key='image')

schema = BrokerScheme(
    video_queue, image_queue
)


# # connections
# with Connection('amqp://user:password@localhost//') as conn:
#
#     # produce
#     producer = conn.Producer(serializer='json')
#     producer.publish({'name': '/tmp/lolcat1.avi', 'size': 2301013},
#                       exchange=media_exchange, routing_key='video',
#                       declare=[video_queue, image_queue])


class InstaPublisher:

    def __init__(self, publisher: Publisher, routing_key: str):
        self._publisher = publisher
        self._routing_key = routing_key

    def _publish(self, message: Message) -> None:
        with self._publisher as publisher:
            publisher.publish(message)

    def make_message_for_start_processing(self, campaign_id: int) -> Message:
        timestamp = datetime.utcnow()
        event = CampaignRunEvent(campaign_id=campaign_id, timestamp=timestamp)
        return Message(event=event, routing_key=self._routing_key)

    def publish_message(self,  campaign_id: int):
        message = self.make_message_for_start_processing(campaign_id=campaign_id)
        self._publish(message)






if __name__ == '__main__':
    # print(schema.queues())
    #print(schema.exchange(routing_key='video'))
    # timestamp = datetime.utcnow()
    # campaign = CampaignRunEvent(campaign_id=1, timestamp=timestamp)
    # message = Message(event=campaign, routing_key='video')
    publisher = KombuPublisher(
    scheme=schema,
    rabbit_url='amqp://user:password@localhost//')
    # with publisher as publisher:
    #     publisher.publish(message)

    insta_publisher = InstaPublisher(
        publisher=publisher,
        routing_key='video'
    )

    insta_publisher.publish_message(
        campaign_id=2
    )