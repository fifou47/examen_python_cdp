import matplotlib.pyplot as plt

class EventVisualizer:
    """Visualisation des distributions d'événements."""
    @staticmethod
    def plot_event_distribution(events, output_path: str = 'reports/event_distribution.png'):
        levels = [e.level for e in events]
        plt.figure()
        plt.hist(levels, bins=len(set(levels)), rwidth=0.8)
        plt.title('Distribution des niveaux de log')
        plt.xlabel('Niveau')
        plt.ylabel('Fréquence')
        plt.tight_layout()
        plt.savefig(output_path)
        print(f"Graphique sauvegardé dans {output_path}")
