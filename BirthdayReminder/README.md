# Birthday Reminder with Smart Notifications

This Home Assistant blueprint automates birthday reminders and congratulations for multiple people. It sends different types of notifications based on how many days are left until each person's birthday and can optionally play birthday music on the actual day.

## Features

- 🎂 **Multiple People**: Support for unlimited number of birthdays
- 📅 **Smart Timing**: Different messages for today, tomorrow, 2 days, and up to 30 days ahead
- 🔔 **Flexible Notifications**: Works with any Home Assistant notification service
- 🎵 **Birthday Music**: Optional music playback on birthday using media player
- 🏠 **Presence Detection**: Optional check if someone is home before sending notifications
- ⏰ **Multiple Daily Checks**: Configurable morning, midday, and evening notification times
- 🎯 **Age Calculation**: Automatically calculates and includes the correct age with proper ordinals (1st, 2nd, 3rd, etc.)

## Configuration

### Required Inputs

- **Birthday Data**: JSON list of people and their birth dates
- **Notification Service**: Home Assistant service for sending notifications

### Optional Inputs

- **Media Player**: Entity for playing birthday music
- **Presence Entity**: Entity to check if someone is home
- **Notification Times**: Three separate time inputs for daily checks
- **Days Ahead**: How many days before birthday to start reminders (1-30)
- **Birthday Songs**: List of songs to play randomly on birthdays

## Birthday Data Format

The birthday data should be provided as a JSON list in the following format:

```json
[
  {"name": "John Doe", "date": "1990-05-15"},
  {"name": "Jane Smith", "date": "1985-12-03"},
  {"name": "Child Name", "date": "2015-08-22"}
]
```

**Important**: 
- Use YYYY-MM-DD format for dates
- Names can contain spaces and special characters
- Ensure proper JSON syntax with quotes around strings

## Notification Examples

### Birthday Today (Day 0)
```
🎉 Birthday Today!
Today John Doe celebrates their 34th birthday! 
Happy Birthday and all the best wishes! 🎂🎈
```

### Birthday Tomorrow (Day 1)
```
🎂 Birthday Tomorrow!
Tomorrow Jane Smith will celebrate their 39th birthday! 
Don't forget to prepare something special! 🎁
```

### 2 Days Until Birthday
```
📅 Birthday in 2 Days
In 2 days Child Name will turn 9. 
Is everything prepared for the celebration? 🎊
```

### 3+ Days Until Birthday
```
🗓️ Upcoming Birthday
John Doe's 34th birthday is coming up in 5 days 
(May 15)! 🎈
```

## Setup Instructions

1. **Import Blueprint**: Copy the blueprint YAML file to your Home Assistant blueprints folder
2. **Create Automation**: Go to Settings → Automations & Scenes → Create Automation → Use Blueprint
3. **Configure Birthday Data**: Enter your birthday list in JSON format
4. **Set Notification Service**: Choose your preferred notification method (e.g., `notify.mobile_app_yourphone`)
5. **Optional Settings**: Configure media player, presence detection, and timing preferences
6. **Save and Test**: Enable the automation and test with a near-future birthday

## Supported Notification Services

- **Mobile Apps**: `notify.mobile_app_yourphone`
- **Persistent Notifications**: `notify.persistent_notification`
- **Email**: `notify.email`
- **TTS/Alexa**: `tts.google_translate_say`, `notify.alexa_media`
- **Telegram**: `notify.telegram`
- **And many more**: Any Home Assistant notify service

## Media Player Integration

If you configure a media player, the blueprint will:
- Play a random song from your birthday songs list
- Only trigger on the actual birthday (day 0)
- Add a 10-second delay before playing music
- Support any Home Assistant media player entity

## Presence Detection

Configure an optional presence entity to only send notifications when someone is home:
- **Person entities**: `person.john_doe`
- **Device trackers**: `device_tracker.johns_phone`
- **Binary sensors**: `binary_sensor.someone_home`
- **Input booleans**: `input_boolean.home_mode`

## Advanced Usage

### Custom Notification Times
The blueprint checks for birthdays at three configurable times:
- **Morning** (default: 07:30)
- **Midday** (default: 12:00) 
- **Evening** (default: 18:30)

### Birthday Music Playlist
Provide a comma-separated list of songs or media content IDs:
```
Happy Birthday Song, Birthday Celebration Music, Birthday Wishes, spotify:track:xyz
```

### Age Calculation
The blueprint automatically:
- Calculates the correct age for each birthday
- Handles year transitions properly
- Uses proper ordinal suffixes (1st, 2nd, 3rd, 4th, etc.)
- Accounts for birthdays that have already passed this year

## Troubleshooting

### Common Issues

1. **No Notifications**: Check if presence entity is configured and someone is marked as home
2. **Wrong Age**: Verify birth year in the date format (YYYY-MM-DD)
3. **Music Not Playing**: Ensure media player entity exists and birthday songs are configured
4. **JSON Error**: Validate your birthday data JSON format

### Testing

To test the blueprint:
1. Temporarily change a birth date to tomorrow's date
2. Wait for the next notification time
3. Check that notifications are received
4. Restore the original birth date

## Examples

### Basic Setup
```yaml
Birthday Data: [{"name": "Mom", "date": "1965-03-15"}]
Notification Service: notify.mobile_app_myphone
```

### Full Setup with Music
```yaml
Birthday Data: [
  {"name": "John", "date": "1990-05-15"},
  {"name": "Sarah", "date": "1988-11-22"}
]
Notification Service: notify.alexa_media_echo_dot
Media Player: media_player.living_room_speaker
Presence Entity: person.family
Birthday Songs: Happy Birthday, Birthday Song, Celebration Music
```

## Version History

- **v1.0**: Initial release with multi-person support and smart notifications
- Automatic age calculation with ordinal suffixes
- Flexible timing and notification services
- Optional music and presence detection

## Credits

Converted from ioBroker script to Home Assistant blueprint, maintaining core functionality while adding Home Assistant-specific features and improved flexibility. 