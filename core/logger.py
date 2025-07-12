import logging
from .event import Event

class EventLogger:
    """Journalise les événements dans un fichier de log."""
    def __init__(self, filename: str = 'app.log'):
        logging.basicConfig(
            filename=filename,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger()

    def log_event(self, event: Event):
        msg = f"{event.node}/{event.component} - {event.message} (ID:{event.event_id})"
        if event.level in ['ERROR', 'CRITICAL']:
            self.logger.error(msg)
        elif event.level == 'WARN':
            self.logger.warning(msg)
        else:
            self.logger.info(msg)