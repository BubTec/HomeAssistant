# Mailbox Monitor Blueprint

A Home Assistant blueprint that monitors your mailbox using two sensors to detect mail insertion and mailbox emptying, automatically tracking status and sending notifications.

## Features

- **Dual Sensor Monitoring**: Uses separate sensors for mail insertion and mailbox emptying detection
- **Automatic Status Tracking**: Maintains mailbox status using an input boolean helper
- **Flexible Notifications**: Configurable notification service and message
- **Debug Logging**: Optional logging for troubleshooting
- **Parallel Mode**: Handles multiple triggers simultaneously

## Requirements

### Hardware
- **Mail Insertion Sensor**: A binary sensor (e.g., door/window sensor, PIR sensor, or custom sensor) that detects when mail is inserted
- **Mailbox Emptying Sensor**: A binary sensor that detects when the mailbox is opened/accessed for emptying

### Home Assistant Setup
Before using this blueprint, create:

1. **Input Boolean Helper**:
   ```yaml
   input_boolean:
     mailbox_has_mail:
       name: "Mailbox Has Mail"
       icon: mdi:mailbox
   ```

2. **Binary Sensors**: Configure your physical sensors as binary sensors in Home Assistant

## Blueprint Inputs

| Input | Description | Type | Required |
|-------|-------------|------|----------|
| **Mail Inserted Sensor** | Binary sensor detecting mail insertion | Entity (binary_sensor) | Yes |
| **Mailbox Emptied Sensor** | Binary sensor detecting mailbox emptying | Entity (binary_sensor) | Yes |
| **Mailbox Status Helper** | Input boolean tracking mail status | Entity (input_boolean) | Yes |
| **Notification Service** | Service for notifications | Text | No (default: notify.notify) |
| **Notification Message** | Message when mail arrives | Text | No (default: "You have mail in your mailbox!") |
| **Enable Logging** | Enable debug logging | Boolean | No (default: true) |

## How It Works

1. **Mail Insertion**: When the mail insertion sensor triggers, the automation:
   - Logs the event (if logging enabled)
   - Sets the mailbox status helper to "on"

2. **Status Change**: When the mailbox status changes to "has mail":
   - Sends a notification using the configured service and message

3. **Mailbox Emptying**: When the mailbox emptying sensor triggers:
   - Logs the event (if logging enabled)
   - Sets the mailbox status helper to "off"

## Installation

1. **Import Blueprint**:
   - Copy the blueprint YAML content
   - Go to Configuration → Blueprints → Import Blueprint
   - Paste the content or upload the file

2. **Create Automation**:
   - Click "Create Automation"
   - Configure the required inputs
   - Save the automation

## Configuration Examples

### Basic Setup
```yaml
alias: "Mailbox Monitor"
use_blueprint:
  path: mailbox_monitor.yaml
  input:
    mail_inserted_sensor: binary_sensor.mailbox_door
    mailbox_emptied_sensor: binary_sensor.mailbox_access
    mailbox_status_helper: input_boolean.mailbox_has_mail
```

### Advanced Setup with Custom Notifications
```yaml
alias: "Smart Mailbox Monitor"
use_blueprint:
  path: mailbox_monitor.yaml
  input:
    mail_inserted_sensor: binary_sensor.mailbox_mail_sensor
    mailbox_emptied_sensor: binary_sensor.mailbox_door_sensor
    mailbox_status_helper: input_boolean.mailbox_has_mail
    notification_service: notify.mobile_app_your_phone
    notification_message: "📬 New mail has arrived in your mailbox!"
    enable_logging: true
```

## Sensor Ideas

### Mail Insertion Detection
- **Magnetic Door/Window Sensor**: Attach to a mail slot or internal flap
- **PIR Motion Sensor**: Detect movement inside the mailbox
- **Weight Sensor**: Detect weight changes when mail is added
- **Light Sensor**: Detect light changes when mail slot opens

### Mailbox Access Detection
- **Door Sensor**: Detect when mailbox door opens
- **Magnetic Contact**: Monitor mailbox access panel
- **Vibration Sensor**: Detect when mailbox is accessed

## Troubleshooting

### Common Issues

1. **False Triggers**: 
   - Adjust sensor sensitivity
   - Add delays or conditions to filter unwanted triggers
   - Check sensor placement

2. **Missing Notifications**:
   - Verify notification service configuration
   - Check Home Assistant logs
   - Test notification service manually

3. **Status Not Updating**:
   - Ensure input boolean entity exists
   - Check automation logs
   - Verify sensor states are changing correctly

### Debug Logging

Enable logging in the blueprint and check logs at:
Configuration → System → Logs

Look for entries from `blueprints.mailbox_monitor`

## Integration Ideas

- **Dashboard Card**: Display mailbox status on your dashboard
- **Alexa/Google Integration**: Voice announcements for mail arrival
- **Security Integration**: Combine with cameras for mail theft prevention
- **Delivery Notifications**: Coordinate with package delivery sensors

## Related Blueprints

- **SmartWelcomeGreeter**: Welcome visitors and delivery personnel
- **BirthdayReminder**: Get reminded of special deliveries

## Version History

- **v1.0**: Initial release with dual sensor monitoring and notifications 