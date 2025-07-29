# Smart Welcome Greeter Blueprint

A comprehensive Home Assistant blueprint that provides intelligent welcome greetings with multiple greeting types, information notifications, and smart lockout functionality.

## Features

- **Multiple Greeting Types**: Normal, funny, movie quotes, and seasonal greetings
- **Information Notifications**: Mail alerts, waste collection reminders, and open window warnings
- **Smart Lockout**: Prevents spam with configurable timeout periods
- **Secondary Motion Detection**: Optional support for hallway/secondary motion sensors
- **Daily Limits**: Configurable maximum daily information announcements
- **Seasonal Adaptation**: Special Christmas greetings in December evenings
- **Random Variations**: Configurable probability for random greetings

## Requirements

### Mandatory
- **Motion Sensor**: Main entrance motion sensor (binary_sensor with motion device class)
- **Notification Service**: TTS service, media player, or notification service for announcements

### Optional
- **Secondary Motion Sensor**: Additional motion sensor for enhanced logic
- **Mailbox Sensor**: Binary sensor indicating mail presence
- **Waste Collection Sensors**: Binary sensors for waste collection days
- **Window Sensors**: Binary sensors and text sensors for open window monitoring
- **Helper Entities**: Counter entity for daily announcement tracking

## Setup Instructions

### 1. Required Helper Entities

Create these helper entities in Home Assistant:

```yaml
# In configuration.yaml or via UI
counter:
  smart_greeter_daily_counter:
    name: "Smart Greeter Daily Counter"
    initial: 0
    step: 1

automation:
  - alias: "Reset Smart Greeter Daily Counter"
    trigger:
      - platform: time
        at: "00:00:00"
      - platform: time
        at: "12:00:00"
    action:
      - service: counter.reset
        target:
          entity_id: counter.smart_greeter_daily_counter
```

### 2. Blueprint Configuration

When setting up the automation from this blueprint:

1. **Motion Sensor**: Select your main entrance motion sensor
2. **Notification Service**: Choose your preferred TTS or notification service
3. **Optional Sensors**: Configure mailbox, waste collection, and window sensors as needed
4. **Timing**: Adjust greeting probability, lockout duration, and daily limits

### 3. Recommended Sensors

For full functionality, consider setting up:

- **Mailbox Sensor**: Contact sensor or smart mailbox indicator
- **Waste Collection**: Calendar integration or manual binary sensors
- **Window Monitoring**: Window sensors combined with a template sensor listing open rooms

## Configuration Options

| Option | Description | Default | Range |
|--------|-------------|---------|-------|
| Greeting Probability | Chance for random greetings | 50% | 0-100% |
| Lockout Duration | Prevention of repeated greetings | 15 min | 1-60 min |
| Secondary Sensor Timeout | Timeout for hallway sensor | 2 min | 1-10 min |
| Max Daily Info | Maximum information announcements | 3 | 1-10 |

## Greeting Types

### Normal Greetings (Always Available)
- "Welcome home!", "Hello!", "Nice to see you!", etc.

### Funny Greetings (30% chance)
- "Look who decided to show up!", "The legend has arrived!", etc.

### Movie Quotes (20% chance)
- "May the force be with you!", "Live long and prosper!", etc.

### Christmas Greetings (December evenings only)
- "Come in and warm up!", "Merry Christmas and welcome home!", etc.

## Information Notifications

The blueprint can announce:

1. **Mail Notifications**: When mailbox sensor indicates mail
2. **Waste Collection**: Reminders for yellow/black bin collection days
3. **Open Windows**: Alerts about open windows (when secondary motion detected)

## Logic Flow

1. **Motion Detection**: Main entrance motion sensor triggers
2. **Information Check**: Prioritizes important notifications (mail, waste, windows)
3. **Random Greeting**: If no information and conditions met, gives random greeting
4. **Lockout**: Prevents repeated announcements for configured duration

## Example Sensor Setup

### Mailbox Sensor
```yaml
# Template sensor example
binary_sensor:
  - platform: template
    sensors:
      mailbox_has_mail:
        friendly_name: "Mailbox Has Mail"
        value_template: "{{ states('sensor.mailbox_distance') | float < 10 }}"
```

### Waste Collection
```yaml
# Using calendar integration
binary_sensor:
  - platform: template
    sensors:
      waste_yellow_today:
        friendly_name: "Yellow Waste Today"
        value_template: >
          {{ 'Yellow Waste' in states('calendar.waste_collection') and 
             state_attr('calendar.waste_collection', 'start_time')[:10] == now().strftime('%Y-%m-%d') }}
```

### Open Windows
```yaml
# Template for room list
sensor:
  - platform: template
    sensors:
      open_windows_rooms:
        friendly_name: "Rooms with Open Windows"
        value_template: >
          {% set rooms = [] %}
          {% if is_state('binary_sensor.bedroom_window', 'on') %}
            {% set rooms = rooms + ['bedroom'] %}
          {% endif %}
          {% if is_state('binary_sensor.kitchen_window', 'on') %}
            {% set rooms = rooms + ['kitchen'] %}
          {% endif %}
          {{ rooms | join(', ') }}
```

## Troubleshooting

### No Greetings
- Check motion sensor is working and properly configured
- Verify notification service is accessible
- Check if lockout period is active

### Too Many Announcements
- Reduce greeting probability
- Increase lockout duration
- Lower max daily information limit

### Missing Information
- Verify optional sensors are properly configured
- Check sensor states in Developer Tools
- Ensure helper counter entity exists

## Migration from ioBroker

This blueprint replaces the ioBroker `Begruessung_AI.json` script with equivalent functionality:

- ✅ Motion detection with lockout
- ✅ Multiple greeting types
- ✅ Information notifications
- ✅ Secondary motion sensor support
- ✅ Daily limits and timing controls

## Contributing

Feel free to suggest improvements or report issues. The blueprint is designed to be easily extendable for additional greeting types or notification sources.

## License

This blueprint is provided as-is for Home Assistant users. Feel free to modify and share. 