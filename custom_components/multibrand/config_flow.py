import logging
from homeassistant import config_entries
from homeassistant.core import callback

_LOGGER = logging.getLogger(__name__)

class MultibrandConfigFlow(config_entries.ConfigFlow, domain="multibrand"):
    """Config flow for multibrand integration."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return None

    async def async_step_user(self, user_input=None):
        """Handle the first step of the config flow."""
        if user_input is not None:
            return self.async_create_entry(
                title="Multibrand Integration",
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=None,
            description_placeholders=None,
        )

    async def async_step_reauth(self, user_input=None):
        """Handle re-authentication."""
        return self.async_abort(reason="reauth_not_supported")

class MultibrandConfigEntry(config_entries.ConfigEntry):
    """Config entry for multibrand integration."""

    _version = 1