## 🛠️ Entwicklung & Zusammenarbeit

Damit unser Projekt sauber läuft und wir uns nicht gegenseitig den Code überschreiben, nutzen wir diesen Workflow:

### 1. Projekt lokal starten
Bevor du startest, stelle sicher, dass du Streamlit installiert hast.
1. Repository klonen (falls noch nicht geschehen).
2. Terminal im Projektordner öffnen.
3. Die App starten mit:
   ```bash
   streamlit run main.py
   
2. So arbeitest du an Features (Git-Workflow)

Bitte arbeite niemals direkt auf dem main-Branch. Nutze stattdessen Feature-Branches:

    Update holen: Stelle sicher, dass dein lokaler Stand aktuell ist:
    Bash

    git checkout main
    git pull origin main

    Neuen Branch erstellen: Erstelle einen Zweig für deine Aufgabe (z.B. ein neues Spiel):
    Bash

    git checkout -b feature/mein-neues-spiel

    Änderungen speichern: Wenn du fertig bist, speichere deine Arbeit:
    Bash

    git add .
    git commit -m "Beschreibung: Spiel X hinzugefügt"

    Hochladen: Schiebe deinen Branch zu GitHub:
    Bash

    git push origin feature/mein-neues-spiel

    Pull Request: Gehe auf GitHub und erstelle einen "Pull Request". Sobald dieser geprüft wurde, wird er in den main gemergt.1