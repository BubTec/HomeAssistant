# 🐾 Cat Litter Box Counter and Monitor

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A//raw.githubusercontent.com/n3roGit/HomeAssistant/main/CatShitCounter/CatShitCounter.yaml)

A comprehensive Home Assistant blueprint for monitoring cat litter box usage, providing intelligent cleaning reminders, and tracking cleaning activities with full customization.

## Features

### 🎯 Core Functionality
- **Motion Detection**: Tracks when your cat enters and exits the litter box
- **Usage Counting**: Automatically counts valid litter box visits
- **Smart Cleaning Detection**: Monitors cleaning tool usage
- **Intelligent Reminders**: Configurable time windows and intervals
- **Tool Monitoring**: Alerts if cleaning tools are left out

### 🔔 Smart Notification System
- **Time Window Control**: Set daily notification hours (e.g., 8 AM - 10 PM)
- **Configurable Intervals**: Choose reminder frequency (1-12 hours)
- **Custom Messages**: Personalize all 6 notification types
- **Multiple Services**: Works with any Home Assistant notification service
- **Placeholder Support**: Use `{count}` in cleaning reminders

### 📊 Advanced Monitoring
- **Inactivity Detection**: Alerts if no activity for 48+ hours
- **Initial State Check**: Restores warnings after Home Assistant restart
- **Parallel Processing**: Handles multiple events simultaneously
- **Total Statistics**: Tracks lifetime usage and cleaning counts

## Requirements

### Required Helper Entities

Before importing this blueprint, create these helper entities in Home Assistant:

#### Counters (Settings → Devices & Services → Helpers → Counter)
- **Usage Counter** (`counter.catshit_lastseen`): Tracks current usage since last cleaning
- **Total Counter** (`counter.catshit_totalcounter`): Tracks total lifetime usage  
- **Clean Counter** (`counter.catshit_counter`): Tracks number of cleanings performed

#### Input Booleans (Settings → Devices & Services → Helpers → Toggle)
- **Needs Cleaning Helper** (`input_boolean.catshit_cleaning`): Indicates if cleaning is required
- **Cleaning Tool Alert** (`input_boolean.catshit_toolcheck`): Indicates if cleaning tool is left open
- **Cat Presence Helper** (`input_boolean.catshit_tracker`): Tracks if cat is currently present

### Required Sensors
- **Cat Door Sensor**: Binary sensor detecting movement at litter box (e.g., motion sensor)
- **Cleaning Tool Sensor**: Binary sensor detecting when cleaning tool is taken (e.g., door/contact sensor)

## Installation

1. **Import Blueprint**: Click the import button above
2. **Create Helper Entities**: Set up the required counters and input booleans (names suggested in blueprint)
3. **Configure Sensors**: Ensure your motion and cleaning tool sensors are working
4. **Create Automation**: Use the blueprint to create a new automation
5. **Configure Settings**: Set your preferred thresholds, time windows, and messages

## Configuration

### Basic Settings
- **Warning Threshold**: Number of uses before cleaning warning (default: 4)
- **Notification Service**: Your preferred notification method (default: `notify.all_mobile`)

### Timing Settings
- **Presence Threshold**: Minimum time cat must be present (default: 30 seconds)
- **Visit Duration**: Wait time after cat leaves before counting (default: 120 seconds)  
- **Cleaning Completion Time**: Time tool must be open to register cleaning (default: 45 seconds)

### Notification Control (NEW!)
- **Notification Start Time**: Begin daily notification window (default: 08:00)
- **Notification End Time**: End daily notification window (default: 22:00)
- **Reminder Interval**: Hours between reminders within window (default: 4 hours)

### Custom Messages (NEW!)
Personalize all 6 notification types:

1. **Cleaning Reminder**: Use `{count}` for usage count
   - Default: *"The litter box needs cleaning! Used {count} times since last cleaning."*

2. **Tool Alert**: When cleaning tool is left open
   - Default: *"Warning: The litter box cleaning tool is not properly stored."*

3. **Inactivity Warning**: No activity for 48+ hours
   - Default: *"Warning: No activity at the litter box for more than 48 hours. Please check on your cat!"*

4. **Cleaning Started**: When cleaning begins
   - Default: *"Cat litter cleaning started. Don't forget to put the tool back!"*

5. **Cleaning Completed**: When cleaning finishes
   - Default: *"Cat litter cleaning completed and counters reset."*

6. **Tool Stored**: When cleaning tool is put away
   - Default: *"Cleaning tool properly stored."*

### Example Configuration
```yaml
# Basic Settings
warning_threshold: 4
notification_service: "notify.all_mobile"

# Timing
presence_threshold: 30
visit_duration: 120
cleaning_completion_time: 45

# Notification Window
notification_start_time: "08:00:00"
notification_end_time: "22:00:00"
reminder_interval_hours: 4

# Custom Messages
cleaning_reminder_message: "Hey! 🐱 The litter box needs attention - used {count} times!"
tool_alert_message: "⚠️ Don't forget to put the cleaning tool away!"
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

### Smart Reminder System (NEW!)
- System checks every 2 hours for notifications
- Sends reminders only during your specified time window
- Respects your chosen interval (e.g., every 4 hours = 8:00, 12:00, 16:00, 20:00)
- Uses your custom messages with dynamic content

### Example Notification Schedule
**Settings**: Window 08:00-22:00, Interval 4 hours
**Result**: Reminders at 08:00, 12:00, 16:00, 20:00 (only if needed)

## Troubleshooting

### Common Issues

**No usage being counted:**
- Check if motion sensor is working and detecting movement
- Verify presence and visit duration settings aren't too strict
- Ensure cleaning tool sensor is in 'off' state

**No reminders received:**
- Check if current time is within notification window
- Verify reminder interval settings
- Ensure notification service is working

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
- Test notification service manually

## Helper Entity Names

The blueprint suggests these entity names for consistency:
- `counter.catshit_lastseen` (Usage Counter)
- `counter.catshit_totalcounter` (Total Counter)
- `counter.catshit_counter` (Cleaning Counter)
- `input_boolean.catshit_cleaning` (Needs Cleaning)
- `input_boolean.catshit_toolcheck` (Tool Alert)
- `input_boolean.catshit_tracker` (Cat Presence)

## Original Script

This blueprint is converted from the original ioBroker script `KatzenKlo_Counter_V3.json`. The functionality has been significantly enhanced with Home Assistant's capabilities, adding time window control, custom messages, and improved configurability.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all required entities are created and configured
3. Review the automation traces in Home Assistant
4. Test your notification service separately
5. Open an issue in this repository with details about your setup 