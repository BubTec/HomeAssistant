# 🐾 Cat Litter Box Counter and Monitor

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A//raw.githubusercontent.com/christoph-buebeck/HomeAssistant/main/CatShitCounter/CatShitCounter.yaml)

A comprehensive Home Assistant blueprint for monitoring cat litter box usage, providing cleaning reminders, and tracking cleaning activities.

## Features

### 🎯 Core Functionality
- **Motion Detection**: Tracks when your cat enters and exits the litter box
- **Usage Counting**: Automatically counts valid litter box visits
- **Smart Cleaning Detection**: Monitors cleaning tool usage
- **Cleaning Reminders**: Sends notifications when cleaning is needed
- **Tool Monitoring**: Alerts if cleaning tools are left out

### 🔔 Smart Notifications
- **Funny Messages**: Random humorous cleaning reminders
- **Configurable Thresholds**: Set your own warning levels
- **Multiple Services**: Works with any Home Assistant notification service
- **Scheduled Reminders**: Hourly reminders during daytime (9 AM - 10 PM)

### 📊 Advanced Monitoring
- **Inactivity Detection**: Alerts if no activity for 48+ hours
- **Initial State Check**: Restores warnings after Home Assistant restart
- **Parallel Processing**: Handles multiple events simultaneously
- **Total Statistics**: Tracks lifetime usage and cleaning counts

## Requirements

### Required Helper Entities

Before importing this blueprint, create these helper entities in Home Assistant:

#### Counters (Settings → Devices & Services → Helpers → Counter)
- **Usage Counter**: Tracks current usage since last cleaning
- **Total Counter**: Tracks total lifetime usage  
- **Clean Counter**: Tracks number of cleanings performed

#### Input Booleans (Settings → Devices & Services → Helpers → Toggle)
- **Needs Cleaning Helper**: Indicates if cleaning is required
- **Cleaning Tool Alert**: Indicates if cleaning tool is left open
- **Cat Presence Helper**: Tracks if cat is currently present

### Required Sensors
- **Cat Door Sensor**: Binary sensor detecting movement at litter box (e.g., motion sensor)
- **Cleaning Tool Sensor**: Binary sensor detecting when cleaning tool is taken (e.g., door/contact sensor)

## Installation

1. **Import Blueprint**: Click the import button above
2. **Create Helper Entities**: Set up the required counters and input booleans
3. **Configure Sensors**: Ensure your motion and cleaning tool sensors are working
4. **Create Automation**: Use the blueprint to create a new automation
5. **Configure Settings**: Set your preferred thresholds and notification service

## Configuration

### Basic Settings
- **Warning Threshold**: Number of uses before cleaning warning (default: 4)
- **Notification Service**: Your preferred notification method (default: persistent notifications)

### Timing Settings
- **Presence Threshold**: Minimum time cat must be present (default: 30 seconds)
- **Visit Duration**: Wait time after cat leaves before counting (default: 120 seconds)  
- **Cleaning Completion Time**: Time tool must be open to register cleaning (default: 45 seconds)

### Example Configuration
```yaml
warning_threshold: 4
presence_threshold: 30
visit_duration: 120
cleaning_completion_time: 45
notification_service: "notify.mobile_app_your_phone"
```

## How It Works

### Usage Detection
1. Motion sensor detects cat entering litter box
2. System waits for minimum presence time (30s default)
3. When cat leaves, system waits for visit completion time (120s default)
4. If cat hasn't returned, usage is counted

### Cleaning Detection
1. Cleaning tool sensor detects tool being taken
2. System starts cleaning timer (45s default)
3. If tool remains out for full duration, cleaning is registered
4. Counters are reset and cleaning is logged

### Notification Examples
- *"A message from your cat: MEOW! Please clean my litter box. I've used it 4 times already."*
- *"Hey human, 5 times used and no fresh litter? I think I'll smell this tomorrow too!"*
- *"The litter box is crying: Used 6 times and still no fresh litter? Where's the service?"*

## Troubleshooting

### Common Issues

**No usage being counted:**
- Check if motion sensor is working and detecting movement
- Verify presence and visit duration settings aren't too strict
- Ensure cleaning tool sensor is in 'off' state

**False positives:**
- Increase presence threshold if brief movements trigger counts
- Adjust visit duration if cat returns quickly

**Cleaning not detected:**
- Check cleaning tool sensor placement and operation
- Verify cleaning completion time setting
- Ensure tool sensor registers 'on' when tool is taken

### Debug Tips
- Monitor the helper entities to see current states
- Check automation traces in Home Assistant
- Verify all sensors are reporting correct states

## Original Script

This blueprint is converted from the original ioBroker script `KatzenKlo_Counter_V3.json`. The core functionality has been preserved while adapting to Home Assistant's architecture and improving configurability.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all required entities are created and configured
3. Review the automation traces in Home Assistant
4. Open an issue in this repository with details about your setup 