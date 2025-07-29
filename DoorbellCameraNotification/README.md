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
- **Notification Sound (iOS)**: iOS notification sound file
- **Notification Channel (Android)**: Android notification channel for custom sounds
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

## Notification Sounds

Notification sounds work differently on iOS and Android:

### iOS Custom Sounds

iOS supports direct sound file specification in the notification:

```yaml
notification_sound: "US-EN-Morgan-Freeman-Someone-Is-Arriving.wav"
```

Available pre-installed sounds include:
- `US-EN-Morgan-Freeman-Someone-Is-Arriving.wav`
- `US-EN-Alexa-Motion-At-Front-Door.wav`
- `US-EN-Daisy-Front-Door-Motion.wav`
- And many more...

You can also upload custom sounds via iTunes or cloud storage.

### Android Notification Channels

Android uses notification channels to manage sounds. Each channel can have its own sound:

1. **Set a custom channel in the blueprint**:
   ```yaml
   notification_channel: "doorbell_alerts"
   ```

2. **Configure the sound on your Android device**:
   - Go to **Settings** > **Apps** > **Home Assistant**
   - Select **Notifications** > **Companion app** > **Notification channels**
   - Find your channel (e.g., "doorbell_alerts")
   - Tap on it and select **Sound**
   - Choose from system sounds or add custom sounds

3. **Create multiple channels for different purposes**:
   - `doorbell_front` - Front door alerts
   - `doorbell_back` - Back door alerts  
   - `doorbell_urgent` - Emergency alerts

### Tips for Both Platforms

- Test notification sounds during setup
- Consider different sound volumes for day/night
- Use distinct sounds for different types of alerts
- Some Android devices may require notification permissions to be manually enabled

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

### Android Notification Channel Examples

**Front Door (High Priority)**
```yaml
notification_channel: "doorbell_front_door"
notification_title: "Front Door Visitor"
```

**Back Door (Normal Priority)**  
```yaml
notification_channel: "doorbell_back_door"
notification_title: "Back Door Activity"
```

**Emergency/Security**
```yaml
notification_channel: "doorbell_security"
notification_title: "Security Alert"
```

After creating these automations, configure different sounds for each channel in your Android settings.

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
- **iOS sound not playing**: Ensure sound file exists and device is not in silent mode
- **Android custom sound not working**: 
  - Check notification channel settings on device
  - Ensure Home Assistant app has notification permissions
  - Try creating a test notification to verify channel setup
- **Android notification channel not created**: Channel is created automatically on first notification

## Based On

This blueprint is based on the community blueprint by @rg3d: [Doorbell cam actionable notification with app launcher](https://community.home-assistant.io/t/doorbell-cam-actionable-notification-with-app-launcher/489144) 