"""Sensors."""

from homeassistant.components.sensor import SensorEntity

from .const import NAME


async def async_setup_entry(hass, entry, async_add_entities):

    async_add_entities([VehicleWeatherRiskSensor()])


class VehicleWeatherRiskSensor(SensorEntity):

    _attr_name = "Vehicle Weather Shield Risk"

    _attr_native_unit_of_measurement = "%"

    _attr_icon = "mdi:weather-lightning"

    @property
    def native_value(self):
        return 0