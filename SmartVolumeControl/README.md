# Smart Volume Control for Smart Assistants

This Home Assistant blueprint automatically adjusts volume levels of smart assistants (Echo, Google Home, etc.) based on mode changes such as night mode, presence detection, or any other state change. Works with Home Assistant's Alexa Media Player integration and other smart assistant integrations.

## Features

- 🎤 **Smart Assistant Focus**: Specifically targets Echo, Google Home, and other smart assistant media players
- 🔊 **Standard Volume Control**: Uses Home Assistant's `media_player.volume_set` service
- 🌙 **Night Mode Support**: Perfect for lowering volumes during night hours
- 🤖 **Auto-Discovery**: Automatically finds smart assistant media players by name patterns
- 🚫 **Advanced Filtering**: Ignore lists with pattern matching (device names, rooms)
- ⭐ **Special Device Handling**: Configure one device with different volume levels
- ⏱️ **Smart Delays**: Random delays to prevent command conflicts (like original ioBroker script)
- 🎯 **Flexible Pattern Matching**: Works with any media_player entities matching smart assistant patterns

## Entity Types Supported

- ✅ **Alexa Echo Devices**: `media_player.echo_*`, `media_player.*_echo_*`, `media_player.*_alexa_*`
- ✅ **Google Home/Nest**: `media_player.google_*`, `media_player.*_nest_*`, `media_player.*_assistant_*`
- ✅ **Custom Smart Assistants**: Any media_player with configurable name patterns
- ✅ **Manual Selection**: Specific media_player entities of your choice

## Use Cases

- **Night Mode**: Lower Echo volumes when everyone goes to sleep
- **Presence Detection**: Mute assistants when leaving/arriving home  
- **Work Hours**: Reduce volumes during work-from-home hours
- **Baby Sleep**: Ultra-quiet mode when baby is sleeping
- **Party Mode**: Increase volumes for entertainment
- **Device-Specific Control**: Different volumes for bedroom vs living room assistants

## Configuration

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Mode Control Entity** | Entity that triggers volume changes | `input_boolean.night_mode` |

### Smart Assistant Specific Inputs

| Input | Description | Default |
|-------|-------------|---------|
| **Smart Assistant Media Players** | Specific media players (empty = auto-discover) | Auto-discover |
| **Device Name Patterns** | Patterns to find smart assistants | echo, alexa, google, nest, assistant |
| **Ignore Patterns** | Device name patterns to ignore | Empty |

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
- **Smart Assistant Media Players**: (leave empty for auto-discovery)
- **Low Volume**: 15 (night volume)
- **High Volume**: 50 (day volume)

### Advanced Configuration with Ignored Devices

```yaml
# Blueprint Configuration
Mode Control Entity: input_boolean.quiet_hours
Smart Assistant Media Players: (leave empty for auto-discovery)
Device Name Patterns:
  echo
  alexa
  google_home
Ignore Patterns:
  basement
  garage
  outdoor
Special Device: media_player.echo_bedroom
Special Low Volume: 10
Special High Volume: 60
```

### Manual Device Selection

```yaml
# Blueprint Configuration
Mode Control Entity: binary_sensor.everyone_away
Smart Assistant Media Players:
  - media_player.echo_kitchen
  - media_player.echo_living_room
  - media_player.google_home_bedroom
Low Volume: 0   # Mute when away
High Volume: 40 # Normal when home
```

## How It Works

1. **Trigger**: Activates when the mode control entity changes state
2. **Device Discovery**: 
   - Uses manual selection if provided
   - Auto-discovers media_player entities matching name patterns
   - Filters by device name patterns (echo, alexa, google, etc.)
3. **Ignore Processing**: 
   - Removes entities from ignore list
   - Applies pattern-based filtering (room names, device names)
4. **Volume Control**: 
   - Normal devices get low/high volume based on mode
   - Special device gets custom volume levels
   - Uses `media_player.volume_set` service with proper 0.0-1.0 scale

## Volume Control Details

### Home Assistant Media Player Service

