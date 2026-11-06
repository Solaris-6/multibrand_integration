"""Shelly integration for Home Assistant - Multibrand support."""
from homeassistant.const import CONF_HOST

NAME = "Shelly"
DOMAIN = "shelly"
MANUFACTURER = "Shelly"
DEFAULT_PORT = 80

# Shelly specific constants
BRAND_SPECIFIC = {
    "rpc_endpoint": "/rpc",
    "cloud_url": "https://shelly.cloud",
    "model_prefix": "SHELLY",
}

# Import complete product catalog
from .products_part1 import SHELLY_PRODUCTS

__all__ = ["SHELLY_PRODUCTS"]
