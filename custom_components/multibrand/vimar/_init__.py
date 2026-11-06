"""Vimar integration for Home Assistant - Multibrand support."""
from homeassistant.const import CONF_HOST

NAME = "Vimar"
DOMAIN = "vimar"
MANUFACTURER = "Vimar"
DEFAULT_PORT = 80

# Vimar specific constants
BRAND_SPECIFIC = {
    "web_portal": "https://www.vimar.com",
    "support_email": "info@vimar.com",
}

# Import complete product catalog
from .products import VIMAR_PRODUCTS

__all__ = ["VIMAR_PRODUCTS"]
