# WiFi Drone für Home Assistant

[English](README.md)

Die Integration verbindet Home Assistant mit der lokalen [WiFi Drone Bridge](https://github.com/seb5594/Home-Assistant-WiFi-Drone-App). Sie stellt eine Kamera mit MJPEG-Livebild und JPEG-Schnappschüssen bereit, dazu einen Binärsensor für den Videostream und Diagnosedaten zum Bridge- und Streamstatus.

1. Starte die Bridge mit konfigurierter Kamera-URL und einem API-Token.
2. Füge dieses Repository als Integration in HACS hinzu, sobald ein HACS-ZIP veröffentlicht ist. Für die manuelle Installation kopiere `custom_components/wifi_drone` in den Ordner `custom_components/` deiner Home-Assistant-Konfiguration.
3. Starte Home Assistant neu und füge unter **Einstellungen → Geräte & Dienste** die Integration **WiFi Drone** hinzu.
4. Gib die Bridge-URL und den API-Token an. Bei direkter Installation aus dem App-Repository lautet die URL `http://c3b88628-wifi-drone:8099`. Bei anderen App-Katalogen verwende den Hostnamen aus dem Info-Tab der App und Port 8099.

Voraussetzung ist Home Assistant ab Version 2025.4. URL und Token lassen sich in der Integration über **Neu konfigurieren** ändern. Verwende eine Bildentitätskarte mit aktivierter Live-Ansicht für das Kamerabild im Dashboard.

## Lizenz

Veröffentlicht unter der [MIT-Lizenz](LICENSE).
