# 💡 Motion-Activated Light Off Blueprint

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A//raw.githubusercontent.com/n3roGit/HomeAssistant/main/MotionActivatedLightOff/MotionActivatedLightOff.yaml)

A Home Assistant blueprint that automatically turns off lights after a specified time when no motion is detected. Perfect for energy saving and convenience in rooms where you want lights to automatically turn off when not in use.

## Features

- **Automatic Light Control**: Turns off lights after configurable delay when no motion is detected
- **Motion Detection**: Monitors motion sensors to determine when to start/stop the turn-off timer
- **Timer Cancellation**: Cancels the turn-off timer when motion is detected again
- **Flexible Configuration**: Configurable delay time and support for individual lights or light groups
- **Debug Logging**: Optional logging for troubleshooting and monitoring
- **Smart Logic**: Only operates when lights are already on

## Requirements

### Required Sensors
- **Motion Sensor**: Binary sensor that detects movement in the area
- **Light Entity**: Light or light group to control

## Installation

1. **Import Blueprint**: Click the import button above
2. **Configure Sensors**: Ensure your motion sensor and light entity are working
3. **Create Automation**: Use the blueprint to create a new automation
4. **Test Functionality**: Verify the automation works as expected

## Configuration

### Basic Settings
- **Motion Sensor**: Binary sensor that detects movement
- **Light Entity**: Light or light group to control
- **Turn Off Delay**: Time in minutes to wait before turning off the light (default: 5 minutes)
- **Enable Logging**: Optional debug logging for troubleshooting

## How It Works

1. **Motion Stops**: When motion stops and the light is on:
   - Starts the turn-off timer
   - Logs the timer start (if logging enabled)

2. **Timer Expires**: After the specified delay:
   - Checks if motion is still not detected
   - Checks if the light is still on
   - Turns off the light
   - Logs the action (if logging enabled)

**Note**: Each time motion stops, a new timer starts. If motion is detected again, the automation will trigger again when motion stops.

## Configuration Examples

### Basic Setup
```yaml
alias: "Kitchen Light Auto Off"
use_blueprint:
  path: motion_activated_light_off.yaml
  input:
    motion_sensor: binary_sensor.kitchen_motion
    light_entity: light.kitchen_lights
    turn_off_delay: 5
    enable_logging: true
```

### Advanced Setup with Light Group
```yaml
alias: "Living Room Lights Auto Off"
use_blueprint:
  path: motion_activated_light_off.yaml
  input:
    motion_sensor: binary_sensor.living_room_motion
    light_entity: light.living_room_group
    turn_off_delay: 10
    enable_logging: false
```

### Short Delay for Bathroom
```yaml
alias: "Bathroom Light Auto Off"
use_blueprint:
  path: motion_activated_light_off.yaml
  input:
    motion_sensor: binary_sensor.bathroom_motion
    light_entity: light.bathroom_light
    turn_off_delay: 2
    enable_logging: true
```



## Troubleshooting

### Common Issues

1. **Light doesn't turn off**:
   - Check if the motion sensor is working correctly
   - Verify the light entity is accessible
   - Ensure the automation is enabled

2. **Timer restarts when motion detected**:
   - This is normal behavior - each time motion stops, a new timer starts
   - The automation will trigger again when motion stops again

3. **Logging not working**:
   - Ensure the enable_logging option is set to true
   - Check Home Assistant logs for notification service errors

### Debug Mode

Enable logging to see detailed information about:
- Timer start/cancellation events
- Light turn-off actions
- Motion detection events

## Use Cases

- **Kitchen**: Turn off lights when no one is cooking
- **Bathroom**: Automatic light control for energy saving
- **Hallway**: Lights off when no movement detected
- **Workshop**: Turn off lights when leaving the workspace
- **Garage**: Automatic light control for convenience

## Energy Saving Benefits

This blueprint helps reduce energy consumption by:
- Automatically turning off lights when not needed
- Preventing lights from staying on unnecessarily
- Providing convenience without manual intervention
- Supporting sustainable home automation practices 