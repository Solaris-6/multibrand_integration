"""Multibrand integration for Home Assistant."""
import asyncio
import logging
from homeassistant.helpers import discovery
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.const import CONF_HOST

_LOGGER = logging.getLogger(__name__)

DOMAIN = "multibrand"
BRANDS = ["shelly", "sonoff", "tuya", "bticino", "vimar"]

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
DISCOVERED_DEVICES = {}


async def async_setup(hass, config):
    """Set up the multibrand integration."""
    hass.data.setdefault(DOMAIN, {})

    async def discover_devices():
        """Discover devices on the local network."""
        session = async_get_clientsession(hass)
        discovered = {}

        # Probe Shelly devices
        try:
            async with session.get("http://192.168.1.1/rpc", timeout=2) as resp:
                if resp.status == 200:
                    discovered["shelly"] = {"status": "online", "models": SHELLY_PRODUCTS.keys()}
        except Exception:
            pass

        # Probe Sonoff devices (eWeLink local API)
        try:
            async with session.get("http://192.168.1.1:8080", timeout=2) as resp:
                if resp.status == 200:
                    discovered["sonoff"] = {"status": "online", "models": SONOFF_PRODUCTS.keys()}
        except Exception:
            pass

        # Probe Tuya devices
        try:
            async with session.get("http://192.168.1.1:6666", timeout=2) as resp:
                if resp.status == 200:
                    discovered["tuya"] = {"status": "online", "models": TUYA_PRODUCTS.keys()}
        except Exception:
            pass

        # Probe Bticino/Vimar (custom APIs)
        for brand in ["bticino", "vimar"]:
            try:
                async with session.get(f"http://192.168.1.1/{brand}", timeout=2) as resp:
                    if resp.status == 200:
                        discovered[brand] = {"status": "online", "models": BTICINO_PRODUCTS.keys() if brand == "bticino" else VIMAR_PRODUCTS.keys()}
            except Exception:
                pass

        return discovered

    discovered = await discover_devices()
    _LOGGER.info("Discovered devices: %s", discovered)

    # Store discovered devices for platforms
    hass.data[DOMAIN]["devices"] = discovered
    hass.data[DOMAIN]["all_products"] = ALL_PRODUCTS

    # Register platforms
    await discovery.async_load_platform(hass, "sensor", DOMAIN, {}, config)
    await discovery.async_load_platform(hass, "switch", DOMAIN, {}, config)
    await discovery.async_load_platform(hass, "device_tracker", DOMAIN, {}, config)

    return True


async def async_unload_platforms(hass, platforms):
    """Unload platforms."""
    unload_ok = True
    for platform in platforms:
        unload_ok = await hass.config_entries.async_unload_platform(hass, DOMAIN, platform) and unload_ok
    return unload_ok
