# 🏠 Smart Welcome Greeter Blueprint

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A//raw.githubusercontent.com/n3roGit/HomeAssistant/main/SmartWelcomeGreeter/SmartWelcomeGreeter.yaml)

A comprehensive Home Assistant blueprint that provides intelligent welcome greetings with **fully customizable messages**, multiple greeting types, information notifications, and smart lockout functionality.

## Features

### 🎭 Fully Customizable Greetings
- **4 Greeting Categories**: Normal, funny, movie quotes, and Christmas/December greetings
- **Personal Messages**: Configure all greetings through the UI with multiline text inputs
- **German Defaults**: Pre-filled with authentic German greetings from the original ioBroker script
- **Random Selection**: Smart mixing of greeting types with configurable probabilities

### 📢 Smart Information System
- **Configurable Notifications**: Customize all notification messages
- **Mail Alerts**: Customizable mailbox notifications
- **Waste Collection**: Personalized reminders for yellow and black waste collection
- **Window Warnings**: Open window alerts with room placeholder support (`{rooms}`)

### 🧠 Intelligent Behavior
- **Smart Lockout**: Prevents spam with configurable timeout periods
- **Secondary Motion Detection**: Enhanced logic with hallway/secondary motion sensors
- **Daily Limits**: Configurable maximum daily information announcements
- **Priority System**: Information announcements take priority over random greetings

## Requirements

### Required Helper Entities

Before importing this blueprint, create these helper entities in Home Assistant:

#### Counter (Settings → Devices & Services → Helpers → Counter)
- **Daily Counter** (`counter.smart_greeter_daily_counter`): Tracks daily announcement count

### Required Sensors
- **Main Entrance Motion Sensor**: Binary sensor detecting movement at entrance
- **Notification Service**: TTS service, media player, or notification service for announcements

### Optional Sensors
- **Secondary Motion Sensor**: Additional motion sensor for enhanced detection logic
- **Mailbox Sensor**: Binary sensor indicating mail presence
- **Waste Collection Sensors**: Binary sensors for waste collection days (yellow/black)
- **Window Sensors**: Binary sensors and text sensors for open window monitoring

## Installation

1. **Import Blueprint**: Click the import button above
2. **Create Helper Entity**: Set up the required daily counter (name suggested in blueprint)
3. **Configure Sensors**: Ensure your motion sensors and optional sensors are working
4. **Create Automation**: Use the blueprint to create a new automation
5. **Customize Messages**: Personalize all greeting and notification texts in the configuration

## Configuration

### Basic Settings
- **Greeting Probability**: Chance for random greetings when no secondary motion (default: 50%)
- **Lockout Duration**: Time to prevent repeated greetings (default: 15 minutes)
- **Secondary Sensor Timeout**: Timeout for hallway sensor (default: 2 minutes)
- **Max Daily Information**: Maximum information announcements per day (default: 3)

### Customizable Message Categories

#### 1. **Normal Greetings** (Always Available)
Default German examples:
- "Willkommen zuhause!" (Welcome home!)
- "Hallo!" (Hello!)
- "Schön dich zu sehen!" (Nice to see you!)
- ... and 27 more authentic German greetings

#### 2. **Funny Greetings** (30% chance to include)
Default German examples:
- "Schau mal wer sich hier blicken lässt!" (Look who decided to show up!)
- "Die Legende ist eingetroffen!" (The legend has arrived!)
- "Alarm: VIP hat das Gebäude betreten!" (Alert: VIP has entered the building!)

#### 3. **Movie Quote Greetings** (20% chance to include)
Default German examples:
- "Möge die Macht mit dir sein!" (May the force be with you!)
- "Willkommen in der Matrix!" (Welcome to the Matrix!)
- "Bond. Zuhause Bond." (Bond. Home Bond.)

