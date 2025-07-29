# Smart Volume Control for Smart Assistants

This Home Assistant blueprint automatically adjusts volume levels of smart assistants (Echo, Google Home, etc.) based on mode changes such as night mode, presence detection, or any other state change. Specifically designed for smart assistant volume entities rather than general media players.

## Features

- 🎤 **Smart Assistant Focus**: Specifically targets Echo, Google Home, and other smart assistant volume entities
- 🔊 **Dual Volume Control**: Supports both player volume and speak volume (like original ioBroker script)
- 🌙 **Night Mode Support**: Perfect for lowering volumes during night hours
- 🤖 **Auto-Discovery**: Automatically finds Alexa and other smart assistant volume entities
- 🚫 **Advanced Filtering**: Ignore lists with pattern matching (device IDs, serial numbers)
- ⭐ **Special Device Handling**: Configure one device with different volume levels
- ⏱️ **Smart Delays**: Random delays to prevent command conflicts (like original script)
- 🎯 **Flexible Entity Types**: Works with number, input_number, and media_player entities

## Entity Types Supported

- ✅ **Alexa Echo Devices**: `number.alexa2_*_echo_*_player_volume`
- ✅ **Alexa Speak Volume**: `number.alexa2_*_echo_*_commands_speak_volume`
- ✅ **Google Home**: `number.*_volume` entities
- ✅ **Input Numbers**: `input_number.*_volume` helpers
- ✅ **Media Players**: Fallback support for `media_player.*` entities

## Use Cases

- **Night Mode**: Lower Echo volumes when everyone goes to sleep
- **Presence Detection**: Mute assistants when leaving/arriving home  
- **Work Hours**: Reduce volumes during work-from-home hours
- **Baby Sleep**: Ultra-quiet mode when baby is sleeping
- **Party Mode**: Increase volumes for entertainment
- **Device-Specific Control**: Different volumes for bedroom vs living room Echos

## Configuration

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Mode Control Entity** | Entity that triggers volume changes | `input_boolean.night_mode` |

### Smart Assistant Specific Inputs

| Input | Description | Default |
|-------|-------------|---------|
| **Volume Control Type** | Player, Speak, or Both volumes | Both |
| **Smart Assistant Volume Entities** | Specific entities (empty = auto-discover) | Auto-discover |
| **Entity Pattern Filters** | Patterns to find volume entities | Alexa, Google patterns |
| **Ignore Patterns** | Device ID patterns to ignore | Empty |

### Volume Configuration

| Input | Description | Default |
|-------|-------------|---------|
| **Low Volume Level** | Volume when mode is active (%) | 20 |
| **High Volume Level** | Volume when mode is inactive (%) | 40 |
| **Special Device** | Device with different volume levels | None |
| **Special Low Volume** | Special device low volume (%) | 30 |
| **Special High Volume** | Special device high volume (%) | 80 |

## Setup Examples

### Basic Alexa Night Mode

```yaml
# Create input_boolean helper
input_boolean:
  night_mode:
    name: Night Mode
    initial: false
```

Blueprint Configuration:
- **Mode Control Entity**: `input_boolean.night_mode`
- **Volume Control Type**: "Both Player and Speak Volume"
- **Low Volume**: 15 (night volume)
- **High Volume**: 50 (day volume)

### Advanced Configuration with Ignored Devices

```yaml
# Blueprint Configuration
Mode Control Entity: input_boolean.quiet_hours
Volume Control Type: "Both Player and Speak Volume"
Smart Assistant Volume Entities: (leave empty for auto-discovery)
Ignore Patterns:
  G090XG0894542523
  G0922H0843620RFD
Special Device: number.alexa2_0_echo_devices_main_echo_player_volume
Special Low Volume: 25
Special High Volume: 75
```

### Pattern-Based Auto-Discovery

The blueprint automatically finds these entity patterns:
```
alexa2.*.Echo-Devices.*.Player.volume
alexa2.*.Echo-Devices.*.Commands.speak-volume
number.*_volume
input_number.*_volume
```

## How It Works

1. **Trigger**: Activates when the mode control entity changes state
2. **Entity Discovery**: 
   - Uses manual selection if provided
   - Auto-discovers smart assistant volume entities
   - Filters by volume type (player/speak/both)
3. **Ignore Processing**: 
   - Removes entities from ignore list
   - Applies pattern-based filtering (device IDs)
4. **Volume Control**: 
   - Normal devices get low/high volume based on mode
   - Special device gets custom volume levels
   - Uses appropriate service based on entity type

## Entity Services Used

### Number Entities (Most Alexa volumes)
```yaml
service: number.set_value
data:
  value: 25  # 0-100 percentage
```

### Input Number Entities
```yaml
service: input_number.set_value
data:
  value: 25  # 0-100 percentage
```

### Media Player Entities (Fallback)
```yaml
service: media_player.volume_set
data:
  volume_level: 0.25  # 0.0-1.0 scale
```

## Advanced Features

### Ignore Patterns

Ignore specific Echo devices by serial number:
```
G090XG0894542523
G0922H0843620RFD
basement_echo
```

### Volume Type Control

- **Player Volume Only**: Controls music/media playback volume
- **Speak Volume Only**: Controls TTS/announcement volume  
- **Both**: Controls both types (recommended)

### Random Delays

Prevents command conflicts when controlling multiple devices:
- Configurable 1-30 second maximum delay
- Each device gets a random delay
- Special device gets fixed delay

## Troubleshooting

### Common Issues

**No entities found:**
- Check if Alexa integration is working
- Verify entity names match expected patterns
- Try manual entity selection

**Some Echos don't respond:**
- Check device IDs in ignore patterns
- Verify entities exist and are available
- Some devices may need brief delays

**Wrong volume levels:**
- Number entities use 0-100 scale
- Media players use 0.0-1.0 scale (auto-converted)
- Check entity state in Developer Tools

### Debugging

Enable debug logging:
```yaml
logger:
  logs:
    homeassistant.components.automation: debug
    homeassistant.components.alexa2: debug
```

Check discovered entities in template editor:
```jinja2
{% set all_entities = [] %}
{% for entity in states.number %}
  {% if 'alexa2' in entity.entity_id and 'volume' in entity.entity_id %}
    {% set all_entities = all_entities + [entity.entity_id] %}
  {% endif %}
{% endfor %}
{{ all_entities }}
```

## Migration from ioBroker

This blueprint replicates the original ioBroker Echo volume script:

| ioBroker Feature | Home Assistant Equivalent |
|------------------|----------------------------|
| `IgnoreList` array | Ignore Patterns input |
| Player volume control | Number entity volume control |
| Speak volume control | Number entity speak-volume control |
| Random delays | Random delay feature |
| Special device handling | Special Device configuration |
| NightLightMode trigger | Mode Control Entity |

## Related Blueprints

This blueprint pairs well with:
- Motion-activated lighting
- Presence detection automations  
- Time-based scene controllers
- Smart doorbell integrations 