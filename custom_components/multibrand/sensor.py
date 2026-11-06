"""Sensor platform for Multibrand integration."""
import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    multibrand_data = hass.data.get(DOMAIN, {})
    devices = multibrand_data.get("devices", {})
    all_products = multibrand_data.get("all_products", {})
    
    entities = []

    for brand, info in devices.items():
        # Get all products for this brand
        brand_products = []
        for product_id, product_data in all_products.items():
            if product_id.startswith(brand + "_"):
                product_data_copy = product_data.copy()
                product_data_copy['brand'] = brand
                brand_products.append(product_data_copy)
        
        for product in brand_products:
            entities.append(MultibrandSensor(product))

    async_add_entities(entities, True)


class MultibrandSensor(SensorEntity):
    """Representation of a multibrand sensor."""

    def __init__(self, product: dict[str, Any]):
        """Initialize the sensor."""
        self._product = product
        self._attr_name = f"{product['name']} sensor"
        self._attr_unique_id = f"{product['id']}_sensor"
        self._attr_has_entity_name = True
        self._attr_available = False

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return self._attr_name

    @property
    def unique_id(self) -> str:
        """Return a unique ID."""
        return self._attr_unique_id

    @property
    def state(self) -> Any:
        """Return the state of the sensor."""
        return self._product.get("power", "unknown")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return state attributes."""
        return {
            "brand": self._product.get("brand"),
            "product_type": self._product.get("type"),
            "product_id": self._product.get("name"),
            "config": self._product,
        }