#### 4. **December/Christmas Greetings** (December evenings only)
Default German examples:
- "Frohe Weihnachten und willkommen zuhause!" (Merry Christmas and welcome home!)
- "Ho ho ho, schau mal wer da ist!" (Ho ho ho, look who's here!)
- "Das schönste Weihnachtsgeschenk - du bist zuhause!" (The best Christmas gift - you're home!)

### Customizable Information Notifications

#### 1. **Mail Notifications**
Default examples:
- "Du hast Post im Briefkasten" (You have mail in the mailbox)
- "Es liegt Post für dich bereit" (There's mail waiting for you)

#### 2. **Yellow Waste Collection Notifications**
Default examples:
- "Vergiss nicht, den gelben Sack und das Altpapier rauszustellen" (Don't forget to put out the yellow bag and paper)
- "Heute kommt die Müllabfuhr für gelben Sack und Altpapier" (Today is collection day for yellow bags and paper)

#### 3. **Black Waste Collection Notifications**
Default examples:
- "Vergiss nicht, die schwarze und braune Tonne rauszustellen" (Don't forget to put out the black and brown bins)
- "Heute kommt die Müllabfuhr für Rest- und Biomüll" (Today is collection day for general and organic waste)

#### 4. **Window Notifications** (with `{rooms}` placeholder)
Default examples:
- "In {rooms} sind noch Fenster offen" (Windows are still open in {rooms})
- "Bitte schließe die Fenster in {rooms}" (Please close the windows in {rooms})

### Example Custom Configuration
```yaml
# Personalized Normal Greetings
normal_greetings: |
  Hey Schatz, willkommen zuhause!
  Hallo mein Liebling!
  Der beste Mensch der Welt ist da!
  Endlich wieder vereint!

# Custom Funny Greetings
funny_greetings: |
  Da ist ja mein Superheld!
  Achtung, hier kommt die Königin!
  Red alert: Amazing person detected!

# Personalized Mail Notifications
mail_notifications: |
  Schatz, du hast Post bekommen!
  Es wartet ein Päckchen auf dich!
  Überraschung im Briefkasten!
```

## How It Works

### Greeting Logic
1. **Motion Detection**: Main entrance motion sensor triggers
2. **Priority Check**: Information notifications (mail, waste, windows) take priority
3. **Greeting Selection**: If no information to announce:
   - Starts with normal greetings
   - 30% chance to add funny greetings to pool
   - 20% chance to add movie quotes to pool
   - December evenings: adds Christmas greetings
4. **Random Selection**: Picks random greeting from combined pool
5. **Lockout**: Prevents repeated announcements for configured duration

### Information Priority
- **Mail alerts** always announced when detected
- **Waste collection** reminders announced on collection days
- **Window warnings** only when secondary motion sensor is active
- **Daily limit** prevents information overload

### Smart Features
- **Secondary Motion Logic**: Uses hallway sensor to determine if someone is actually entering vs. just passing by
- **Seasonal Adaptation**: Christmas greetings automatically activate in December evenings
- **Daily Limits**: Prevents excessive information announcements

## Example Sensor Setup

### Helper Entity
```yaml
# Via UI: Settings → Devices & Services → Helpers → Counter
# Or in configuration.yaml:
counter:
  smart_greeter_daily_counter:
    name: "Smart Greeter Daily Counter"
    initial: 0
    step: 1
```

### Mailbox Sensor
```yaml
binary_sensor:
  - platform: template
    sensors:
      mailbox_has_mail:
        friendly_name: "Mailbox Has Mail"
        value_template: "{{ states('sensor.mailbox_distance') | float < 10 }}"
```

### Waste Collection (Calendar Integration)
```yaml
binary_sensor:
  - platform: template
    sensors:
      waste_yellow_today:
        friendly_name: "Yellow Waste Collection Today"
        value_template: >
          {{ 'Gelber Sack' in states('calendar.waste_collection') and 
             state_attr('calendar.waste_collection', 'start_time')[:10] == now().strftime('%Y-%m-%d') }}
      
      waste_black_today:
        friendly_name: "Black Waste Collection Today"
        value_template: >
          {{ 'Restmüll' in states('calendar.waste_collection') and 
             state_attr('calendar.waste_collection', 'start_time')[:10] == now().strftime('%Y-%m-%d') }}
```

### Open Windows Template
```yaml
sensor:
  - platform: template
    sensors:
      open_windows_rooms:
        friendly_name: "Rooms with Open Windows"
        value_template: >
          {% set rooms = [] %}
          {% if is_state('binary_sensor.bedroom_window', 'on') %}
            {% set rooms = rooms + ['Schlafzimmer'] %}
          {% endif %}
          {% if is_state('binary_sensor.kitchen_window', 'on') %}
            {% set rooms = rooms + ['Küche'] %}
          {% endif %}
          {% if is_state('binary_sensor.living_room_window', 'on') %}
            {% set rooms = rooms + ['Wohnzimmer'] %}
          {% endif %}
          {{ rooms | join(', ') if rooms else 'keine' }}
```

## Troubleshooting

### No Greetings at All
- Check if motion sensor is working and properly configured
- Verify notification service is accessible and working
- Check if lockout period is still active (check automation traces)
- Ensure greeting probability isn't set to 0%

### Too Many Announcements
- Reduce greeting probability percentage
- Increase lockout duration (15-60 minutes)
- Lower max daily information limit (1-3)
- Check if secondary motion sensor is working correctly

### Missing Information Notifications
- Verify optional sensors are properly configured and working
- Check sensor states in Developer Tools → States
- Ensure daily counter entity exists and resets properly
- Verify daily limit hasn't been reached

### Messages Not Customized
- Check if blueprint inputs are properly filled
- Ensure multiline text areas contain one message per line
- Verify no empty lines in message configurations
- Test with simple messages first

## Original Script Migration

This blueprint is converted from the original ioBroker `Begruessung_AI.json` script with significant enhancements:

**✅ Preserved Features:**
- Motion detection with intelligent lockout
- Multiple greeting types with German content
- Information notifications (mail, waste, windows)
- Secondary motion sensor support
- Daily limits and timing controls

**🆕 New Features:**
- **Fully customizable messages** through Home Assistant UI
- **Helper entity name suggestions** for easier setup
- **Improved syntax** - no more blueprint errors
- **Better default values** - works out of the box
- **Enhanced documentation** with examples

**🔄 Technical Improvements:**
- Fixed variable reference syntax
- Corrected optional input handling
- Improved template logic
- Better error handling

## Helper Entity Names

The blueprint suggests this entity name for consistency:
- `counter.smart_greeter_daily_counter` (Daily Counter Helper)

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all required entities are created and configured
3. Review the automation traces in Home Assistant
4. Test your notification service separately
5. Open an issue in this repository with details about your setup

## Contributing

Feel free to suggest improvements or report issues. The blueprint is designed to be easily extendable for additional greeting types or notification sources.

## License

This blueprint is provided as-is for Home Assistant users. Feel free to modify and share. 