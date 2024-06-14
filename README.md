# Python Schulungsseite

Dieses Projekt ist eine umfassende Webanwendung zum Erlernen der Grundlagen von Python. Die Anwendung bietet eine Vielzahl von Ressourcen wie Grundlagen, Konzepte, Videos, ein Wiki und ein interaktives Quiz.

## Features

- **Grundlagen**: Lernen Sie die grundlegenden Konzepte der Python-Programmierung.
- **Konzepte**: Erfahren Sie mehr über fortgeschrittene Python-Konzepte.
- **Wiki**: Ein Nachschlagewerk für alle Python-bezogenen Fragen.
- **Videos**: Sehen Sie sich hilfreiche Videos an, um Ihre Python-Kenntnisse zu erweitern.
- **Quiz**: Testen Sie Ihr Wissen mit einem interaktiven Quiz, das Multiple-Choice-Fragen mit Erklärungen bietet.
- **Bibliotheken**: Entdecken Sie verschiedene Bibliotheken für Audio, Musik, Video, Fotos, Bilder, Grafik, berufliche Anwendungen und Hobbys.

## Installation

### Voraussetzungen

- Python 3.12 oder höher
- Flask
- SQLite

### Schritte

1. Klonen Sie das Repository:

   ```bash
   git clone https://github.com/IhrBenutzername/python-schulungsseite.git
   cd python-schulungsseite


Erstellen Sie ein virtuelles Environment und aktivieren Sie es:

python -m venv venv
source venv/bin/activate  # Auf Windows: venv\Scripts\activate

Installieren Sie die Abhängigkeiten:

pip install -r requirements.txt



Erstellen Sie die SQLite-Datenbank und fügen Sie die Fragen und Antworten hinzu:

python create_db.py


Starten Sie die Anwendung:

python app.py


Öffnen Sie Ihren Webbrowser und gehen Sie zu http://127.0.0.1:5000, um die Anwendung zu verwenden.

![image](https://github.com/kruemmel-python/Python-Schulungsseite/assets/169469747/fad251c6-c96c-47ff-918c-d2ed897c58d3)


Beispielinhalt der Datenbank
Das create_db.py-Skript erstellt die Datenbank und fügt Beispiel-Quizfragen und -antworten hinzu. Sie können das Skript anpassen, um weitere Fragen und Antworten hinzuzufügen.

API-Endpunkte
GET /
Startseite der Anwendung.

GET /impressum
Seite mit Impressumsinformationen.

GET /datenschutz
Seite mit Datenschutzinformationen.

GET /grundlagen
Übersichtsseite der grundlegenden Python-Konzepte.

GET /grundlagen/<topic>
Detailseite für ein spezifisches Thema der grundlegenden Python-Konzepte.

GET /konzepte
Übersichtsseite der fortgeschrittenen Python-Konzepte.

GET /konzepte/<topic>
Detailseite für ein spezifisches Thema der fortgeschrittenen Python-Konzepte.

GET /wiki
Nachschlagewerk für Python-bezogene Fragen.

GET /videos
Seite mit hilfreichen Videos zum Erlernen von Python.

GET /quiz
Startseite des interaktiven Quiz.

POST /quiz/<int:question_id>
Endpunkt zum Absenden einer Antwort und Laden der nächsten Frage.

GET /bibliotheken
Übersichtsseite der verschiedenen Bibliotheken.

GET /bibliotheken/<library>
Detailseite für eine spezifische Bibliothek.



