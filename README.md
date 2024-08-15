Webscraper.py ist auf https://aisel.aisnet.org/wi2023/ eingestellt.

Funktionen :  - Automatisches Maximieren des Chrome Drivers
              - Cookie auswahl bestätigen
              - Auf PDF button zum Herunterladen in PDF Verzeichnis klicken

Verbesserung: - Chrome Driver beendet augenblicklich nach anklicken von jeder Datei, ohne zu überprüfen ob Dateien fertig heruntergeladen sind.
                Versuche den aktuellen If-try Block aufzulösen, um eine While-true schleife zum Aufrufen der Links zu erzeugen,
                haben bisher dazu geführt, dass die erste Datei heruntergeladen wird und dann stoppt.
