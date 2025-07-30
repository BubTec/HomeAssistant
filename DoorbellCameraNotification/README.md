# Doorbell Camera Notification with Door Opener

A Home Assistant blueprint that sends actionable notifications with camera snapshots when someone rings the doorbell. The notification includes a photo and a button to remotely open the door.

## Features

- 📸 **Camera Snapshot**: Automatically takes a photo when the doorbell is triggered
- 📱 **Mobile Notifications**: Sends notifications to your mobile devices with the camera snapshot
- 🔔 **Persistent Notifications**: Shows alerts in Home Assistant sidebar for all users with auto-dismiss option
- 🚪 **Door Opener**: Includes an action button to remotely open the door
- 🎛️ **Dashboard Integration**: Clicking the notification opens your specified dashboard view
- 🔊 **Custom Sounds**: Configurable notification sounds for iOS and Android devices
- ⏱️ **Timeout Control**: Configurable timeout for notification actions
- 📺 **Fully Kiosk Integration**: Automatically redirects tablet displays via REST API and button controls
- 🌟 **Auto-Return**: Tablets return to configured normal URL after timeout
- ⚙️ **Simple Configuration**: Fixed URL configuration without complex helper dependencies

## Requirements

- Home Assistant with the Mobile App integration
- A camera entity (for taking snapshots)
- A trigger entity (switch, binary_sensor, button, etc.)
- An action to open the door (switch, script, etc.)
- Mobile device with the Home Assistant Companion App
- **Optional**: Fully Kiosk Browser Integration for tablet dashboard control

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
- **Fully Kiosk Tablets**: Select Fully Kiosk tablet entities (e.g., `media_player.buro_tablet`)
- **Kiosk Dashboard URL**: Dashboard path to display when doorbell rings
- **Normal Start URL**: Standard URL to return to after timeout
- **Kiosk Return Timeout**: Time before tablets return to normal URL (0 = no auto-return)
- **Wake Tablet Screens**: Whether to wake up sleeping tablets
- **Enable Persistent Notification**: Show notification in Home Assistant sidebar for all users
- **Persistent Notification Title**: Custom title for the sidebar notification
- **Persistent Notification Message**: Custom message content (use {{timestamp}} as placeholder for time)
- **Auto-dismiss Persistent Notification**: Time after which to automatically remove the notification (0 = manual dismiss only)

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

### 4. Setup Fully Kiosk Integration (Optional)

If you want to redirect tablet displays when the doorbell rings:

1. **Install Fully Kiosk Browser** app on your tablets
2. **Install the Fully Kiosk Browser integration** in Home Assistant:
   - Go to **Settings** > **Devices & Services** > **Add Integration**
   - Search for "Fully Kiosk Browser"
   - Configure with your tablet's IP address and password
3. Your tablets will appear as `media_player` entities (e.g., `media_player.buro_tablet`)

### 5. Ensure Directory Exists

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

### Fully Kiosk Tablet Configuration Examples

**Basic Tablet Redirect**
```yaml
kiosk_tablets:
  - media_player.buro_tablet
  - media_player.kuche_tablet
kiosk_dashboard_url: "https://your.hass.io/dashboard-home/entrance"
kiosk_normal_url: "https://your.hass.io/dashboard-home"
kiosk_return_timeout: 30
kiosk_wake_screen: true
```

**Different Dashboards per Blueprint**
```yaml
# Entrance Door Blueprint
kiosk_tablets: 
  - media_player.buro_tablet
kiosk_dashboard_url: "https://your.hass.io/dashboard-security/entrance-full"
kiosk_normal_url: "https://your.hass.io/dashboard-home"
kiosk_return_timeout: 45

# Back Door Blueprint
kiosk_tablets:
  - media_player.kuche_tablet
kiosk_dashboard_url: "https://your.hass.io/dashboard-home/entrance-compact"
kiosk_normal_url: "https://your.hass.io/dashboard-kiosk"
kiosk_return_timeout: 20
```

**No Auto-Return (Manual Navigation)**
```yaml
kiosk_tablets:
  - media_player.buro_tablet
kiosk_dashboard_url: "https://your.hass.io/dashboard-home/entrance"
kiosk_normal_url: "https://your.hass.io/dashboard-home"
kiosk_return_timeout: 0  # No automatic return
kiosk_wake_screen: true
```

### Persistent Notification Configuration Examples

**Always Show with Auto-Dismiss**
```yaml
enable_persistent_notification: true
persistent_notification_title: "🔔 Doorbell Alert"
persistent_notification_message: "Someone rang the doorbell at {{timestamp}}."
persistent_notification_auto_dismiss: 300  # Auto-dismiss after 5 minutes
```

**Custom Message with Details**
```yaml
enable_persistent_notification: true
persistent_notification_title: "🚨 Front Door Visitor"
persistent_notification_message: "🔔 DOORBELL: Visitor detected at front door ({{timestamp}}). Please check camera and respond if needed."
persistent_notification_auto_dismiss: 0  # No auto-dismiss, manual only
```

