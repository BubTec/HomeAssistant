# Smart Frost & Ice Warning System

This Home Assistant blueprint provides intelligent frost and ice warnings based on weather data and temperature sensors. Perfect for car owners who want to know when they need to scrape ice from their windscreens, or anyone wanting frost protection alerts for plants and outdoor equipment.

## Features

- ❄️ **Two Warning Levels**: High risk (ice scraping definitely needed) and medium risk (possibly needed)
- 🌡️ **Multiple Temperature Sources**: Works with weather entities, temperature sensors, or both
- ⏰ **Flexible Scheduling**: Daily morning warnings plus optional hourly updates
- 📱 **Customizable Messages**: Personalize warning messages with temperature placeholders
- 🏠 **Location-Aware**: Add location names for personalized messages
- 📅 **Weekend Control**: Choose whether to include weekend warnings
- 🔄 **Real-time Updates**: Optional hourly temperature checks for changing conditions

## How It Works

1. **Temperature Collection**: Gets temperature from configured sensors or weather entities
2. **Risk Assessment**: Compares temperature against configurable thresholds
3. **Smart Notifications**: Sends appropriate warnings based on risk level and time
4. **History Logging**: Records temperature checks for debugging and history

## Configuration

### Required Settings

- **Weather Entity** OR **Temperature Sensor**: At least one temperature source
- **Notification Service**: Where to send the warnings

### Temperature Thresholds

- **High Risk** (default 0°C): Temperature below which ice scraping is definitely needed
- **Medium Risk** (default 3°C): Temperature below which ice scraping might be needed

### Timing Options

- **Warning Time** (default 07:00): When to send daily frost warnings
- **Weekend Warnings** (default false): Whether to warn on weekends
- **Hourly Checks** (default true): Real-time temperature monitoring

### Message Customization

Both warning messages support placeholders:
- `{temperature}`: Current temperature value
- `{location}`: Location name (if configured)

## Supported Temperature Sources

### Weather Entities
- **OpenWeatherMap**: `weather.openweathermap`
- **AccuWeather**: `weather.accuweather`
- **Weather.gov**: `weather.weather_gov_home`
- **DarkSky**: `weather.dark_sky`
- **Met.no**: `weather.met_no`

### Temperature Sensors
- **ESPHome/Tasmota**: `sensor.outdoor_temperature`
- **Z-Wave/Zigbee**: `sensor.garden_temperature`
- **Xiaomi**: `sensor.xiaomi_outdoor_temp`
- **Car Integration**: `sensor.car_outside_temperature`
- **Weather Station**: `sensor.weather_station_temp`

## Warning Examples

### High Risk (≤0°C)
```
❄️ High Frost Warning
High frost risk! You will definitely need to scrape ice 
from your windscreen before driving. Current temperature: -2°C
```

### Medium Risk (0°C to 3°C)
```
🌡️ Possible Frost Warning  
Possible frost risk! You might need to scrape ice from 
your windscreen. Current temperature: 1.5°C
```

### No Risk (>3°C)
```
☀️ No Frost Expected
Good news! No frost expected today. Temperature: 8°C
Weather: Partly cloudy
```

## Setup Instructions

1. **Import Blueprint**: Add the YAML file to your blueprints folder
2. **Create Automation**: Use the blueprint to create a new automation
3. **Configure Temperature Source**: Select weather entity or temperature sensor
4. **Set Thresholds**: Adjust temperature thresholds for your climate
5. **Choose Notification**: Select your preferred notification service
6. **Customize Messages**: Personalize warning messages if desired
7. **Test**: Set a future time and verify notifications work

## Advanced Configuration

### Multiple Location Setup
Create separate automations for different locations:
```yaml
# Home frost warning
Location Name: "at home"
Temperature Sensor: sensor.home_outdoor_temp

# Garage frost warning  
Location Name: "in the garage"
Temperature Sensor: sensor.garage_temperature
```

### Car Integration Example
```yaml
Weather Entity: weather.openweathermap
Temperature Sensor: sensor.car_outside_temperature
Location Name: "at your car"
High Risk Message: "🚗 Car frost alert! Scrape windscreen before driving. Temperature: {temperature}°C"
```

### Smart Thresholds by Season
Use different automations for winter/summer with different thresholds:
- **Winter**: High ≤-2°C, Medium ≤1°C
- **Summer**: High ≤0°C, Medium ≤3°C

## Notification Services

### Mobile Apps
```yaml
Notification Service: notify.mobile_app_yourphone
```

### TTS/Alexa
```yaml
Notification Service: tts.google_translate_say
# or
Notification Service: notify.alexa_media_echo_dot
```

### Multiple Services
Create multiple automations with the same settings but different notification services for redundancy.

## Temperature Source Priority

The blueprint uses this priority order:
1. **Temperature Sensor** (if configured and available)
2. **Weather Entity Current Temperature** (if sensor unavailable)
3. **Weather Entity Forecast** (if current temp unavailable)

## Troubleshooting

### Common Issues

1. **No Notifications**: 
   - Check if temperature source is providing valid data
   - Verify notification service is working
   - Check weekend settings if it's a weekend

2. **Wrong Temperature**:
   - Ensure sensor/weather entity is working correctly
   - Check logbook for temperature readings
   - Verify temperature sensor device class

3. **Too Many/Few Warnings**:
   - Adjust threshold temperatures
   - Disable hourly checks if too frequent
   - Check weekend warning setting

### Testing

1. **Manual Temperature Test**: Temporarily set threshold above current temperature
2. **Time Test**: Set warning time to a few minutes in the future
3. **Service Test**: Use Developer Tools → Services to test notification service

## Integration Examples

### With Plant Protection
```yaml
High Risk Message: "❄️ Frost warning! Protect your plants and scrape car windscreen. Temperature: {temperature}°C"
Medium Risk Message: "🌱 Light frost possible. Check sensitive plants and car windscreen. Temperature: {temperature}°C"
```

### With Pool/Garden Systems
```yaml
Location Name: "in the garden"
High Risk Message: "❄️ Hard frost warning! Turn off garden water and protect equipment. Temperature: {temperature}°C"
```

### With Smart Home Integration
Use with other automations:
- Turn on heated car seats when frost warning active
- Send notifications to family members
- Activate outdoor heating systems
- Close pool covers automatically

## Climate Adaptation

### Northern Climates
```yaml
High Frost Risk Threshold: -5°C
Medium Frost Risk Threshold: 0°C
```

### Mild Climates  
```yaml
High Frost Risk Threshold: 2°C
Medium Frost Risk Threshold: 5°C
```

### Desert/Dry Climates
```yaml
High Frost Risk Threshold: -2°C
Medium Frost Risk Threshold: 2°C
```

## Version History

- **v1.0**: Initial release with dual temperature sources and customizable thresholds
- Smart message templating with location awareness
- Hourly monitoring with weekend control
- Full weather entity and sensor support

## Credits

Converted from ioBroker EisScheibenWarnung script to Home Assistant blueprint, enhancing flexibility and adding international weather service support while maintaining the core frost detection functionality. 