"""Multibrand integration for Home Assistant."""
import asyncio
import logging
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST
from homeassistant.core import HomeAssistant
from homeassistant.helpers import discovery
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN, BRANDS

_LOGGER = logging.getLogger(__name__)

# Import constants
from .const import DOMAIN, BRANDS

# Import all brand product catalogs
from .shelly import SHELLY_PRODUCTS
from .sonoff import SONOFF_PRODUCTS
from .tuya import TUYA_PRODUCTS
from .bticino import BTICINO_PRODUCTS
from .vimar import VIMAR_PRODUCTS

# Complete smart product catalog for all brands
ALL_PRODUCTS = {
    **SHELLY_PRODUCTS,
    **SONOFF_PRODUCTS,
    **TUYA_PRODUCTS,
    **BTICINO_PRODUCTS,
    **VIMAR_PRODUCTS,
}

# Device discovery cache
DISCOVERED_DEVICES: dict[str, Any] = {}


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the multibrand integration (legacy YAML setup)."""
    _LOGGER.warning("Multibrand integration is now configured via ConfigEntry. "
                   "YAML setup is deprecated.")
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up multibrand from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN].setdefault("devices", {})
    hass.data[DOMAIN]["all_products"] = ALL_PRODUCTS

    # Get host from config entry or use default discovery IP
    host = entry.data.get(CONF_HOST, "192.168.1.1")
    _LOGGER.info("Configured host for discovery: %s", host)

    async def discover_devices():
        """Discover devices on the local network."""
        session = async_get_clientsession(hass)
        discovered = {}

        # Probe Shelly devices (legacy - use config entry integration instead)
        try:
            async with session.get(f"http://{host}/rpc", timeout=2) as resp:
                if resp.status == 200:
                    discovered["shelly"] = {"status": "online", "models": list(SHELLY_PRODUCTS.keys())}
        except Exception:
            pass

        # Probe Sonoff devices (legacy - use config entry integration instead)
        try:
            async with session.get(f"http://{host}:8080", timeout=2) as resp:
                if resp.status == 200:
                    discovered["sonoff"] = {"status": "online", "models": list(SONOFF_PRODUCTS.keys())}
        except Exception:
            pass

        # Probe Tuya devices (legacy - use config entry integration instead)
        try:
            async with session.get(f"http://{host}/sm", timeout=2) as resp:
                if resp.status == 200:
                    discovered["tuya"] = {"status": "online", "models": list(TUYA_PRODUCTS.keys())}
        except Exception:
            pass

        return discovered

    # Discover devices on startup (legacy discovery)
    DISCOVERED_DEVICES = await discover_devices()
    _LOGGER.info("Discovered devices: %s", DISCOVERED_DEVICES)

    # Store discovered devices for platforms (legacy)
    hass.data[DOMAIN]["devices"] = DISCOVERED_DEVICES

    # Register platforms (legacy YAML setup - still supported but deprecated)
    await discovery.async_load_platform(hass, "sensor", DOMAIN, {}, config)
    await discovery.async_load_platform(hass, "switch", DOMAIN, {}, config)
    await discovery.async_load_platform(hass, "device_tracker", DOMAIN, {}, config)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, ["sensor", "switch", "device_tracker"])
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unload_ok
