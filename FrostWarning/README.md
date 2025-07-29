# Frost Warning Blueprint

A modern Home Assistant blueprint for frost warnings with flexible configuration and robust error handling. This blueprint replaces the old ioBroker script with a more reliable and feature-rich solution.

## Features

### 🔧 **Flexible Configuration**
- **API Key Management**: Secure API key input (no hardcoded values)
- **Location Selection**: Dropdown menu to select from predefined locations (Home, Work, Car 1, Car 2, Garage, Custom)
- **Multiple Notification Targets**: Support for various notification services
- **Customizable Messages**: Personalized notification titles and content
- **Flexible Scheduling**: Configurable warning times and days of the week

### 🛡️ **Robust Error Handling**
- **REST Sensor Integration**: Uses Home Assistant REST sensors for reliable API calls
- **Fallback Sensors**: Local temperature sensor backup when API fails
- **Comprehensive Logging**: Detailed logs for debugging and monitoring
- **Graceful Degradation**: System continues working even with API issues

### 📱 **Modern Notifications**
- **Rich Notifications**: Support for sounds, channels, and click actions
- **Multiple Platforms**: iOS, Android, and other notification services
- **Dashboard Integration**: Click notifications to open relevant dashboards
- **Priority Handling**: High-priority alerts for important warnings

## Setup

