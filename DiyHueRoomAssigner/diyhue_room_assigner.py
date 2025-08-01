from pathlib import Path
import yaml
import appdaemon.plugins.hass.hassapi as hass

class DiyHueRoomAssigner(hass.Hass):
    """Assigns each light entity a diyhue_room attribute based on its area."""

    def initialize(self):
        # Collect all light entities and their state
        lights = self.get_state("light") or {}

        # Build customize mapping by resolving the area_id attribute of each
        # light to an area name. ``self.area_name`` expects an ``area_id`` and
        # returns the matching name.
        customize = {}
        for entity_id, state in lights.items():
            aid = state.get("attributes", {}).get("area_id")
            if aid:
                area = self.area_name(aid)
                if area:
                    customize[entity_id] = {"diyhue_room": area}

        # Determine path to Home Assistant customize.yaml
        # Use the config directory directly rather than its parent so the
        # output ends up in the same folder where Home Assistant expects it
        # (typically ``/config``).
        out_path = Path(self.config_dir) / "customize.yaml"

        try:
            with open(out_path, "w", encoding="utf-8") as f:
                yaml.safe_dump(customize, f, allow_unicode=True)
            self.log(
                f"Generated customize.yaml with {len(customize)} entries at {out_path}"
            )
        except Exception as err:
            self.error(f"Error writing customize.yaml: {err}")
