"""Coordinator."""

from homeassistant.core import HomeAssistant


class VehicleWeatherCoordinator:
    """Vehicle Weather Coordinator."""

    def __init__(self, hass: HomeAssistant) -> None:
        self.hass = hass
        self.risk = 0