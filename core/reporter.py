from fpdf import FPDF
from datetime import datetime

class Reporter:
    """Génère un rapport de synthèse des événements et alertes."""
    def __init__(self, summary: dict,
                 output_txt: str = 'reports/report.txt',
                 output_pdf: str = 'reports/report.pdf'):
        self.summary = summary
        self.output_txt = output_txt
        self.output_pdf = output_pdf

    def generate_txt(self):
        with open(self.output_txt, 'w') as f:
            f.write(f"Rapport généré le {datetime.now().isoformat()}\n")
            f.write("Total événements: {}\n".format(self.summary['total_events']))
            f.write("Événements critiques: {}\n".format(self.summary['critical_events']))
            f.write("Nombre d'alertes: {}\n".format(self.summary['alerts']))

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Rapport de Surveillance', ln=True)
        pdf.set_font('Arial', '', 12)
        for key, val in self.summary.items():
            pdf.cell(0, 8, f"{key.replace('_',' ').capitalize()}: {val}", ln=True)
        pdf.output(self.output_pdf)