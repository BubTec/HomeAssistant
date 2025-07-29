# Cat Litter Box Counter Blueprint for Home Assistant

This blueprint converts the ioBroker cat litter box monitoring system to Home Assistant, providing comprehensive tracking of cat litter box usage, cleaning reminders, and tool monitoring.

## Features

- **Usage Tracking**: Counts how many times the litter box is used
- **Smart Presence Detection**: Distinguishes between actual usage and brief movements
- **Cleaning Reminders**: Automated notifications when cleaning is needed
- **Tool Monitoring**: Tracks cleaning tool usage and reminds if left open
- **Random Notification Messages**: Fun and varied reminder messages
- **Inactivity Alerts**: Warns if the litter box hasn't been used for 48+ hours
- **Configurable Thresholds**: Customize all timing and count parameters

## Required Home Assistant Helpers

Before using this blueprint, you need to create the following helpers in Home Assistant:

### 1. Counter Helpers (Settings → Devices & Services → Helpers → Create Helper → Counter)
- `counter.cat_litter_usage` - Tracks current usage since last cleaning
- `counter.cat_litter_total` - Tracks total usage ever
- `counter.cat_litter_cleanings` - Tracks number of cleanings performed

### 2. Input Boolean Helpers (Settings → Devices & Services → Helpers → Create Helper → Toggle)
- `input_boolean.cat_litter_needs_cleaning` - Indicates if cleaning is needed
- `input_boolean.cat_cleaning_tool_alert` - Tracks if cleaning tool is left open
- `input_boolean.cat_presence_detected` - Internal state for presence detection

### 3. Required Sensors
You need to have these sensors in your Home Assistant:
- **Cat Door Sensor**: Binary sensor that detects movement at the litter box (e.g., motion sensor, door sensor)
- **Cleaning Tool Sensor**: Binary sensor that detects when the cleaning tool is taken/opened (e.g., contact sensor on tool storage)

## Setup Instructions

### 1. Create Helper Entities
```yaml
# Add to configuration.yaml if creating manually:

counter:
  cat_litter_usage:
    name: "Cat Litter Usage Count"
    icon: mdi:cat
    
  cat_litter_total:
    name: "Cat Litter Total Usage"
    icon: mdi:counter
    
  cat_litter_cleanings:
    name: "Cat Litter Cleanings"
    icon: mdi:broom

input_boolean:
  cat_litter_needs_cleaning:
    name: "Cat Litter Needs Cleaning"
    icon: mdi:alert-circle
    
  cat_cleaning_tool_alert:
    name: "Cleaning Tool Alert"
    icon: mdi:tools
    
  cat_presence_detected:
    name: "Cat Presence Detected"
    icon: mdi:cat
```

### 2. Install the Blueprint
1. Copy the `CatShitCounter.yaml` file to your Home Assistant `blueprints/automation/` folder
2. Or import via the Home Assistant UI using the GitHub raw URL

### 3. Create Automation from Blueprint
1. Go to Settings → Automations & Scenes → Blueprints
2. Find "Cat Litter Box Counter and Monitor"
3. Click "Create Automation"
4. Configure the following inputs:

#### Required Inputs:
- **Cat Door Occupancy Sensor**: Your motion/door sensor at the litter box
- **Cleaning Tool Contact Sensor**: Sensor that detects when cleaning tool is taken
- **Usage Counter Helper**: `counter.cat_litter_usage`
- **Total Usage Counter Helper**: `counter.cat_litter_total`
- **Cleaning Counter Helper**: `counter.cat_litter_cleanings`
- **Needs Cleaning Boolean Helper**: `input_boolean.cat_litter_needs_cleaning`
- **Cleaning Tool Alert Boolean Helper**: `input_boolean.cat_cleaning_tool_alert`
- **Cat Presence Detection Helper**: `input_boolean.cat_presence_detected`

#### Optional Configuration:
- **Notification Service**: Default is `notify.persistent_notification`
- **Usage Warning Threshold**: Default is 4 uses
- **Presence Threshold**: Default is 30 seconds
- **Visit Duration**: Default is 120 seconds
- **Cleaning Completion Time**: Default is 45 seconds

## How It Works

### Usage Detection Logic
1. Cat enters litter box → motion sensor triggers
2. System waits for presence threshold (30s) to confirm cat is actually using the box
3. When cat leaves → motion sensor goes off
4. System waits for visit duration (2 minutes) to ensure visit is complete
5. Usage counters are incremented

### Cleaning Detection
1. Cleaning tool sensor opens → cleaning process starts
2. System waits for completion time (45s) to confirm actual cleaning
3. If tool is still open after completion time → counters reset, cleaning logged
4. Hourly reminders if tool is left open

### Notifications
- **Warning notifications** when usage count reaches threshold
- **Hourly reminders** during daytime hours (9 AM - 10 PM) if cleaning needed
- **Tool alerts** if cleaning tool is left open
- **Inactivity warnings** if no usage detected for 48+ hours

## Example Notification Messages
The system includes randomized, fun notification messages:
- "A message from your cat: MEOW! Please clean my litter box. I've used it 4 times already."
- "Hey human, 4 times used and no fresh litter? I think I'll smell this tomorrow too!"
- "The litter box is crying: Used 4 times and still no fresh litter? Where's the service?"

## Customization

### Notification Services
You can use any Home Assistant notification service:
- `notify.mobile_app_your_phone` - For mobile notifications
- `notify.alexa_media_echo_device` - For Alexa announcements
- `notify.telegram` - For Telegram messages

### Timing Adjustments
All timing parameters are configurable in the blueprint:
- **Presence Threshold**: Minimum time to register presence (10-120 seconds)
- **Visit Duration**: Wait time after presence ends (30-300 seconds)
- **Warning Threshold**: Number of uses before warning (1-10)
- **Cleaning Completion Time**: Time tool must be open to register cleaning (15-180 seconds)

## Dashboard Cards

Add these cards to your dashboard to monitor the system:

```yaml
type: entities
title: Cat Litter Box Monitor
entities:
  - counter.cat_litter_usage
  - counter.cat_litter_total
  - counter.cat_litter_cleanings
  - input_boolean.cat_litter_needs_cleaning
  - input_boolean.cat_cleaning_tool_alert
  - binary_sensor.your_cat_door_sensor
  - binary_sensor.your_cleaning_tool_sensor
```

## Troubleshooting

### Common Issues:
1. **False triggers**: Adjust presence threshold if brief movements trigger counting
2. **Missed usage**: Reduce presence threshold if actual usage isn't being detected
3. **Too many notifications**: Increase warning threshold or adjust notification service
4. **Cleaning not detected**: Check cleaning tool sensor and adjust completion time

### Debug Mode:
Enable Home Assistant automation tracing to see detailed execution logs and timing.

## Migration from ioBroker

If migrating from the original ioBroker script:
1. Note your current counter values
2. Set up the Home Assistant helpers with those initial values
3. Test the sensor mappings match your physical setup
4. Adjust timing parameters based on your previous configuration

## Support

For issues or questions:
1. Check Home Assistant logs for automation errors
2. Verify all helper entities are created correctly
3. Test sensors individually to ensure they trigger properly
4. Review the blueprint configuration for correct entity mappings 