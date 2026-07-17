"""Config flow for Vehicle Weather Shield."""

from typing import Any

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN


class VehicleWeatherShieldConfigFlow(
    config_entries.ConfigFlow,
    domain=DOMAIN,
):
    """Handle a config flow for Vehicle Weather Shield."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> FlowResult:
        """Handle the initial setup."""

        if user_input is not None:
            return self.async_create_entry(
                title="Vehicle Weather Shield",
                data=user_input,
            )

        schema = vol.Schema(
            {
                vol.Required(
                    "vehicle_name",
                    default="My Vehicle",
                ): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )