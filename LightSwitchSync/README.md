# 🔗 Light/Switch Synchronization Blueprint

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A//raw.githubusercontent.com/n3roGit/HomeAssistant/main/LightSwitchSync/LightSwitchSync.yaml)

A Home Assistant blueprint that synchronizes multiple lights or switches with a master device. When the master device is controlled, all slave devices automatically follow the same state, brightness, and color settings.

## Features

- **Master-Slave Control**: One master device controls multiple slave devices
- **Mixed Device Types**: Works with lights, switches, or a combination of both
- **Brightness Synchronization**: Optional brightness level synchronization for lights
- **Color Synchronization**: Optional color synchronization for RGB lights
- **Bidirectional Support**: Can be used in both directions (master ↔ slave)
- **Smart Detection**: Automatically detects device types and uses appropriate services

## Requirements

### Required Devices
- **Master Device**: Light or switch that controls all others
- **Slave Devices**: One or more lights or switches to be synchronized

## Installation

1. **Import Blueprint**: Click the import button above
2. **Configure Devices**: Set up your master and slave devices
3. **Create Automation**: Use the blueprint to create a new automation
4. **Test Functionality**: Verify the synchronization works as expected

## Configuration

### Basic Settings
- **Master Device**: The main light or switch that controls all others
- **Slave Devices**: List of lights or switches that should follow the master
- **Sync Brightness**: Also synchronize brightness levels (lights only)
- **Sync Color**: Also synchronize color settings (RGB lights only)

## How It Works

1. **State Change**: When the master device state changes (on/off)
2. **Type Detection**: Blueprint detects if master is a light or switch
3. **Service Selection**: Uses appropriate service (light.turn_on/off or switch.turn_on/off)
4. **Synchronization**: Applies the same state to all slave devices
5. **Advanced Features**: If enabled, also syncs brightness and color

## Configuration Examples

### Basic Light Synchronization
```yaml
alias: "Living Room Light Sync"
use_blueprint:
  path: light_switch_sync.yaml
  input:
    master_device: light.living_room_main
    slave_devices:
      - light.living_room_lamp
      - light.living_room_spot
    sync_brightness: true
    sync_color: false
```

### Switch and Light Mix
```yaml
alias: "Kitchen Device Sync"
use_blueprint:
  path: light_switch_sync.yaml
  input:
    master_device: switch.kitchen_main
    slave_devices:
      - light.kitchen_under_cabinet
      - switch.kitchen_fan
    sync_brightness: false
    sync_color: false
```

### RGB Light with Color Sync
```yaml
alias: "Bedroom RGB Sync"
use_blueprint:
  path: light_switch_sync.yaml
  input:
    master_device: light.bedroom_main
    slave_devices:
      - light.bedroom_lamp
      - light.bedroom_strip
    sync_brightness: true
    sync_color: true
```

## Use Cases

- **Room Lighting**: Main light controls additional lamps and spots
- **Kitchen Setup**: Main switch controls under-cabinet lights and fan
- **Bedroom Ambiance**: Main light controls bedside lamps and LED strips
- **Office Setup**: Main light controls desk lamp and monitor backlight
- **Garage Control**: Main switch controls multiple garage lights

## Advanced Features

### Brightness Synchronization
When enabled, slave lights will match the brightness percentage of the master light:
- Master at 50% brightness → All slaves at 50% brightness
- Works with dimmable lights only

### Color Synchronization
When enabled, RGB slave lights will match the color of the master light:
- Master set to red → All slaves turn red
- Works with RGB lights only

### Mixed Device Types
The blueprint automatically handles different device types:
- Master: Light, Slaves: Mix of lights and switches
- Master: Switch, Slaves: Mix of lights and switches
- Appropriate services are used for each device type

## Troubleshooting

### Common Issues

1. **Slave devices don't respond**:
   - Check if slave devices are accessible
   - Verify device types are supported (light/switch)
   - Ensure automation is enabled

2. **Brightness sync not working**:
   - Ensure both master and slave lights support dimming
   - Check if sync_brightness is enabled
   - Verify master light has brightness attribute

3. **Color sync not working**:
   - Ensure both master and slave lights support RGB
   - Check if sync_color is enabled
   - Verify master light has rgb_color attribute

### Device Compatibility

**Supported Master Devices:**
- Lights (dimmable, RGB, basic)
- Switches (smart switches, relays)

**Supported Slave Devices:**
- Lights (dimmable, RGB, basic)
- Switches (smart switches, relays)

**Not Supported:**
- Groups (use individual devices instead)
- Non-switchable devices
- Devices without on/off capability

## Benefits

This blueprint provides:
- **Centralized Control**: Control multiple devices with one switch
- **Consistent Behavior**: All devices respond identically
- **Flexible Setup**: Mix and match different device types
- **Advanced Features**: Optional brightness and color synchronization
- **Easy Configuration**: Simple setup through Home Assistant UI 