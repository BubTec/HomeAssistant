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
- **Retry Logic**: Automatic retry attempts for failed API calls
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

### 2. Installation
1. Copy the `FrostWarning.yaml` file to your Home Assistant configuration
2. Import the blueprint in Home Assistant
3. Create a new automation using this blueprint

### 3. Configuration

#### Required Settings
- **Frost API Key**: Your eiswarnung.de API key
- **Location Selection**: Choose from dropdown (Home, Work, Car 1, Car 2, Garage, Custom)
- **Location Coordinates**: Configure coordinates for each location type
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
The blueprint uses the German eiswarnung.de API to get accurate frost forecasts:
- **Level 1**: High risk - definitely need to scrape windshield
- **Level 2**: Medium risk - might need to scrape windshield
- **Level 0**: No risk - no scraping needed

### Location Selection
- Choose from predefined locations via dropdown
- Each location has its own coordinate settings
- Location name is included in notifications and logs
- Easy switching between different locations

### Fallback System
If the API fails:
1. System retries up to 3 times with configurable delays
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
frost_api_key: "your-api-key-here"
location_selection: "home"
home_latitude: 53.086273193359375
home_longitude: 8.839592933654785
car_temperature_sensor: sensor.car_outside_temperature
notification_targets:
  - entity_id: notify.mobile_app_iphone
warning_time: "07:30"
```

### Advanced Setup - Multiple Cars
```yaml
frost_api_key: "your-api-key-here"
location_selection: "car1"
car1_latitude: 53.086273193359375
car1_longitude: 8.839592933654785
car2_latitude: 53.087000000000000
car2_longitude: 8.840000000000000
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
retry_attempts: 5
retry_delay_seconds: 60
```

### Work Location Setup
```yaml
frost_api_key: "your-api-key-here"
location_selection: "work"
work_latitude: 52.5200
work_longitude: 13.4050
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
- Review logs for specific error messages

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
- Better error handling and retry logic
- Flexible location selection via dropdown
- Multiple predefined location types
- Rich notifications with actions
- Comprehensive logging
- Fallback sensor support

### 🔄 **Migration Steps**
1. Get API key from eiswarnung.de
2. Configure blueprint with your location settings
3. Test with fallback sensor first
4. Gradually replace old notifications
5. Monitor logs for any issues

## Support

For issues or questions:
1. Check the logs for detailed error messages
2. Verify all configuration settings
3. Test with minimal configuration first
4. Review Home Assistant documentation for notification setup

## License

This blueprint is provided as-is for educational and personal use. 