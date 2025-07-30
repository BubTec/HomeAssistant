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

        # Determine path to Home Assistant ``customize.yaml``.  Depending on
        # the AppDaemon setup ``self.config_dir`` may either point directly to
        # the Home Assistant config directory (e.g. ``/config``) or to a
        # subdirectory like ``/config/appdaemon``.  To ensure the file ends up
        # beside ``configuration.yaml`` we strip a trailing ``appdaemon`` if
        # present.
        ha_config = Path(self.config_dir)
        if ha_config.name == "appdaemon":
            ha_config = ha_config.parent
        out_path = ha_config / "customize.yaml"

        try:
            with open(out_path, "w", encoding="utf-8") as f:
                yaml.safe_dump(
                    customize,
                    f,
                    allow_unicode=True,
                    default_flow_style=False,
                    sort_keys=False,
                )
            self.log(
                "Generated customize.yaml with %d entries at %s"
                % (len(customize), out_path)
            )
        except Exception as err:
            self.error(f"Error writing customize.yaml: {err}")
