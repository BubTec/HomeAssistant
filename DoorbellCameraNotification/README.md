# Doorbell Camera Notification with Door Opener

A Home Assistant blueprint that sends actionable notifications with camera snapshots when someone rings the doorbell. The notification includes a photo and a button to remotely open the door.

## Features

- 📸 **Camera Snapshot**: Automatically takes a photo when the doorbell is triggered
- 📱 **Mobile Notifications**: Sends notifications to your mobile devices with the camera snapshot
- 🚪 **Door Opener**: Includes an action button to remotely open the door
- 🎛️ **Dashboard Integration**: Clicking the notification opens your specified dashboard view
- 🔊 **Custom Sounds**: Configurable notification sounds for iOS devices
- ⏱️ **Timeout Control**: Configurable timeout for notification actions

## Requirements

- Home Assistant with the Mobile App integration
- A camera entity (for taking snapshots)
- A trigger entity (switch, binary_sensor, button, etc.)
- An action to open the door (switch, script, etc.)
- Mobile device with the Home Assistant Companion App

## Setup

### 1. Import the Blueprint

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://github.com/your-repo/HomeAssistant/blob/main/DoorbellCameraNotification/DoorbellCameraNotification.yaml)

### 2. Configure the Automation

When creating an automation from this blueprint, configure:

- **Doorbell Trigger Entity**: The entity that triggers when someone rings (e.g., `switch.doorbell_button`)
- **Doorbell Camera**: The camera to take snapshots from (e.g., `camera.front_door`)
- **Notification Target**: Where to send notifications (e.g., `notify.mobile_app_iphone` or `notify.all_mobile`)
- **Notification Title**: Custom title for the notification
- **Dashboard View**: Path to open when notification is clicked (e.g., `/dashboard-home/entrance`)
- **Door Opener Action**: Action to perform when "Open Door" is pressed
- **Door Button Title**: Text for the door opener button
- **Notification Sound**: iOS notification sound file
- **Action Timeout**: How long the action button remains active

### 3. Create Notification Groups (Optional)

To send notifications to multiple devices, add this to your `configuration.yaml`:

```yaml
notify:
  - name: all_mobile
    platform: group
    services:
      - service: mobile_app_iphone
      - service: mobile_app_android_phone
```

### 4. Ensure Directory Exists

The blueprint saves snapshots to `/config/www/doorbell/`. Make sure this directory exists:

```bash
mkdir -p /config/www/doorbell
```

## Configuration Examples

### Basic Switch Door Opener
```yaml
door_opener_action:
  - action: switch.turn_on
    target:
      entity_id: switch.front_door_opener
```

### Script-based Door Opener
```yaml
door_opener_action:
  - action: script.open_front_door
```

### Multiple Actions
```yaml
door_opener_action:
  - action: switch.turn_on
    target:
      entity_id: switch.door_lock
  - delay:
      seconds: 2
  - action: switch.turn_off
    target:
      entity_id: switch.door_lock
```

## Usage

1. When someone triggers the doorbell entity, the automation:
   - Takes a snapshot from the configured camera
   - Sends a notification with the photo to your mobile device(s)
   - Shows an "Open Door" button in the notification

2. **Clicking the notification** opens your specified dashboard view
3. **Clicking the "Open Door" button** executes your configured door opener action

## Snapshots

Camera snapshots are automatically saved to `/config/www/doorbell/` with timestamps. You can access them via:
- Local path: `/config/www/doorbell/YYYY-MM-DD_HH-MM-SS.jpg`
- Web path: `/local/doorbell/YYYY-MM-DD_HH-MM-SS.jpg`

## Tips

- Test your door opener action separately before using it in the blueprint
- Consider creating a script for complex door opening sequences
- Snapshots are not automatically deleted - you may want to create a separate automation to clean them up periodically
- The notification action timeout prevents accidental door opening after the event

## Troubleshooting

- **No notification received**: Check your notification service name and mobile app setup
- **No snapshot**: Verify camera entity is working and `/config/www/doorbell/` directory exists
- **Door opener not working**: Test the action independently in Developer Tools
- **Automation not appearing**: Check YAML syntax and blueprint import

## Based On

This blueprint is based on the community blueprint by @rg3d: [Doorbell cam actionable notification with app launcher](https://community.home-assistant.io/t/doorbell-cam-actionable-notification-with-app-launcher/489144) 