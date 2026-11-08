"""Config flow for Multibrand integration."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant, callback

from const import DOMAIN


class MultibrandConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Multibrand."""

    VERSION = 1
    _async_step_user_completed: bool = False

    async def async_step_user(self, user_input=None) -> config_entries.FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            return self.async_create_entry(title="Multibrand", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )


class MultibrandOptionsFlow(config_entries.OptionsFlow):
    """Handle options flow for Multibrand."""

    async def async_step_init(self, user_input=None) -> config_entries.FlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(step_id="init", data_schema=vol.Schema({}))


@callback
def _async_get_options_flow(config_entry: config_entries.ConfigEntry) -> config_entries.OptionsFlow:
    """Get the options flow for this handler."""
    return MultibrandOptionsFlow(config_entry)
