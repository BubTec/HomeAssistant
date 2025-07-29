# Frost Warning Blueprint

Ein Home Assistant Blueprint für automatische Eiswarnungen basierend auf der eiswarnung.de API.

## ⚠️ **Wichtiger Hinweis: REST-Sensor Setup erforderlich**

Dieser Blueprint benötigt einen **REST-Sensor** für die echte API-Integration. Ohne diesen Sensor werden nur Test-Nachrichten gesendet.

## 🔧 **REST-Sensor Setup (Erforderlich)**

### **1. Füge folgenden Code zu deiner `configuration.yaml` hinzu:**

```yaml
# REST-Sensor für eiswarnung.de API
sensor:
  - platform: rest
    name: "Frost Warning API"
    unique_id: "frost_warning_api"
    resource_template: >-
      https://api.eiswarnung.de?key=DEIN_API_KEY&lat={{ state_attr('device_tracker.skoda_superb_combi_standort', 'latitude') }}&lng={{ state_attr('device_tracker.skoda_superb_combi_standort', 'longitude') }}
    scan_interval: 3600  # Alle Stunde
    timeout: 10
    value_template: "{{ value_json.result.forecastId }}"
    json_attributes_path: "$.result"
    json_attributes:
      - "forecastId"
      - "description"
    headers:
      User-Agent: "Home Assistant"
```

### **2. Ersetze `DEIN_API_KEY` und `device_tracker.skoda_superb_combi_standort`:**

```yaml
# Beispiel mit deinen Daten:
sensor:
  - platform: rest
    name: "Frost Warning API"
    unique_id: "frost_warning_api"
    resource_template: >-
      https://api.eiswarnung.de?key=62fd0be7c6a10f7fa6979f1299c1448b&lat={{ state_attr('device_tracker.skoda_superb_combi_standort', 'latitude') }}&lng={{ state_attr('device_tracker.skoda_superb_combi_standort', 'longitude') }}
    scan_interval: 3600
    timeout: 10
    value_template: "{{ value_json.result.forecastId }}"
    json_attributes_path: "$.result"
    json_attributes:
      - "forecastId"
      - "description"
    headers:
      User-Agent: "Home Assistant"
```

### **3. Home Assistant neu starten**

Nach dem Hinzufügen des Sensors:
1. **Konfiguration** → **Server-Steuerung** → **Neu starten**
2. Warte bis Home Assistant wieder läuft
3. Prüfe ob der Sensor `sensor.frost_warning_api` existiert

## 📱 **Blueprint Features**

- ✅ **Echte API-Integration** (mit REST-Sensor)
- ✅ **Intelligente Benachrichtigungen** - Nur bei Frost (Level 1 oder 2)
- ✅ **Geräte-spezifische Nachrichten** - Direkt an dein Handy
- ✅ **GPS-Integration** - Automatische Koordinaten vom Device Tracker
- ✅ **Deutsche Texte** - Vollständig lokalisiert
- ✅ **Anpassbare Nachrichten** - Title und Text konfigurierbar

## 🎯 **Frost-Level Bedeutung**

- **Level 0**: Kein Frost → Keine Benachrichtigung
- **Level 1**: Frost → "Du musst heute kratzen!"
- **Level 2**: Möglicher Frost → "Du musst eventuell kratzen!"

## 🧪 **Installation**

1. **REST-Sensor** in `configuration.yaml` hinzufügen (siehe oben)
2. **Home Assistant neu starten**
3. **Blueprint importieren**
4. **Automatisierung erstellen** mit deinen Einstellungen

## ⚙️ **Blueprint Konfiguration**

- **Frost API Key**: Dein eiswarnung.de API-Schlüssel
- **Location Device**: Device Tracker mit GPS-Koordinaten
- **Notification Targets**: Dein Handy für Benachrichtigungen
- **Notification Title**: "Eis Warnung!" (anpassbar)
- **Warning Message**: Nachrichtentext (anpassbar)
- **Warning Time**: Uhrzeit für tägliche Prüfung
- **Warning Days**: Wochentage für Warnungen

## 🔍 **Troubleshooting**

### **Problem: Keine Benachrichtigungen**
- Prüfe ob `sensor.frost_warning_api` existiert
- Prüfe Sensor-Wert: sollte 0, 1 oder 2 sein
- Prüfe API-Key und GPS-Koordinaten

### **Problem: Sensor zeigt "unavailable"**
- Prüfe API-Key in `configuration.yaml`
- Prüfe Internet-Verbindung
- Prüfe Device Tracker hat GPS-Koordinaten

### **Problem: Benachrichtigung an falsches Gerät**
- Prüfe Device-ID in Blueprint-Konfiguration
- Teste mit einfacher Benachrichtigung

## 📝 **Beispiel-Benachrichtigung**

**Bei Frost (Level 1):**
```
Title: "Eis Warnung!"
Message: "Du musst heute kratzen! Frost-Level: 1, Standort: Škoda Superb Combi Standort"
```

**Bei möglichem Frost (Level 2):**
```
Title: "Eis Warnung!"
Message: "Du musst eventuell kratzen! Frost-Level: 2, Standort: Škoda Superb Combi Standort"
```

## 🚀 **Nächste Schritte**

Nach der Installation des REST-Sensors wird der Blueprint echte Frost-Daten abrufen und nur bei tatsächlichem Frost benachrichtigen. 