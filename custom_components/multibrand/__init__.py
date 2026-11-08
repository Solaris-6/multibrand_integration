import logging

from . import const

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry):
    """Set up multibrand from a config entry."""
    _LOGGER.debug("Setting up multibrand entry: %s", entry.title)
    hass.data.setdefault(const.DOMAIN, {})
    return True

async def async_unload_entry(hass, entry):
    """Unload a multibrand from hass."""
    return True