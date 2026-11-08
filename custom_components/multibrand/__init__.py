"""Multibrand integration for Home Assistant."""
import logging
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, BRANDS

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the multibrand integration (legacy YAML setup - deprecated)."""
    _LOGGER.warning("Multibrand integration is now configured via ConfigEntry. "
                   "YAML setup is deprecated and will be removed in future versions.")
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up multibrand from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN].setdefault("devices", {})
    hass.data[DOMAIN]["all_products"] = {}

    # Import product catalogs dynamically to avoid circular imports
    try:
        from .shelly import SHELLY_PRODUCTS
        from .sonoff import SONOFF_PRODUCTS
        from .tuya import TUYA_PRODUCTS
        from .bticino import BTICINO_PRODUCTS
        from .vimar import VIMAR_PRODUCTS

        # Complete smart product catalog for all brands
        hass.data[DOMAIN]["all_products"] = {
            **SHELLY_PRODUCTS,
            **SONOFF_PRODUCTS,
            **TUYA_PRODUCTS,
            **BTICINO_PRODUCTS,
            **VIMAR_PRODUCTS,
        }
    except ImportError as err:
        _LOGGER.error("Failed to import product catalogs: %s", err)
        return False

    # Discover devices on startup (optional legacy discovery)
    try:
        host = entry.data.get("host", "192.168.1.1") if hasattr(entry, 'data') else "192.168.1.1"
        _LOGGER.info("Configured host for discovery: %s", host)
    except Exception as err:
        _LOGGER.warning("Could not get host from config entry: %s", err)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, ["sensor", "switch", "device_tracker"])
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unload_ok
