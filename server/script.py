import os
from core.models import Bild
from django.core.files import File

# Basisverzeichnisse
ordner_label_1 = 'data/real'
ordner_label_2 = 'data/fake'

print(os.getcwd())  # Aktuelles Arbeitsverzeichnis ausgeben

# Funktion zum Laden der Bilder
def lade_bilder(ordner, label):
    for dateiname in os.listdir(ordner):
        pfad = os.path.join(ordner, dateiname)
        if os.path.isfile(pfad) and dateiname.lower().endswith(('.jpg', '.jpeg', '.png')):
            with open(pfad, 'rb') as f:
                bild = Bild(label=label)
                bild.bild.save(dateiname, File(f), save=True)

# Bilder aus beiden Ordnern importieren
lade_bilder(ordner_label_1, label='real')
lade_bilder(ordner_label_2, label='fake')