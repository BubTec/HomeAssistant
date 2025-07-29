# Smart Alexa Echo Volume Control

This Home Assistant blueprint automatically adjusts volume levels of Alexa Echo devices based on time schedules. Designed specifically for Home Assistant's Alexa Media Player integration with built-in time-based triggers for day and night modes.

## Features

- 🎤 **Alexa Media Player Integration**: Properly filtered device selectors for Alexa devices
- 🕒 **Time-Based Control**: Built-in time triggers for automatic day/night mode switching
- 🔊 **Volume Control**: Uses proper media_player services for Echo devices
- 📅 **Day Selection**: Choose which days the automation should be active
- 🌙 **Night Mode Support**: Automatic quiet hours with customizable times
- 🤖 **Auto-Discovery**: Automatically finds all Alexa Media Player devices
- 🚫 **Ignore Lists**: Pattern matching to exclude specific devices or rooms
- ⭐ **Special Device Handling**: Configure one Echo with different volume levels
- ⏱️ **Smart Delays**: Random delays to prevent command conflicts
- 🇩🇪 **German Support**: Works with German device names

## Supported Echo Devices

- ✅ **Alexa Media Player Entities**: `media_player.*` with `alexa_media` integration
- ✅ **Auto-Detection**: Automatically finds all devices from Alexa Media Player integration
- ✅ **Proper Filtering**: Device selectors show only Alexa devices

## Use Cases

- **Automatic Night Mode**: Lower Echo volumes at bedtime, restore in morning
- **Weekday Quiet Hours**: Reduce volumes during work-from-home hours
- **Weekend Sleep-in**: Different schedule for weekends
- **Baby Sleep**: Ultra-quiet mode during nap times
- **Room-Specific Control**: Different volumes for bedroom vs living room Echos
- **Custom Schedules**: Flexible day selection (weekdays, weekends, custom days)

## Configuration

### Time Schedule

| Input | Description | Default |
|-------|-------------|---------|
| **Night Mode Start Time** | When quiet hours begin | 22:00 |
| **Night Mode End Time** | When quiet hours end | 07:00 |
| **Active Days** | Days when automation runs | Every Day |
| **Custom Days** | Specific days (if Custom selected) | None |

### Echo Device Configuration

| Input | Description | Default |
|-------|-------------|---------|
| **Echo Volume Entities** | Specific Echo entities (empty = auto-discover) | Auto-discover |
| **Ignored Echo Devices** | Echo entities to exclude | None |
| **Ignore Patterns** | Device name patterns to ignore | Empty |

### Volume Configuration

| Input | Description | Default |
|-------|-------------|---------|
| **Night Mode Volume** | Volume during quiet hours (%) | 20 |
| **Day Mode Volume** | Volume during normal hours (%) | 40 |
| **Special Echo Device** | Echo with different volume levels | None |
| **Special Night Volume** | Special Echo night volume (%) | 30 |
| **Special Day Volume** | Special Echo day volume (%) | 80 |

## Setup Examples

### Basic Automatic Night Mode

Blueprint Configuration:
- **Night Mode Start**: 22:00
- **Night Mode End**: 07:00
- **Active Days**: Every Day
- **Echo Volume Entities**: (leave empty for auto-discovery)
- **Night Mode Volume**: 15
- **Day Mode Volume**: 50

This will automatically:
- At 22:00: Set all Echos to 15% volume
- At 07:00: Set all Echos to 50% volume
- Runs every day

### Weekdays Only Configuration

Blueprint Configuration:
- **Night Mode Start**: 23:00
- **Night Mode End**: 06:30
- **Active Days**: Weekdays Only
- **Night Mode Volume**: 10
- **Day Mode Volume**: 60

Perfect for work schedules - quiet at night on weekdays only.

### Advanced Configuration with Special Device

```yaml
# Blueprint Configuration
Night Mode Start: 22:30
Night Mode End: 07:30
Active Days: Custom
Custom Days: Monday, Tuesday, Wednesday, Thursday, Friday, Sunday
Ignore Patterns:
  basement
  garage
  outdoor
Special Echo Device: media_player.schlafzimmer_echo
Special Night Volume: 5    # Very quiet in bedroom
Special Day Volume: 30     # Still quieter than others during day
```

### Weekend Sleep-in Mode

Blueprint Configuration:
- **Night Mode Start**: 23:30
- **Night Mode End**: 09:00  
- **Active Days**: Weekends Only
- **Night Mode Volume**: 10
- **Day Mode Volume**: 45

Later quiet hours and sleep-in time for weekends.

## How It Works

1. **Time Triggers**: 
   - At night mode start time → Sets all Echos to night volume
   - At night mode end time → Sets all Echos to day volume
2. **Day Filter**: Only runs on selected days (weekdays, weekends, or custom selection)
3. **Echo Discovery**: 
   - Uses manual selection if provided
   - Auto-discovers all Alexa Media Player integration devices
