# Home Assistant Blueprints Collection

Home Assistant Blueprints converted from original ioBroker scripts. Each blueprint maintains the core functionality while being optimized for Home Assistant's automation system.

## Available Blueprints

### 🏠 Smart Welcome Greeter
Intelligent welcome greeting system with multiple greeting types, information notifications, and smart lockout functionality. Announces mail, waste collection reminders, and open window warnings.

[📖 Documentation](./SmartWelcomeGreeter/) | [![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A//raw.githubusercontent.com/n3roGit/HomeAssistant/main/SmartWelcomeGreeter/SmartWelcomeGreeter.yaml)

### 🐾 Cat Litter Box Counter and Monitor
Comprehensive cat litter box monitoring with usage tracking, cleaning reminders, and tool monitoring.

[📖 Documentation](./CatShitCounter/) | [![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A//raw.githubusercontent.com/n3roGit/HomeAssistant/main/CatShitCounter/CatShitCounter.yaml)

### 🎂 Birthday Reminder with Smart Notifications
Automated birthday reminders and congratulations for multiple people. Provides different messages based on days remaining until birthday, with optional music playback and presence detection.

[📖 Documentation](./BirthdayReminder/) | [![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A//raw.githubusercontent.com/n3roGit/HomeAssistant/main/BirthdayReminder/BirthdayReminder.yaml)

### ❄️ Smart Frost & Ice Warning System
Intelligent frost and ice warnings based on weather data and temperature sensors. Perfect for knowing when to scrape ice from windscreens or protect plants and outdoor equipment.

[📖 Documentation](./FrostWarning/) | [![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A//raw.githubusercontent.com/n3roGit/HomeAssistant/main/FrostWarning/FrostWarning.yaml)

### 🔊 Alexa Echo Volume Control
Automatically adjusts volume levels of Alexa Echo devices based on mode changes (night mode, presence detection). Specifically designed for Home Assistant's Alexa Media Player integration with pattern-based filtering and special device handling like the original ioBroker script.

[📖 Documentation](./SmartVolumeControl/) | [![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A//raw.githubusercontent.com/n3roGit/HomeAssistant/main/SmartVolumeControl/SmartVolumeControl.yaml)

### 🔔 Doorbell Camera Notification with Door Opener
Sends actionable notifications with camera snapshots when someone rings the doorbell. Includes a remote door opener button and dashboard integration. Perfect for front door monitoring and remote access control.

[📖 Documentation](./DoorbellCameraNotification/) | [![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A//raw.githubusercontent.com/n3roGit/HomeAssistant/main/DoorbellCameraNotification/DoorbellCameraNotification.yaml)

### 💡 Motion-Activated Light Off
Automatically turns off lights after a specified time when no motion is detected. Perfect for energy saving and convenience in rooms where you want lights to automatically turn off when not in use.

[📖 Documentation](./MotionActivatedLightOff/) | [![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A//raw.githubusercontent.com/n3roGit/HomeAssistant/main/MotionActivatedLightOff/MotionActivatedLightOff.yaml)

---

## Features Overview

| Blueprint | Key Features | Use Cases |
|-----------|-------------|-----------|
| **Smart Welcome Greeter** | Multi-greeting types, info notifications, lockout protection | Entrance automation, information system |
| **Cat Litter Box Counter** | Usage tracking, cleaning reminders, tool monitoring | Pet care automation |
| **Birthday Reminder** | Multi-person support, age calculation, music integration | Family reminders, celebration planning |
| **Frost Warning** | Dual warning levels, multiple temp sources, real-time updates | Car windscreen, plant protection |
| **Alexa Echo Volume Control** | Echo-specific volume control, ignore patterns, special device handling | Night mode automation, Echo device management |
| **Doorbell Camera Notification** | Photo snapshots, actionable notifications, door opener, dashboard integration | Doorbell monitoring, remote access control |
| **Motion-Activated Light Off** | Automatic light control, motion detection, timer cancellation, energy saving | Kitchen, bathroom, hallway, workshop automation |

## 🚀 Development Environment

This project includes a complete development environment for testing and developing Home Assistant blueprints locally.

### Quick Start with Dev Containers

1. **Prerequisites**: Install [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. **Open Project**: Open this repository in VS Code
3. **Start Container**: Press `Ctrl+Shift+P` and run `Dev Containers: Reopen in Container`
4. **Launch Home Assistant**: Use the provided tasks to start HA locally
5. **Test Blueprints**: Import and test your blueprints at `http://localhost:8123`

### Development Features

- **Local Home Assistant Instance**: Test blueprints in a real HA environment
- **Pre-configured Test Entities**: Motion sensors, door sensors, presence detection, etc.
- **Debug Support**: Set breakpoints and debug automation execution
- **Docker Support**: Optional Docker-based setup with MQTT and InfluxDB
- **Validation Tools**: Built-in YAML validation and configuration checking

📖 [Detailed Development Guide](.devcontainer/README.md)

## How to Use

### For End Users
1. Click the "Import Blueprint" button for any blueprint
2. Follow the setup instructions in each blueprint's documentation
3. Create required helper entities as specified
4. Configure the automation with your sensors and preferences

### For Developers
1. Use the development environment to test blueprints locally
2. Import blueprints into the local Home Assistant instance
3. Test with the provided mock entities
4. Validate and debug before publishing

## Requirements

- Home Assistant 2023.4+
- Helper entities (counters, input booleans) as specified in each blueprint
- Appropriate sensors/integrations for each blueprint's functionality

### Development Requirements
- Visual Studio Code with Dev Containers extension
- Docker Desktop (for Docker-based development)
- 4GB RAM minimum (8GB recommended)

## Blueprint Structure

Each blueprint includes:
- 📝 **YAML Blueprint**: Ready-to-import automation blueprint
- 📖 **Comprehensive README**: Setup instructions, examples, troubleshooting
- 🔧 **Flexible Configuration**: Adaptable to various hardware and preferences
- 🏠 **Home Assistant Native**: Optimized for HA's automation system

## Credits

Originally converted from ioBroker scripts, these blueprints have been enhanced with Home Assistant-specific features while maintaining their core functionality and reliability. 