```yaml
service: media_player.volume_set
target:
  entity_id: media_player.echo_kitchen
data:
  volume_level: 0.25  # 25% volume (0.0-1.0 scale)
```

### Automatic Conversion

The blueprint automatically converts percentage inputs (0-100) to Home Assistant's volume scale (0.0-1.0):
- Input: 25% → volume_level: 0.25
- Input: 50% → volume_level: 0.50
- Input: 100% → volume_level: 1.00

## Pattern Matching Examples

### Default Auto-Discovery Patterns
```
echo          # Matches: media_player.echo_kitchen, media_player.bedroom_echo
alexa         # Matches: media_player.alexa_bedroom, media_player.living_alexa
google        # Matches: media_player.google_home, media_player.google_nest
nest          # Matches: media_player.nest_mini, media_player.kitchen_nest
assistant     # Matches: media_player.assistant_*, media_player.*_assistant
```

### Custom Patterns
Add your own patterns for other devices:
```
sonos_one     # If you have Sonos One with voice assistant
bose_home     # Bose smart speakers
```

## Advanced Features

### Ignore Patterns

Ignore specific devices or rooms:
```
basement      # Ignores: media_player.echo_basement
outdoor       # Ignores: media_player.outdoor_speaker
workshop      # Ignores: media_player.workshop_echo
```

### Random Delays

Prevents command conflicts when controlling multiple devices:
- Configurable 1-30 second maximum delay
- Each device gets a random delay between 0-max seconds
- Special device gets fixed delay (default 15 seconds)

### Special Device Handling

Perfect for main/master devices that need different volume levels:
- Bedroom Echo stays quieter even in "normal" mode
- Living room speaker gets louder for announcements
- Kitchen device for cooking timers and recipes

## Integration Requirements

### Alexa Media Player Integration

Install the custom Alexa Media Player integration:
```yaml
# In HACS → Integrations
# Search for "Alexa Media Player"
# Follow setup instructions for your Amazon account
```

Your Echo devices will appear as:
```
media_player.echo_dot_kitchen
media_player.echo_show_bedroom  
media_player.echo_plus_living_room
```

### Google Assistant Integration

For Google/Nest devices, use the Google Cast integration (built-in):
```
media_player.google_home_mini
media_player.nest_hub_kitchen
media_player.nest_audio_bedroom
```

## Troubleshooting

### Common Issues

**No devices found:**
- Check if Alexa Media Player or Google Cast integration is working
- Verify device names contain expected patterns (echo, alexa, google)
- Try manual device selection instead of auto-discovery

**Some devices don't respond:**
- Check device names in ignore patterns
- Verify entities exist in Developer Tools → States
- Ensure devices are online and available

**Wrong volume levels:**
- All volumes use 0-100 percentage scale
- Blueprint automatically converts to Home Assistant's 0.0-1.0 scale
- Check current volume_level attribute in Developer Tools

### Debugging

Enable debug logging:
```yaml
logger:
  logs:
    homeassistant.components.automation: debug
    homeassistant.components.media_player: debug
```

Check discovered devices in Developer Tools → Template:
```jinja2
{% set patterns = ['echo', 'alexa', 'google', 'nest'] %}
{% set found_players = [] %}
{% for entity in states.media_player %}
  {% for pattern in patterns %}
    {% if pattern in entity.entity_id.lower() %}
      {% set found_players = found_players + [entity.entity_id] %}
      {% break %}
    {% endif %}
  {% endfor %}
{% endfor %}
{{ found_players }}
```

## Migration from ioBroker

This blueprint replicates the original ioBroker Echo volume script:

| ioBroker Feature | Home Assistant Equivalent |
|------------------|----------------------------|
| `IgnoreList` array | Ignore Patterns input |
| Alexa device selection | Auto-discovery by name patterns |
| Volume control | media_player.volume_set service |
| Random delays | Random delay feature |
| Special device handling | Special Device configuration |
| NightLightMode trigger | Mode Control Entity |

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
  - alias: "Away Mode Volume"
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