4. **Ignore Processing**: 
   - Removes entities from ignore list
   - Applies pattern-based filtering (room names, device names)
5. **Volume Control**: 
   - Normal Echos get night/day volume based on time
   - Special Echo gets custom volume levels
   - Uses `media_player.volume_set` service with proper 0.0-1.0 scaling

## Auto-Discovery Details

The blueprint automatically finds Echo entities from Alexa Media Player integration:
```jinja2
# Examples of entities that will be found:
media_player.badezimmer_echo
media_player.echo_kitchen
media_player.alexa_bedroom
media_player.buero_echo_dot
```

Search criteria:
- Domain is **media_player**
- Integration is **alexa_media**
- Automatically filtered in device selector

## Volume Control Service

### Alexa Media Player Devices
```yaml
service: media_player.volume_set
target:
  entity_id: media_player.badezimmer_echo
data:
  volume_level: 0.25  # 0.0-1.0 scale (25%)
```

The blueprint automatically converts percentage (0-100) to the required 0.0-1.0 scale.

## Advanced Features

### Ignore Patterns

Ignore specific rooms or device types:
```
basement      # Ignores: *basement*
outdoor       # Ignores: *outdoor*
garage        # Ignores: *garage*
büro          # Ignores: *büro*
```

### Random Delays

Prevents command conflicts:
- Configurable 1-30 second maximum delay
- Each Echo gets a random delay between 0-max seconds
- Special Echo gets fixed delay (default 15 seconds)

### Special Device Handling

Perfect for main/master Echos that need different behavior:
- Bedroom Echo stays quieter even in "day" mode
- Kitchen Echo gets louder for cooking timers
- Study Echo for work calls needs different levels

## Day Selection Options

### Predefined Options
- **Every Day**: 7 days a week
- **Weekdays Only**: Monday-Friday
- **Weekends Only**: Saturday-Sunday

### Custom Selection
Choose any combination of days:
- Monday, Wednesday, Friday only
- Tuesday, Thursday, Saturday
- Any custom pattern you need

## Alexa Media Player Integration

### Installation

Install via HACS:
```
1. Go to HACS → Integrations
2. Search for "Alexa Media Player"
3. Install and restart Home Assistant
4. Configure with your Amazon account
```

### Expected Entities

Your Echo devices will create entities like:
```
media_player.badezimmer_echo
media_player.buero_echo_dot
media_player.eingang_echo
media_player.kinderzimmer_echo_show
media_player.schlafzimmer_echo_dot
```

## Troubleshooting

### Common Issues

**No Echo devices found:**
- Check if Alexa Media Player integration is working
- Verify devices appear as media_player entities
- Check Developer Tools → States for available entities
- Try manual entity selection instead of auto-discovery

**Some Echos don't respond:**
- Check device names in ignore patterns
- Verify entities exist and are available in Developer Tools
- Ensure Echo devices are online in Alexa app
- Check if devices support volume control

**Wrong timing:**
- Verify time zone settings in Home Assistant
- Check that Active Days selection matches your needs
- Use Developer Tools → Events to monitor automation triggers

### Debugging

Enable debug logging:
```yaml
logger:
  logs:
    homeassistant.components.automation: debug
    custom_components.alexa_media: debug
```

Check discovered Echo entities in Developer Tools → Template:
```jinja2
{% set found_echos = [] %}
{% for entity in states.media_player %}
  {% if state_attr(entity.entity_id, 'integration') == 'alexa_media' %}
    {% set found_echos = found_echos + [entity.entity_id] %}
  {% endif %}
{% endfor %}
{{ found_echos }}
```

## Migration from Entity-Based Triggers

If you previously used entity-based triggers (like input_boolean helpers), this blueprint now has built-in time triggers. Benefits:

| Old Method | New Method | Benefit |
|------------|------------|---------|
| input_boolean.night_mode | Built-in time triggers | No extra helpers needed |
| Separate time automations | Integrated time schedule | Simpler setup |
| Manual entity selection | Alexa integration filter | Better device discovery |
| number/input_number entities | media_player entities | Proper Alexa control |

## Example Schedules

### Standard Work Schedule
- **Night**: 22:00 - 07:00
- **Days**: Weekdays Only
- **Night Volume**: 15%
- **Day Volume**: 50%

### Family with Kids
- **Night**: 20:30 - 07:30
- **Days**: Every Day
- **Night Volume**: 10%
- **Day Volume**: 40%
- **Special Device**: Bedroom Echo at 5% night / 25% day

### Shift Worker
- **Night**: 06:00 - 14:00 (day sleep)
- **Days**: Custom (work days)
- **Night Volume**: 5%
- **Day Volume**: 60%

## Related Blueprints

This blueprint pairs well with:
- Motion-activated lighting with time conditions
- Smart doorbell with quiet hours
- Baby sleep monitoring automations
- Work-from-home mode controllers
- Other time-based home automation blueprints 