**Completely Custom Title and Message**
```yaml
enable_persistent_notification: true
persistent_notification_title: "Windfang Klingel"  # Your custom title
persistent_notification_message: "Someone rang the doorbell at {{timestamp}}."  # Your custom message
persistent_notification_auto_dismiss: 300
```

**Different Messages for Different Doors**
```yaml
# Front Door Blueprint
persistent_notification_title: "🔔 Front Door"
persistent_notification_message: "Someone is at the front door ({{timestamp}}). Camera snapshot available below."

# Back Door Blueprint  
persistent_notification_title: "🔔 Back Door"
persistent_notification_message: "Back door activity detected at {{timestamp}}. Check who is there."

# Emergency Entry Blueprint
persistent_notification_title: "🚨 Security Alert"
persistent_notification_message: "⚠️ SECURITY: Unauthorized entry attempt detected at {{timestamp}}! Immediate attention required."
```

**Simple Short Message**
```yaml
enable_persistent_notification: true
persistent_notification_title: "🔔 Doorbell"
persistent_notification_message: "Visitor at {{timestamp}}"
persistent_notification_auto_dismiss: 180  # Auto-dismiss after 3 minutes
```

**Disabled Persistent Notifications**
```yaml
enable_persistent_notification: false
```

## Usage

1. When someone triggers the doorbell entity, the automation:
   - Takes a snapshot from the configured camera
   - Sends a notification with the photo to your mobile device(s)
   - **Creates a persistent notification** in the Home Assistant sidebar (if enabled)
   - Shows an "Open Door" button in the notification
   - **Optionally redirects Fully Kiosk tablets** to the doorbell dashboard

2. **Mobile Notifications:**
   - **Clicking the notification** opens your specified dashboard view
   - **Clicking the "Open Door" button** executes your configured door opener action

3. **Persistent Notifications:**
   - **Visible to all users** in the Home Assistant sidebar
   - **Shows camera snapshot directly** in the notification (HTML embedded image)
   - **Fully customizable title and message** content
   - **Timestamp placeholder** support in messages ({{timestamp}})
   - **Responsive image sizing** with rounded corners for better appearance
   - **Includes dashboard link** for easy access
   - **Auto-dismisses** after the configured time (if enabled)
   - **Manual dismissal** by clicking the X button in the sidebar

4. **Tablet Display Control:**
   - Wakes up sleeping tablets (if enabled)
   - Redirects to the doorbell dashboard immediately
   - Automatically returns to original view after timeout (if configured)
   - Multiple tablets can show different dashboard views

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
- **Tablets not redirecting**: 
  - Check Fully Kiosk integration is installed and tablets are discovered
  - Verify tablet entities are `media_player` domain with `fully_kiosk` integration
  - Test manually: Developer Tools > Services > `fully_kiosk.load_url`
  - Check that `fully_kiosk.load_url` service is available
- **Tablets not waking up**: 
  - Check "Wake Tablet Screens" is enabled
  - Verify screen switch entity exists (e.g., `switch.buro_tablet_bildschirm`)
  - Test manually: Developer Tools > Services > `switch.turn_on` on screen switch
- **Tablets not returning to normal view**: 
  - Check return timeout is > 0
  - Verify normal start URL is configured correctly
  - Test manually: Use `fully_kiosk.load_url` service with normal URL
- **Service not found errors**:
  - Verify Fully Kiosk Browser integration is properly installed
  - Check that tablets are discovered and showing as `media_player` entities
  - Restart Home Assistant after installing the integration
- **Persistent notification not showing**: 
  - Check "Enable Persistent Notification" is set to true
  - Verify notification appears in Home Assistant sidebar (bell icon)
  - Check Home Assistant logs for any errors in `persistent_notification.create` service
- **Persistent notification not auto-dismissing**: 
  - Verify auto-dismiss time is greater than 0
  - Check if automation completed successfully (no errors in logs)
  - Manual dismissal works regardless of auto-dismiss setting
- **Persistent notification image not showing**: 
  - Ensure camera snapshot was saved successfully to `/config/www/doorbell/`
  - Check file permissions on the www directory
  - Verify the camera entity is working and accessible
  - Test the image URL manually: `http://your-ha-instance/local/doorbell/filename.jpg`
  - The image is now embedded using HTML `<img>` tags for better compatibility
  - Check browser console for any image loading errors
- **Custom message not working**: 
  - Check that `{{timestamp}}` placeholder is used correctly in the message
  - Verify the message input field accepts the custom text
  - Template syntax errors will prevent the automation from running
- **Links in persistent notification not working**: 
  - Ensure camera snapshot was saved successfully
  - Check dashboard view path is correct and accessible
  - Links use Home Assistant's internal URL structure

## Based On

This blueprint is based on the community blueprint by @rg3d: [Doorbell cam actionable notification with app launcher](https://community.home-assistant.io/t/doorbell-cam-actionable-notification-with-app-launcher/489144) 