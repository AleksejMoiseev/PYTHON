from dataclasses import dataclass, asdict
from datetime import datetime
from uuid import uuid4
from typing import Union, Optional


@dataclass
class Event:
    timestamp: Union[datetime, str]

    def __post_init__(self):
        self.timestamp = self.timestamp.strftime(
            '%Y-%m-%d %H:%M:%S'
        )

    def dict(self):
        return asdict(self)


@dataclass
class CampaignRunEvent(Event):
    campaign_id: int
    process_uuid: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()
        self.process_uuid = uuid4().hex


@dataclass
class Message:
    routing_key: str
    event: Event


if __name__ == '__main__':
    timestamp = datetime.utcnow()
    c = CampaignRunEvent(campaign_id=1, timestamp=timestamp)
    message = Message(event=c, routing_key='key')
    event = message.event.dict()
    print(event, message.routing_key)
