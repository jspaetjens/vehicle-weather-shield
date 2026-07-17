"""Test Vehicle Weather Shield constants."""

from custom_components.vehicle_weather_shield.const import DOMAIN


def test_domain():
    """Test integration domain."""
    assert DOMAIN == "vehicle_weather_shield"