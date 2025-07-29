# Alexa Echo Volume Control

This Home Assistant blueprint automatically adjusts volume levels of Alexa Echo devices based on mode changes such as night mode, presence detection, or any other state change. Designed specifically for Home Assistant's Alexa Media Player integration and replicates the functionality of the original ioBroker Echo volume script.

## Features

- 🎤 **Alexa Echo Focus**: Specifically designed for Amazon Echo devices
- 🔊 **Volume Control**: Uses appropriate services for Echo volume entities
- 🌙 **Night Mode Support**: Perfect for lowering volumes during night hours
- 🤖 **Auto-Discovery**: Automatically finds Echo volume entities
- 🚫 **Ignore Lists**: Pattern matching to exclude specific devices or rooms
- ⭐ **Special Device Handling**: Configure one Echo with different volume levels
- ⏱️ **Smart Delays**: Random delays to prevent command conflicts (like original ioBroker script)
- 🇩🇪 **German Support**: Works with German device names like "Lautsprecher"

## Supported Echo Entities

- ✅ **Number Entities**: `number.*_volume` (most common with Alexa Media Player)
- ✅ **Input Number Entities**: `input_number.*_volume` (custom helpers)
- ✅ **Auto-Detection**: Finds entities containing "alexa", "echo", or "lautsprecher" with "volume"

## Use Cases

- **Night Mode**: Lower Echo volumes when everyone goes to sleep
- **Presence Detection**: Mute Echos when leaving/arriving home  
- **Work Hours**: Reduce volumes during work-from-home hours
- **Baby Sleep**: Ultra-quiet mode when baby is sleeping
- **Party Mode**: Increase volumes for entertainment
- **Room-Specific Control**: Different volumes for bedroom vs living room Echos

## Configuration

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Mode Control Entity** | Entity that triggers volume changes | `input_boolean.night_mode` |

### Echo Device Configuration

| Input | Description | Default |
|-------|-------------|---------|
| **Echo Volume Entities** | Specific Echo entities (empty = auto-discover) | Auto-discover |
| **Ignored Echo Devices** | Echo entities to exclude | None |
| **Ignore Patterns** | Device name patterns to ignore | Empty |

### Volume Configuration

| Input | Description | Default |
|-------|-------------|---------|
| **Low Volume Level** | Volume when mode is active (%) | 20 |
| **High Volume Level** | Volume when mode is inactive (%) | 40 |
| **Special Echo Device** | Echo with different volume levels | None |
| **Special Low Volume** | Special Echo low volume (%) | 30 |
| **Special High Volume** | Special Echo high volume (%) | 80 |

## Setup Examples

### Basic Echo Night Mode

```yaml
# Create input_boolean helper
input_boolean:
  night_mode:
    name: Night Mode
    initial: false
```

Blueprint Configuration:
- **Mode Control Entity**: `input_boolean.night_mode`
- **Echo Volume Entities**: (leave empty for auto-discovery)
- **Low Volume**: 15 (night volume)
- **High Volume**: 50 (day volume)

### Advanced Configuration with Ignored Devices

```yaml
# Blueprint Configuration
Mode Control Entity: input_boolean.quiet_hours
Echo Volume Entities: (leave empty for auto-discovery)
Ignore Patterns:
  basement
  garage
  outdoor
Special Echo Device: number.schlafzimmer_lautsprecher_volume
Special Low Volume: 10
Special High Volume: 60
```

### Manual Echo Selection

```yaml
# Blueprint Configuration
Mode Control Entity: binary_sensor.everyone_away
Echo Volume Entities:
  - number.badezimmer_lautsprecher_volume
  - number.buro_lautsprecher_volume
  - number.kinderzimmer_lautsprecher_volume
Low Volume: 0   # Mute when away
High Volume: 40 # Normal when home
```

## How It Works

1. **Trigger**: Activates when the mode control entity changes state
2. **Echo Discovery**: 
   - Uses manual selection if provided
   - Auto-discovers entities containing "alexa", "echo", or "lautsprecher" with "volume"
   - Searches both `number` and `input_number` domains
3. **Ignore Processing**: 
   - Removes entities from ignore list
   - Applies pattern-based filtering (room names, device names)
4. **Volume Control**: 
   - Normal Echos get low/high volume based on mode
   - Special Echo gets custom volume levels
   - Uses appropriate service (`number.set_value` or `input_number.set_value`)

