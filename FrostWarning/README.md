# German Ice Warning System (eiswarnung.de)

This Home Assistant blueprint provides professional ice warnings using the German eiswarnung.de API for accurate frost predictions. Perfect for German locations with precise windscreen scraping forecasts based on professional meteorological data.

## Features

- ❄️ **Professional Ice Forecasts**: Uses eiswarnung.de API for accurate German weather predictions
- 🎯 **Two Warning Levels**: Level 1 (ice scraping definitely needed), Level 2 (possibly needed)
- 🚗 **Car-Focused**: Specifically designed for windscreen ice warnings
- 🌡️ **Temperature Integration**: Optional local temperature sensor for additional context
- ⏰ **Smart Scheduling**: Morning warnings plus real-time updates when forecasts change
- 📱 **German Messages**: Native German notifications (customizable)
- 📅 **Weekend Control**: Choose whether to include weekend warnings

## Required Setup

### 1. Get eiswarnung.de API Key

1. Visit [eiswarnung.de](https://www.eiswarnung.de/) 
2. Register for an API account
3. Note your API key, latitude, and longitude

### 2. Configure RESTful Sensor

Add this to your `configuration.yaml`:

```yaml
rest:
  - resource: "https://api.eiswarnung.de?key=YOUR_API_KEY&lat=YOUR_LATITUDE&lng=YOUR_LONGITUDE"
    name: "Eiswarnung Forecast ID"
    scan_interval: 7200  # Update every 2 hours
    value_template: >
      {% if value_json.result is defined and value_json.result.forecastId is defined %}
        {{ value_json.result.forecastId }}
      {% else %}
        0
      {% endif %}
    unit_of_measurement: "level"
```

**Example for Munich:**
```yaml
rest:
  - resource: "https://api.eiswarnung.de?key=your_key_here&lat=48.1351&lng=11.5820"
    name: "Eiswarnung Forecast ID"
    scan_interval: 7200
    value_template: >
      {% if value_json.result is defined and value_json.result.forecastId is defined %}
        {{ value_json.result.forecastId }}
      {% else %}
        0
      {% endif %}
    unit_of_measurement: "level"
```

### 3. Restart Home Assistant

After adding the sensor configuration, restart Home Assistant to create the sensor.

### 4. Import and Configure Blueprint

- Import the blueprint
- Set **Eiswarnung Forecast Sensor** to `sensor.eiswarnung_forecast_id`
- Configure other options as needed

## Warning Levels

The eiswarnung.de API provides these forecast levels:

| Level | Meaning | Action |
|-------|---------|--------|
| **0** | No ice expected | No warning (optional good news message) |
| **1** | High ice risk | Definitely scrape windscreen |
| **2** | Medium ice risk | Possibly scrape windscreen |

## Configuration

### Required Settings

- **Eiswarnung Forecast Sensor**: `sensor.eiswarnung_forecast_id` (created above)
- **Notification Service**: Where to send warnings

### Optional Settings

- **Temperature Sensor**: Local temperature for additional context (car, garage, outdoor)
- **Location Name**: Personalize messages ("at your car", "in Munich")
- **Weekend Warnings**: Include/exclude weekend notifications
- **Custom Messages**: Modify warning texts

## Example Messages

### Level 1 (High Risk)
```
❄️ Eiswarnung Stufe 1!
Du musst heute die Scheiben kratzen, bevor du mit dem Auto fährst!
Die Temperatur bei deinem Auto liegt bei -3°C.
```

### Level 2 (Medium Risk)
```
🌡️ Eiswarnung Stufe 2!
Vielleicht musst du heute die Scheiben kratzen, bevor du mit dem Auto fährst!
Die Temperatur in der Garage liegt bei 1°C.
```

### Level 0 (No Risk)
```
☀️ Keine Eiswarnung
Gute Nachrichten! Heute ist kein Eis zu erwarten bei deinem Auto.
Temperatur: 8°C.
```

## Advanced Configuration

### Multiple Locations

Create separate sensors for different locations:

```yaml
rest:
  # Home location
  - resource: "https://api.eiswarnung.de?key=YOUR_KEY&lat=52.5200&lng=13.4050"
    name: "Eiswarnung Home"
    scan_interval: 7200
    value_template: "{{ value_json.result.forecastId if value_json.result.forecastId is defined else 0 }}"
  
  # Work location  
  - resource: "https://api.eiswarnung.de?key=YOUR_KEY&lat=48.1351&lng=11.5820"
    name: "Eiswarnung Work"
    scan_interval: 7200
    value_template: "{{ value_json.result.forecastId if value_json.result.forecastId is defined else 0 }}"
```

Then create separate automations for each location.

### Car Integration

Perfect for car temperature sensors:

```yaml
# Blueprint Configuration
Eiswarnung Forecast Sensor: sensor.eiswarnung_forecast_id
Temperature Sensor: sensor.car_outside_temperature  # VW Connect, BMW, etc.
Location Name: "bei deinem Auto"
```

### Garage/Carport Setup

```yaml
# Blueprint Configuration  
Temperature Sensor: sensor.garage_temperature
Location Name: "in der Garage"
High Risk Message: "❄️ Eiswarnung! Scheiben kratzen nötig. Garage: {temp_info}"
```

## Troubleshooting

### Common Issues

1. **No Sensor Data**:
   - Check if API key is valid
   - Verify latitude/longitude coordinates
   - Check Home Assistant logs for REST errors
   - Ensure sensor name matches blueprint configuration

2. **Wrong Location**:
   - Verify coordinates on a map
   - Use more precise decimal places
   - Check if coordinates are within Germany

3. **No Notifications**:
   - Test notification service separately
   - Check weekend warning settings
   - Verify trigger times

### Testing the Sensor

Check sensor status in Developer Tools:
- Go to **Developer Tools** → **States**
- Find `sensor.eiswarnung_forecast_id`
- Value should be 0, 1, or 2

### API Rate Limits

- Free tier: Limited requests per day
- Update interval: 2 hours recommended
- Avoid intervals under 1 hour

## German Coordinates Reference

| City | Latitude | Longitude |
|------|----------|-----------|
| Berlin | 52.5200 | 13.4050 |
| Munich | 48.1351 | 11.5820 |
| Hamburg | 53.5511 | 9.9937 |
| Cologne | 50.9375 | 6.9603 |
| Frankfurt | 50.1109 | 8.6821 |
| Stuttgart | 48.7758 | 9.1829 |
| Düsseldorf | 51.2277 | 6.7735 |
| Leipzig | 51.3397 | 12.3731 |

## Integration Examples

### With Smart Car Systems

```yaml
# Works great with:
- VW Connect (sensor.car_outside_temperature)
- BMW Connected Drive
- Mercedes me
- Tesla integration
```

### With Home Automation

```yaml
# Trigger other automations:
- Turn on heated car seats
- Activate garage heater  
- Send family notifications
- Start car warming systems
```

### With Weather Stations

```yaml
# Combine with local weather:
Temperature Sensor: sensor.outdoor_temperature
# Provides local vs. forecast comparison
```

## Version History

- **v1.0**: Initial release with eiswarnung.de API integration
- Professional German ice forecasting
- RESTful sensor configuration
- Level-based warning system

## Credits

Enhanced version of the original ioBroker EisScheibenWarnung script, maintaining the proven eiswarnung.de API while adding Home Assistant flexibility and modern automation features. 