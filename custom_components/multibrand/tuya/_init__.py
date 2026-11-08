"""Tuya integration for Home Assistant - Multibrand support."""

from homeassistant.const import CONF_HOST

NAME = "Tuya"
DOMAIN = "tuya"
MANUFACTURER = "Tuya"
DEFAULT_PORT = 6666

# Tuya specific constants
BRAND_SPECIFIC = {
    "cloud_url": "https://tuya.com",
    "mcu_protocol": "https://developer.tuya.com",
}

# Import complete product catalog (single file)
from .products import TUYA_PRODUCTS

__all__ = ["TUYA_PRODUCTS"]
