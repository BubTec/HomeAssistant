# Smart Volume Control for Media Players

This Home Assistant blueprint automatically adjusts volume levels of media players based on mode changes such as night mode, presence detection, or any other state change. Perfect for creating context-aware audio environments with Echo devices, speakers, and other media players.

## Features

- 🔊 **Automatic Volume Control**: Adjusts volume based on any boolean or state entity
- 🌙 **Night Mode Support**: Perfect for lowering volumes during night hours
- 📱 **Multiple Device Types**: Works with any media_player entity (Echo, Sonos, etc.)
- 🚫 **Ignore Lists**: Exclude specific devices from automatic control
- ⭐ **Special Device Handling**: Configure one device with different volume levels
- ⏱️ **Smart Delays**: Optional random delays to prevent command conflicts
- 🔍 **Auto-Discovery**: Can automatically find all media players or use specific selection
- 🎯 **Flexible Triggers**: Works with input_boolean, binary_sensor, switch, or any state entity

## Use Cases

- **Night Mode**: Lower volumes when everyone goes to sleep
- **Presence Detection**: Adjust volumes when leaving/arriving home  
- **Work Hours**: Reduce volumes during work-from-home hours
- **Guest Mode**: Set appropriate volumes when guests are present
- **Party Mode**: Increase volumes for entertainment
- **Baby Sleep**: Ultra-quiet mode when baby is sleeping

## Configuration

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Mode Control Entity** | Entity that triggers volume changes | `input_boolean.night_mode` |

### Optional Inputs

| Input | Description | Default |
|-------|-------------|---------|
| **Media Players** | Specific players to control (empty = all) | Auto-discover all |
| **Low Volume Level** | Volume when mode is active (%) | 20 |
| **High Volume Level** | Volume when mode is inactive (%) | 40 |
| **Ignored Media Players** | Players to exclude | None |
| **Special Device** | Device with different volume levels | None |
| **Special Low Volume** | Special device low volume (%) | 30 |
| **Special High Volume** | Special device high volume (%) | 80 |
| **Use Random Delays** | Prevent simultaneous commands | True |
| **Maximum Random Delay** | Max delay in seconds | 10 |
| **Special Device Delay** | Fixed delay for special device | 15 |

## Setup Examples

### Basic Night Mode

```yaml
# Create input_boolean helper
input_boolean:
  night_mode:
    name: Night Mode
    initial: false
```

Blueprint Configuration:
- **Mode Control Entity**: `input_boolean.night_mode`
- **Low Volume**: 15 (night volume)
- **High Volume**: 50 (day volume)

### Advanced Configuration with Special Device

```yaml
# Blueprint Configuration
Mode Control Entity: input_boolean.quiet_hours
Media Players: 
  - media_player.living_room_echo
  - media_player.kitchen_echo
  - media_player.bedroom_echo
Ignored Media Players:
  - media_player.basement_speaker
Special Device: media_player.main_echo
Special Low Volume: 25
Special High Volume: 75
Use Random Delays: true
Maximum Random Delay: 5
```

### Presence-Based Control

```yaml
# Use presence sensor as trigger
Mode Control Entity: binary_sensor.everyone_away
Low Volume: 0   # Mute when away
High Volume: 40 # Normal when home
```

## How It Works

1. **Trigger**: Activates when the mode control entity changes state
2. **Mode Detection**: Automatically detects if mode is active based on entity type:
   - `input_boolean`/`switch`: ON = active
   - `binary_sensor`: ON = active  
   - Other entities: 'on', 'true', 'active', 'home' = active
3. **Device Control**: 
   - Normal devices get low/high volume based on mode
   - Special device gets custom volume levels
   - Ignored devices are skipped
4. **Smart Timing**: Random delays prevent command conflicts

## Technical Details

### Supported Entity Types

- ✅ `input_boolean` - Manual toggles
- ✅ `binary_sensor` - Motion, presence, door sensors
- ✅ `switch` - Any switch entity
- ✅ `sensor` - Custom sensors with state values

### Volume Levels

Volume levels are specified as percentages (0-100) and automatically converted to Home Assistant's 0.0-1.0 scale.

### Error Handling

- Uses `continue_on_error: true` to prevent failures with unavailable devices
- Template conditions prevent execution when entities are unavailable
- Automatic filtering of non-existent devices

## Troubleshooting

### Common Issues

**Blueprint doesn't trigger:**
- Check that mode control entity exists and changes state
- Verify the entity type is supported

**Some devices don't respond:**
- Ensure devices are online and available
- Check device names match exactly
- Some devices may need a brief delay between commands

**Volumes not applied correctly:**
- Volume levels should be 0-100 (percentages)
- Some devices may have minimum/maximum volume limits

### Debugging

Enable debug logging to see what's happening:

```yaml
logger:
  logs:
    homeassistant.components.automation: debug
```

## Advanced Tips

### Custom Mode Detection

For complex mode detection, create a template binary sensor:

```yaml
binary_sensor:
  - platform: template
    sensors:
      smart_quiet_mode:
        friendly_name: "Smart Quiet Mode"
        value_template: >
          {{ is_state('input_boolean.night_mode', 'on') or 
             is_state('binary_sensor.baby_sleeping', 'on') or
             (now().hour >= 22 or now().hour <= 6) }}
```

### Multiple Volume Profiles

Create different blueprints for different scenarios:
- Night mode (very quiet)
- Work hours (medium quiet)  
- Party mode (loud)
- Guest mode (moderate)

### Integration with Other Automations

Combine with other automations for complete smart home control:
- Dim lights when volume is lowered
- Send notifications about mode changes
- Adjust thermostats based on presence

## Related Blueprints

This blueprint pairs well with:
- Motion-activated lighting
- Presence detection automations
- Smart doorbell integrations
- Time-based scene controllers 