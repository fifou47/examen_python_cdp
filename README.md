# Système de Surveillance Intelligente de Logs


Système d'analyse de logs en temps quasi-réel avec détection d'anomalies, génération de rapports et visualisation statistique.

##  Installation

1. **Cloner le dépôt** :
```bash
   git clone https://github.com/fifo47/examen_python_cdp.git
   cd examen_python_cdp
```
Création d'un environnement python 


```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Installlation des dépendances requises

```bash
 pip install -r requirements.txt
```

Commande CLI principal

```bash
# Traitement complet (lecture + analyse + rapports)

# Afficher les alertes détectées

# Générer les rapports (TXT + PDF)

# Générer la visualisation statistique

python main.py --start --alerts  --report --plot
```

# Fonctionnalités
## 1. Lecture asynchrone
Lit les logs ligne par ligne avec délai de 2s

Supporte les formats JSON complexes

Gestion robuste des erreurs de lecture

## 2. Détection d'anomalies
Alerte après 3 événements ERROR/CRITICAL en ≤30s

Journalisation précise dans app.log

Stockage des alertes dans alerts.json

## 3. Génération de rapports
Rapport texte : Statistiques basiques

Rapport PDF : Version formatée avec FPDF

Contenu :

Nombre total d'événements

Événements critiques

Alertes détectées

Horodatages des alertes

## 4. Visualisation
Histogramme des niveaux de log

Export PNG automatique

Légendes claires et mise en page professionnelle
