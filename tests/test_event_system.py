import json
import unittest
from datetime import datetime, timedelta
from core.event import Event
from core.analyzer import EventAnalyzer

class TestEventSystem(unittest.TestCase):
    def setUp(self):
        self.analyzer = EventAnalyzer()
        self.base = datetime(2023,1,1,0,0,0)

    def make_event(self, seconds, level):
        ts = (self.base + timedelta(seconds=seconds)).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        data = {
            'timestamp': ts,
            'level': level,
            'node': 'n1',
            'component': 'c1',
            'event_id': 'id',
            'message': 'msg',
            'template': 't'
        }
        return Event.from_json(json.dumps(data))

    def test_alert_detected(self):
        for s in [0,10,20]:
            self.analyzer.process_event(self.make_event(s,'ERROR'))
        self.assertEqual(len(self.analyzer.alerts),1)

    def test_no_alert_if_far(self):
        for s in [0,40,80]:
            self.analyzer.process_event(self.make_event(s,'ERROR'))
        self.assertEqual(len(self.analyzer.alerts),0)

if __name__ == '__main__':
    unittest.main()