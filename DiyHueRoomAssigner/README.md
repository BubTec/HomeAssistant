# DiyHue Room Assigner (AppDaemon)

This AppDaemon app writes a `customize.yaml` file that assigns each light entity a
`diyhue_room` attribute based on the entity's Home Assistant area. Use this
file with diyHue to import your lights with the correct room names.

## Usage
1. Install the app into your AppDaemon `apps` directory.
2. Configure it in `apps.yaml`:

```yaml
room_assigner:
  module: diyhue_room_assigner
  class: DiyHueRoomAssigner
```

3. Restart AppDaemon. The generated `customize.yaml` will be placed in your
Home Assistant config folder (the same folder that contains `configuration.yaml`).

If a light entity does not belong to an area it will be skipped.
