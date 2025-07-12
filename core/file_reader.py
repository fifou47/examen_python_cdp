import asyncio
import logging

async def read_log_file(file_path: str, delay: float = 0.2):
    """Lit le fichier ligne par ligne de façon asynchrone avec un délai entre chaque ligne."""
    try:
        with open(file_path, 'r') as f:
            for raw in f:
                line = raw.strip()
                if line:
                    yield line
                await asyncio.sleep(delay)
    except FileNotFoundError:
        logging.error(f"Fichier '{file_path}' introuvable.")
        raise
    except Exception as e:
        logging.error(f"Erreur de lecture : {e}")
        raise