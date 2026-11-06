"""Bticino integration for Home Assistant - Multibrand support."""
from homeassistant.const import CONF_HOST

NAME = "Bticino"
DOMAIN = "bticino"
MANUFACTURER = "Bticino"
DEFAULT_PORT = 80

# Bticino specific constants
BRAND_SPECIFIC = {
    "web_portal": "https://www.bticino.com",
    "support_email": "support@bticino.com",
}

# Import complete product catalog
from .products import BTICINO_PRODUCTS

__all__ = ["BTICINO_PRODUCTS"]
