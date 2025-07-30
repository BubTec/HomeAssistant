import os
import yaml
import appdaemon.plugins.hass.hassapi as hass

class DiyHueRoomAssigner(hass.Hass):
    """Assigns each light entity a diyhue_room attribute based on its area."""

    def initialize(self):
        # Collect all light entities
        states = self.get_state()
        lights = {
            entity_id: data
            for entity_id, data in states.items()
            if entity_id.startswith("light.")
        }

        # Get all area IDs
        area_ids = self.areas()

        # Build mapping of area_id -> area_name
        areas = {aid: self.area_name(aid) for aid in area_ids}

        customize = {}
        for entity_id, state in lights.items():
            aid = state.get("attributes", {}).get("area_id")
            if aid and aid in areas:
                customize[entity_id] = {"diyhue_room": areas[aid]}

        # Determine path to Home Assistant customize.yaml
        config_dir = str(self.config_dir)
        out_path = os.path.join(os.path.dirname(config_dir), "customize.yaml")

        try:
            with open(out_path, "w", encoding="utf-8") as f:
                yaml.dump(customize, f, allow_unicode=True)
            self.log(
                f"Erzeugt customize.yaml mit {len(customize)} Einträgen unter {out_path}"
            )
        except Exception as err:
            self.error(f"Fehler beim Schreiben von customize.yaml: {err}")
