# main.py
import asyncio
import argparse
import json
import sys
from core.file_reader import read_log_file
from core.event import Event
from core.analyzer import EventAnalyzer
from core.logger import EventLogger
from core.reporter import Reporter
from core.visualizer import EventVisualizer

async def run_processing(analyzer: EventAnalyzer, logger: EventLogger, path: str):
    events = []
    try:
        async for line in read_log_file(path):
            try:
                event = Event.from_json(line)
                analyzer.process_event(event)
                logger.log_event(event)
                events.append(event)
            except json.JSONDecodeError as e:
                print(f"Ignoré (JSON invalide): {e}")
    except Exception as e:
        print(f"Erreur lors du traitement: {e}")
    return events

async def main():
    parser = argparse.ArgumentParser(description="Système de surveillance des événements logs")
    parser.add_argument("--start", action="store_true", help="Lancer le traitement complet")
    parser.add_argument("--alerts", action="store_true", help="Afficher les alertes détectées")
    parser.add_argument("--report", action="store_true", help="Générer le rapport TXT et PDF")
    parser.add_argument("--plot", action="store_true", help="Visualiser la distribution des événements")
    args = parser.parse_args()

    analyzer = EventAnalyzer()
    logger = EventLogger()
    events = []

    if args.start:
        print("Lancement du traitement...")
        events = await run_processing(analyzer, logger, 'data/events.log')
        print(f"Traitement terminé. {len(events)} événements traités.")

    if args.alerts:
        print("--- ALERTES DÉTECTÉES ---")
        if not analyzer.alerts:
            print("Aucune alerte détectée.")
        for a in analyzer.alerts:
            print(json.dumps(a, indent=2))

    if args.report:
        print("Génération du rapport...")
        summary = analyzer.summary()
        reporter = Reporter(summary)
        reporter.generate_txt()
        reporter.generate_pdf()
        print("Rapport TXT et PDF générés dans reports/.")

    if args.plot:
        if not events:
            print("Aucun événement chargé. Utilisez --start d'abord.")
        else:
            EventVisualizer.plot_event_distribution(events)

    if not any(vars(args).values()):
        parser.print_help()

if __name__ == '__main__':
    asyncio.run(main())
