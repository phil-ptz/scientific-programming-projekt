### Daten hinzufügen:

Ordner "data/AI" und "data/REAL" erstellen. Datensätze (Bilder) ind die entsprechenden Ordner kopieren.

# **Pflichtenheft: KI zur Erkennung von echten und KI-generierten Bildern**

## **1. Projektübersicht**
### **1.1 Projektziel**
Entwicklung eines Machine-Learning-Modells, das zwischen echten (von Menschen erstellten) und KI-generierten Bildern unterscheiden kann. Das Modell soll auf einem frei wählbaren Ansatz basieren (z. B. CNN, Transformer, GAN-basierte Klassifikation).

### **1.2 Anwendungsbereich**
- Erkennung von Deepfakes und synthetischen Bildern (z. B. generiert durch Stable Diffusion, DALL·E, MidJourney)
- Mögliche Einsatzgebiete: Forensik, Content-Moderation, Authentizitätsprüfung

---

## **2. Anforderungen**
### **2.1 Funktionale Anforderungen**
| **ID** | **Anforderung** | **Beschreibung** |
|--------|-----------------|------------------|
| FR-01  | Datensammlung   | Beschaffung eines ausgewogenen Datensatzes mit echten und KI-generierten Bildern. |
| FR-02  | Datenvorverarbeitung | Bereinigung, Normalisierung und Augmentierung der Bilddaten. |
| FR-03  | Modellauswahl    | Auswahl eines geeigneten ML/DL-Modells (z. B. CNN, Vision Transformer, Hybridmodell). |
| FR-04  | Modelltraining   | Training des Modells mit Trainings- und Validierungsdaten. |
| FR-05  | Evaluierung      | Bewertung der Modelleistung mittels Metriken (Accuracy, Precision, Recall, F1-Score, ROC-AUC). |
| FR-06  | Inferenz        | Bereitstellung einer Methode zur Klassifikation neuer Bilder (Echt vs. KI-generiert). |
| FR-07  | Interpretierbarkeit | Optional: Erklärbarkeit der Entscheidungen (z. B. mittels Grad-CAM, SHAP). |

### **2.2 Nicht-funktionale Anforderungen**
| **ID** | **Anforderung** | **Beschreibung** |
|--------|-----------------|------------------|
| NF-01  | Performance     | Das Modell soll eine Accuracy von mindestens 85% auf Testdaten erreichen. |
| NF-02  | Skalierbarkeit  | Das Modell sollte auf neuen Datensätzen anpassbar sein. |
| NF-03  | Laufzeit       | Inferenzzeit pro Bild < 500 ms (abhängig von Hardware). |
| NF-04  | Robustheit     | Das Modell sollte gegen kleine Bildmanipulationen robust sein. |

---

## **3. Projektplanung**
### **3.1 Meilensteine**
| **Meilenstein** | **Beschreibung** | **Zieltermin** |
|-----------------|------------------|----------------|
| M1 | Datensatzbeschaffung & -aufbereitung | [Datum] |
| M2 | Modellauswahl & -implementierung | [Datum] |
| M3 | Training & Hyperparameter-Optimierung | [Datum] |
| M4 | Evaluierung & Dokumentation | [Datum] |
| M5 | Präsentation & Abschluss | [Datum] |

### **3.2 Verantwortlichkeiten**
| **Rolle** | **Aufgabe** |
|-----------|-------------|
| Projektleitung | Koordination, Zeitmanagement |
| Datenverarbeitung | Datensammlung, Preprocessing |
| Modellentwicklung | Implementierung & Training |
| Evaluierung | Metriken, Testläufe |
| Dokumentation | Protokollierung, Präsentation |

---

## **4. Technische Spezifikationen**
### **4.1 Tools & Frameworks**
- **Programmiersprache:** Python
- **Bibliotheken:** TensorFlow/Keras, PyTorch, OpenCV, scikit-learn
- **Datenverarbeitung:** Pandas, NumPy
- **Visualisierung:** Matplotlib, Seaborn
- **Optional:** Weights & Biases (W&B) für Experiment-Tracking

### **4.2 Hardware**
- **Training:** GPU-Unterstützung (z. B. Google Colab, lokale GPU)
- **Inferenz:** CPU/GPU je nach Modellgröße

---

## **5. Risikoanalyse**
| **Risiko** | **Auswirkung** | **Gegenmaßnahme** |
|------------|---------------|-------------------|
| Unausgewogener Datensatz | Schlechte Generalisierung | Datenbalance prüfen, Augmentierung |
| Overfitting | Gute Trainings-, schlechte Testperformance | Regularisierung, Dropout, Cross-Validation |
| Hardware-Limitationen | Lange Trainingszeiten | Cloud-Ressourcen nutzen (Colab, AWS) |
| KI-generierte Bilder werden immer realistischer | Modell veraltet schnell | Aktuelle Datensätze verwenden |

---

## **6. Abnahmekriterien**
- Das Modell erreicht eine Accuracy ≥ 85% auf einem separaten Testset.
- Die Dokumentation ist vollständig (Code, Trainingsprotokolle, Evaluierung).
- Eine Demo (z. B. Jupyter Notebook oder Streamlit-App) liegt vor.

---

## **7. Projektabschluss**
- **Präsentation** der Ergebnisse (Metriken, Herausforderungen, Learnings)
- **Code- & Dokumentationsabgabe** (GitHub-Repository)
- **Reflexion** über mögliche Verbesserungen

---

**Genehmigt durch:** [Name]  
**Datum:** [Datum]  

---

Dieses Pflichtenheft dient als Grundlage für die Projektdurchführung. Änderungen werden im Team abgestimmt und dokumentiert.
