import json
from datetime import datetime

class Event:
    """Représente un événement issu du log."""
    def __init__(self, timestamp: datetime, level: str, node: str,
                 component: str, event_id: str, message: str, template: str):
        self.timestamp = timestamp
        self.level = level.upper()
        self.node = node
        self.component = component
        self.event_id = event_id
        self.message = message
        self.template = template

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        ts = datetime.strptime(data['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
        return cls(
            timestamp=ts,
            level=data['level'],
            node=data['node'],
            component=data['component'],
            event_id=data.get('event_id', data.get('id', '')),
            message=data['message'],
            template=data['template']
        )