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

# Import complete product catalog
from .products_part1 import TUYA_PRODUCTS
from .products_part2 import TUYA_PRODUCTS

__all__ = ["TUYA_PRODUCTS"]