## Auto-Discovery Details

The blueprint automatically finds Echo entities matching these patterns:
```jinja2
# Examples of entities that will be found:
number.badezimmer_lautsprecher_volume
number.echo_kitchen_volume
number.alexa_bedroom_volume
input_number.echo_office_volume
```

Search criteria:
- Entity contains **"alexa"** OR **"echo"** OR **"lautsprecher"**
- AND entity contains **"volume"**
- Domain is **number** or **input_number**

## Volume Control Services

### Number Entities (Most Common)
```yaml
service: number.set_value
target:
  entity_id: number.badezimmer_lautsprecher_volume
data:
  value: 25  # 0-100 percentage
```

### Input Number Entities
```yaml
service: input_number.set_value
target:
  entity_id: input_number.echo_kitchen_volume
data:
  value: 25  # 0-100 percentage
```

## Advanced Features

### Ignore Patterns

Ignore specific rooms or device types:
```
basement      # Ignores: *basement*
outdoor       # Ignores: *outdoor*
workshop      # Ignores: *workshop*
```

### Random Delays

Prevents command conflicts (like original ioBroker script):
- Configurable 1-30 second maximum delay
- Each Echo gets a random delay between 0-max seconds
- Special Echo gets fixed delay (default 15 seconds)

### Special Device Handling

Perfect for main/master Echos that need different behavior:
- Bedroom Echo stays quieter even in "normal" mode
- Kitchen Echo gets louder for cooking timers
- Main Echo for announcements and important notifications

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
number.badezimmer_lautsprecher_volume
number.buro_lautsprecher_volume
number.eingang_lautsprecher_volume
number.kinderzimmer_lautsprecher_volume
number.schlafzimmer_lautsprecher_volume
```

## Troubleshooting

### Common Issues

**No Echo devices found:**
- Check if Alexa Media Player integration is working
- Verify entity names contain "alexa", "echo", or "lautsprecher"
- Check Developer Tools → States for available entities
- Try manual entity selection instead of auto-discovery

**Some Echos don't respond:**
- Check device names in ignore patterns
- Verify entities exist and are available in Developer Tools
- Ensure Echo devices are online in Alexa app

**Wrong volume levels:**
- All volumes use 0-100 percentage scale
- Check current value in Developer Tools → States
- Some Echos may have minimum/maximum volume limits

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
{% for entity in states.number %}
  {% set entity_name = entity.entity_id.lower() %}
  {% if ('alexa' in entity_name or 'echo' in entity_name or 'lautsprecher' in entity_name) and 'volume' in entity_name %}
    {% set found_echos = found_echos + [entity.entity_id] %}
  {% endif %}
{% endfor %}
{{ found_echos }}
```

## Migration from ioBroker

This blueprint replicates the original ioBroker Echo volume script:

| ioBroker Feature | Home Assistant Equivalent |
|------------------|----------------------------|
| `IgnoreList` array | Ignore Patterns input |
| Echo device selection | Auto-discovery with alexa/echo/lautsprecher |
| Volume control | number.set_value service |
| Random delays (1-10000ms) | Random delay feature (1-30s) |
| Special device handling | Special Echo Device configuration |
| NightLightMode trigger | Mode Control Entity |
| `mathRandomInt()` function | Built-in random range function |

## Example Automations

### Time-Based Night Mode

```yaml
automation:
  - alias: "Auto Night Mode"
    trigger:
      - platform: time
        at: "22:00:00"
        id: "night_start"
      - platform: time  
        at: "07:00:00"
        id: "night_end"
    action:
      - service: input_boolean.turn_{{ 'on' if trigger.id == 'night_start' else 'off' }}
        target:
          entity_id: input_boolean.night_mode
```

### Presence-Based Control

```yaml
automation:
  - alias: "Away Mode Echo Volume"
    trigger:
      - platform: state
        entity_id: binary_sensor.everyone_away
    action:
      - service: input_boolean.turn_{{ 'on' if trigger.to_state.state == 'on' else 'off' }}
        target:
          entity_id: input_boolean.away_mode
```

## Related Blueprints

This blueprint pairs well with:
- Motion-activated lighting
- Presence detection automations  
- Time-based scene controllers
- Smart doorbell integrations
- Other Alexa automation blueprints 