import json
from typing import List, Dict
from .event import Event

class EventAnalyzer:
    """Analyse les événements et détecte les anomalies (alertes)."""
    def __init__(self):
        self.events: List[Event] = []
        self.alerts: List[Dict] = []
        self.critical_levels = ["ERROR", "CRITICAL"]

    def process_event(self, event: Event):
        self.events.append(event)
        if event.level in self.critical_levels:
            self._check_alert()

    def _check_alert(self):
        crits = [e for e in self.events if e.level in self.critical_levels]
        if len(crits) < 3:
            return
        last_three = crits[-3:]
        delta = (last_three[-1].timestamp - last_three[0].timestamp).total_seconds()
        if delta <= 30:
            alert = {
                'id': f"ALERT-{len(self.alerts)+1}",
                'timestamp': last_three[-1].timestamp.isoformat(),
                'events': [
                    { 'time': e.timestamp.isoformat(), 'level': e.level,
                      'node': e.node, 'component': e.component,
                      'message': e.message } for e in last_three
                ]
            }
            self.alerts.append(alert)
            self._save_alerts()

    def _save_alerts(self, file_path: str = 'data/alerts.json'):
        with open(file_path, 'w') as f:
            json.dump(self.alerts, f, indent=2)

    def summary(self):
        total = len(self.events)
        critical = len([e for e in self.events if e.level in self.critical_levels])
        return { 'total_events': total, 'critical_events': critical, 'alerts': len(self.alerts) }