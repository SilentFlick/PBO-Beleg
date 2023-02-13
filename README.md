# PBO-Beleg

Dies ist eine Plattform für Kommunikation und Erfahrungsaustausch, entwickelt mit VueJS und Python. Hinweis: Das Backend ist unvollständig und bietet nur einige Funktionen für das Frontend.

## Einrichtung

Um alle Abhängigkeiten zu installieren, sind `pip` und `npm` erforderlich. Stellen Sie daher sicher, dass

- `nodejs`
- `npm`
- `python`
- `pip`

bereits installiert sind. Führen Sie diese Befehle aus, um Abhängigkeiten zu installieren.

```
npm install
pip install --user -r requirements.txt
```

## Ausführung

Unter Linux können Sie das Shell-Skript `start.sh` ausführen, unter Mac OS/Windows müssen das Frontend und Backend manuell gestartet werden.

```
npm run dev
#Start Server
cd ./src/backend/
if [ -f pbo ]; then
rm pbo
fi
python3 main.py
```

Die Webseite befindet sich auf `localhost:8080`.