### 1. Prerequisites
- Home Assistant instance
- API key from [eiswarnung.de](https://eiswarnung.de)
- Temperature sensor (optional, for fallback)

### 2. REST Sensor Setup

**IMPORTANT**: You need to create a REST sensor first in your `configuration.yaml`:

```yaml
# Add this to your configuration.yaml
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

**Example for your location:**
```yaml
rest:
  - resource: "https://api.eiswarnung.de?key=your_key_here&lat=53.086273193359375&lng=8.839592933654785"
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

### 3. Installation
1. Add the REST sensor to your `configuration.yaml`
2. Restart Home Assistant
3. Copy the `FrostWarning.yaml` file to your Home Assistant configuration
4. Import the blueprint in Home Assistant
5. Create a new automation using this blueprint

### 4. Configuration

#### Required Settings
- **Frost API Key**: Your eiswarnung.de API key (used in REST sensor)
- **Location Selection**: Choose from dropdown (Home, Work, Car 1, Car 2, Garage, Custom)
- **Location Coordinates**: Configure coordinates for each location type
- **Frost Forecast Sensor**: Select the REST sensor you created (e.g., `sensor.eiswarnung_forecast_id`)
- **Car Temperature Sensor**: Temperature sensor for your car (optional but recommended)
- **Notification Targets**: Where to send warnings

#### Location Configuration
The blueprint supports multiple predefined locations:

| Location | Description | Use Case |
|----------|-------------|----------|
| **Home** | Your home address | General frost warnings |
| **Work** | Your workplace | Commute-related warnings |
| **Car 1** | Primary vehicle location | Main car frost warnings |
| **Car 2** | Secondary vehicle location | Second car or family car |
| **Garage** | Garage or carport location | Indoor/covered parking |
| **Custom** | Custom coordinates | Any other location |

#### Optional Settings
- **Warning Time**: When to send daily warnings (default: 07:30)
- **Warning Days**: Which days to send warnings (default: Monday-Friday)
- **Update Interval**: How often to check for frost (default: 2 hours)
- **Fallback Settings**: Local sensor configuration for API failures

## How It Works

### API Integration
The blueprint uses a REST sensor to get frost forecasts from eiswarnung.de:
- **Level 1**: High risk - definitely need to scrape windshield
- **Level 2**: Medium risk - might need to scrape windshield
- **Level 0**: No risk - no scraping needed

### Location Selection
- Choose from predefined locations via dropdown
- Each location has its own coordinate settings
- Location name is included in notifications and logs
- Easy switching between different locations

### Fallback System
If the REST sensor fails:
1. System checks if fallback sensor is enabled
2. Falls back to local temperature sensor if enabled
3. Uses configurable temperature threshold (default: 3°C)
4. Logs all attempts and failures for debugging

### Notification System
- Sends rich notifications with custom sounds and channels
- Includes location name and car temperature information
- Click notifications open specified dashboard views
- Supports multiple notification targets simultaneously

## Configuration Examples

### Basic Setup - Home Location
```yaml
# In configuration.yaml
rest:
  - resource: "https://api.eiswarnung.de?key=your-api-key&lat=53.086273193359375&lng=8.839592933654785"
    name: "Eiswarnung Forecast ID"
    scan_interval: 7200
    value_template: >
      {% if value_json.result is defined and value_json.result.forecastId is defined %}
        {{ value_json.result.forecastId }}
      {% else %}
        0
      {% endif %}
    unit_of_measurement: "level"

# Blueprint Configuration
location_selection: "home"
home_latitude: 53.086273193359375
home_longitude: 8.839592933654785
frost_forecast_sensor: sensor.eiswarnung_forecast_id
car_temperature_sensor: sensor.car_outside_temperature
notification_targets:
  - entity_id: notify.mobile_app_iphone
warning_time: "07:30"
```

### Advanced Setup - Multiple Cars
```yaml
# Blueprint Configuration
location_selection: "car1"
car1_latitude: 53.086273193359375
car1_longitude: 8.839592933654785
car2_latitude: 53.087000000000000
car2_longitude: 8.840000000000000
frost_forecast_sensor: sensor.eiswarnung_forecast_id
car_temperature_sensor: sensor.car_outside_temperature
notification_targets:
  - entity_id: notify.mobile_app_iphone
  - entity_id: notify.alexa_media
notification_title: "❄️ Frost Warning!"
dashboard_view: "/dashboard-home/car"
warning_time: "06:45"
warning_days: [1, 2, 3, 4, 5, 6, 7]  # Every day
update_interval_hours: 1
enable_fallback_sensor: true
fallback_temperature_threshold: 2.5
```

### Work Location Setup
```yaml
# Blueprint Configuration
location_selection: "work"
work_latitude: 52.5200
work_longitude: 13.4050
frost_forecast_sensor: sensor.eiswarnung_forecast_id
car_temperature_sensor: sensor.car_outside_temperature
notification_targets:
  - entity_id: notify.mobile_app_iphone
warning_time: "06:30"
warning_days: [1, 2, 3, 4, 5]  # Weekdays only
```

## Multiple Location Setup

You can create multiple automations for different locations:

### Example: Home and Work Warnings
1. **Home Automation**:
   - Location Selection: "Home"
   - Warning Time: "07:30"
   - Warning Days: [1, 2, 3, 4, 5, 6, 7]

2. **Work Automation**:
   - Location Selection: "Work"
   - Warning Time: "06:30"
   - Warning Days: [1, 2, 3, 4, 5]

### Example: Multiple Cars
1. **Primary Car**:
   - Location Selection: "Car 1"
   - Notification Title: "❄️ Car 1 Frost Warning!"

2. **Secondary Car**:
   - Location Selection: "Car 2"
   - Notification Title: "❄️ Car 2 Frost Warning!"

## Troubleshooting

### API Issues
- Check your API key is valid
- Verify coordinates are correct for selected location
- Check network connectivity
- Review REST sensor status in Developer Tools

### REST Sensor Issues
- Ensure REST sensor is properly configured in `configuration.yaml`
- Check sensor status: Developer Tools → States → `sensor.eiswarnung_forecast_id`
- Verify sensor value is 0, 1, or 2
- Check Home Assistant logs for REST errors

### Location Issues
- Ensure coordinates are set for the selected location
- Verify coordinates are within Germany (for eiswarnung.de API)
- Check location name appears correctly in notifications

### Notification Problems
- Ensure notification services are properly configured
- Check notification permissions on mobile devices
- Verify notification channel settings for Android

### Fallback Sensor Issues
- Confirm sensor entity ID is correct
- Check sensor is reporting valid temperature values
- Adjust temperature threshold if needed

## Migration from ioBroker

This blueprint replaces the old ioBroker script with several improvements:

### ✅ **Improvements**
- Modern Home Assistant integration
- Better error handling with REST sensors
- Flexible location selection via dropdown
- Multiple predefined location types
- Rich notifications with actions
- Comprehensive logging
- Fallback sensor support

### 🔄 **Migration Steps**
1. Get API key from eiswarnung.de
2. Create REST sensor in `configuration.yaml`
3. Configure blueprint with your location settings
4. Test with fallback sensor first
5. Gradually replace old notifications
6. Monitor logs for any issues

## Support

For issues or questions:
1. Check the logs for detailed error messages
2. Verify REST sensor configuration
3. Test with minimal configuration first
4. Review Home Assistant documentation for notification setup

## License

This blueprint is provided as-is for educational and personal use. 