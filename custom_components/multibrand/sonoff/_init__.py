"""Sonoff integration for Home Assistant - Multibrand support."""
from homeassistant.const import CONF_HOST

NAME = "Sonoff"
DOMAIN = "sonoff"
MANUFACTURER = "Sonoff"
DEFAULT_PORT = 8080

# Sonoff specific constants
BRAND_SPECIFIC = {
    "cloud_url": "https://ewe-link.cn",
    "default_region": "eu",
}

# Import complete product catalog
from .products_part1 import SONOFF_PRODUCTS
from .products_part2 import SONOFF_PRODUCTS

__all__ = ["SONOFF_PRODUCTS"]
